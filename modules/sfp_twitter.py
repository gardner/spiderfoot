#-------------------------------------------------------------------------------
# Name:         sfp_twitter
# Purpose:      Query Twitter for name and location information.
#
# Author:      <bcoles@gmail.com>
#
# Created:     2018-10-17
# Copyright:   (c) bcoles 2018
# Licence:     GPL
#-------------------------------------------------------------------------------

import re

from sflib import SpiderFootPlugin, SpiderFootEvent

class sfp_twitter(SpiderFootPlugin):
    """Twitter:Footprint,Investigate,Passive:Social Media::Gather name and location from Twitter profiles."""

    meta = {
        'name': "Twitter",
        'summary': "Gather name and location from Twitter profiles.",
        'flags': [""],
        'useCases': ["Footprint", "Investigate", "Passive"],
        'categories': ["Social Media"],
        'dataSource': {
            'website': "https://twitter.com/",
            'model': "FREE_NOAUTH_UNLIMITED",
            'references': [],
            'favIcon': "https://abs.twimg.com/favicons/twitter.ico",
            'logo': "https://abs.twimg.com/responsive-web/web/icon-ios.8ea219d4.png",
            'description': "Twitter is an American microblogging and social networking service "
                                "on which users post and interact with messages known as \"tweets\". "
                                "Registered users can post, like, and retweet tweets, but unregistered users can only read them.",
        }
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.__dataSource__ = "Twitter"
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        return ["SOCIAL_MEDIA"]

    # What events this module produces
    def producedEvents(self):
        return ["RAW_RIR_DATA", "GEOINFO"]

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return None
        else:
            self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        # Retrieve profile
        try:
            network = eventData.split(": ")[0]
            url = eventData.split(": ")[1].replace("<SFURL>", "").replace("</SFURL>", "")
        except BaseException as e:
            self.sf.error("Unable to parse SOCIAL_MEDIA: " +
                          eventData + " (" + str(e) + ")", False)
            return None

        if not network == "Twitter":
            self.sf.debug("Skipping social network profile, " + url + ", as not a Twitter profile")
            return None

        res = self.sf.fetchUrl(url, timeout=self.opts['_fetchtimeout'],
                               useragent="SpiderFoot")

        if res['content'] is None:
            return None

        if not res['code'] == "200":
            self.sf.debug(url + " is not a valid Twitter profile")
            return None

        # Retrieve name
        human_name = re.findall(r'<div class="fullname">([^<]+)\s*</div>',
                                res['content'], re.MULTILINE)

        if human_name:
            e = SpiderFootEvent("RAW_RIR_DATA", "Possible full name: " + human_name[0],
                                self.__name__, event)
            self.notifyListeners(e)

        # Retrieve location
        location = re.findall(r'<div class="location">([^<]+)</div>', res['content'])

        if location:
            if len(location[0]) < 3 or len(location[0]) > 100:
                self.sf.debug("Skipping likely invalid location.")
            else:
                e = SpiderFootEvent("GEOINFO", location[0], self.__name__, event)
                self.notifyListeners(e)

# End of sfp_twitter class
