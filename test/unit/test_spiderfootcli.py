# test_spiderfootcli.py
import io
import subprocess
import sys
import unittest

from sfcli import SpiderFootCli


class TestSpiderFootCli(unittest.TestCase):
    """
    Test TestSpiderFootCli
    """

    default_options = {
        "cli.debug": False,
        "cli.silent": False,
        "cli.color": True,
        "cli.output": "pretty",
        "cli.history": True,
        "cli.history_file": "",
        "cli.spool": False,
        "cli.spool_file": "",
        "cli.ssl_verify": True,
        "cli.username": "",
        "cli.password": "",
        "cli.server_baseurl": "http://127.0.0.1:5001"
    }

    def execute(self, command):
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = proc.communicate()
        return out, err, proc.returncode

    def test_help_arg_should_print_help_and_exit(self):
        out, err, code = self.execute([sys.executable, "sfcli.py", "-h"])
        self.assertIn(b"show this help message and exit", out)
        self.assertEqual(b"", err)
        self.assertEqual(0, code)

    def test_default(self):
        """
        Test default(self, line)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.default("")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("Unknown command", output)

    def test_default_should_ignore_comments(self):
        """
        Test default(self, line)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        result = sfcli.default("# test comment")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertEqual(None, result)
        self.assertEqual("", output)

    def test_complete_start_should_return_a_list(self):
        """
        Test complete_start(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        start = sfcli.complete_start(None, None, None, None)
        self.assertIsInstance(start, list)
        self.assertEqual([], start)

    def test_complete_find_should_return_a_list(self):
        """
        Test complete_find(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        find = sfcli.complete_find(None, None, None, None)
        self.assertIsInstance(find, list)
        self.assertEqual([], find)

    def test_complete_data_should_return_a_list(self):
        """
        Test complete_data(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        data = sfcli.complete_data(None, None, None, None)
        self.assertIsInstance(data, list)
        self.assertEqual([], data)

    def test_complete_default(self):
        """
        Test complete_default(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        default = sfcli.complete_default("", "-t -m", None, None)
        self.assertIsInstance(default, list)
        self.assertEqual('TBD', 'TBD')

        default = sfcli.complete_default("", "-m -t", None, None)
        self.assertIsInstance(default, list)
        self.assertEqual('TBD', 'TBD')

    def test_complete_default_invalid_text_should_return_a_string(self):
        """
        Test complete_default(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        default = sfcli.complete_default(None, "example line", None, None)
        self.assertIsInstance(default, list)
        self.assertEqual([], default)

    def test_complete_default_invalid_line_should_return_a_string(self):
        """
        Test complete_default(self, text, line, startidx, endidx)
        """
        sfcli = SpiderFootCli()
        default = sfcli.complete_default("example text", None, None, None)
        self.assertIsInstance(default, list)
        self.assertEqual([], default)

    def test_dprint(self):
        """
        Test dprint(self, msg, err=False, deb=False, plain=False, color=None)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.dprint("example output")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("example output", output)

    @unittest.skip("todo")
    def test_do_debug_should_toggle_debug(self):
        """
        Test do_debug(self, line)
        """
        sfcli = SpiderFootCli(self.default_options)

        sfcli.do_debug(0)
        initial_debug_state = sfcli.ownopts['cli.debug']
        sfcli.do_debug(1)
        new_debug_state = sfcli.ownopts['cli.debug']

        self.assertNotEqual(initial_debug_state, new_debug_state)

    @unittest.skip("todo")
    def test_do_spool_should_toggle_spool(self):
        """
        Test do_spool(self, line)
        """
        sfcli = SpiderFootCli()

        sfcli.ownopts['cli.spool_file'] = '/dev/null'

        sfcli.do_spool(0)
        initial_spool_state = sfcli.ownopts['cli.spool']
        sfcli.do_spool(1)
        new_spool_state = sfcli.ownopts['cli.spool']

        self.assertNotEqual(initial_spool_state, new_spool_state)

    @unittest.skip("todo")
    def test_do_history(self):
        """
        Test do_history(self, line)
        """
        sfcli = SpiderFootCli(self.default_options)

        sfcli.do_history(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_precmd_should_print_line_to_history_file(self):
        """
        Test precmd(self, line)
        """
        sfcli = SpiderFootCli()

        line = "example line"

        precmd = sfcli.precmd(line)

        self.assertEqual(line, precmd)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_precmd_should_print_line_to_spool_file(self):
        """
        Test precmd(self, line)
        """
        sfcli = SpiderFootCli()

        line = "example line"

        precmd = sfcli.precmd(line)

        self.assertEqual(line, precmd)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_precmd_should_return_line(self):
        """
        Test precmd(self, line)
        """
        sfcli = SpiderFootCli()

        line = "example line"

        precmd = sfcli.precmd(line)

        self.assertEqual(line, precmd)

    @unittest.skip("todo")
    def test_ddprint(self):
        """
        Test ddprint(self, msg)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.ddprint("example debug output")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("example debug output", output)

        self.assertEqual('TBD', 'TBD')

    def test_edprint(self):
        """
        Test edprint(self, msg)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.edprint("example debug output")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("example debug output", output)

    def test_pretty_should_return_a_string(self):
        """
        Test pretty(self, data, titlemap=None)
        """
        sfcli = SpiderFootCli()

        invalid_types = [None, "", list(), dict()]
        for invalid_type in invalid_types:
            with self.subTest(invalid_type=invalid_type):
                pretty = sfcli.pretty(invalid_type)
                self.assertEqual("", pretty)

    @unittest.skip("todo")
    def test_request(self):
        """
        Test request(self, url, post=None)
        """
        sfcli = SpiderFootCli()
        sfcli.request(None, None)

        self.assertEqual('TBD', 'TBD')

    def test_request_invalid_url_should_return_none(self):
        """
        Test request(self, url, post=None)
        """
        sfcli = SpiderFootCli()

        invalid_types = [None, list(), dict()]
        for invalid_type in invalid_types:
            with self.subTest(invalid_type=invalid_type):
                result = sfcli.request(invalid_type)
                self.assertEqual(None, result)

    def test_emptyline_should_return_none(self):
        """
        Test emptyline(self)
        """
        sfcli = SpiderFootCli()
        emptyline = sfcli.emptyline()
        self.assertEqual(None, emptyline)

    def test_completedefault_should_return_empty_list(self):
        """
        Test completedefault(self, text, line, begidx, endidx)
        """
        sfcli = SpiderFootCli()
        completedefault = sfcli.completedefault(None, None, None, None)
        self.assertIsInstance(completedefault, list)
        self.assertEqual([], completedefault)

    def test_myparseline_should_return_a_list_of_two_lists(self):
        """
        Test myparseline(self, cmdline, replace=True)
        """
        sfcli = SpiderFootCli()
        parsed_line = sfcli.myparseline("")

        self.assertEqual(len(parsed_line), 2)
        self.assertIsInstance(parsed_line, list)
        self.assertIsInstance(parsed_line[0], list)
        self.assertIsInstance(parsed_line[1], list)

    def test_send_output(self):
        """
        Test send_output(self, data, cmd, titles=None, total=True, raw=False)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.send_output("{}", "", raw=True)
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("Total records: 0", output)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_query(self):
        """
        Test do_query(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_query(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_ping(self):
        """
        Test do_ping(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_ping(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_modules(self):
        """
        Test do_modules(self, line, cacheonly=False)
        """
        sfcli = SpiderFootCli()
        sfcli.do_modules(None, None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_types(self):
        """
        Test do_types(self, line, cacheonly=False)
        """
        sfcli = SpiderFootCli()
        sfcli.do_types(None, None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_load(self):
        """
        Test do_load(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_load(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_scaninfo(self):
        """
        Test do_scaninfo(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_scaninfo(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_scans(self):
        """
        Test do_scans(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_scans(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_data(self):
        """
        Test do_data(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_data(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_export(self):
        """
        Test do_export(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_export(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_logs(self):
        """
        Test do_logs(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_logs(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_start(self):
        """
        Test do_start(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_start(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_stop(self):
        """
        Test do_stop(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_stop(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_search(self):
        """
        Test do_search(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_search(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_find(self):
        """
        Test do_find(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_find(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_summary(self):
        """
        Test do_summary(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_summary(None)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_delete(self):
        """
        Test do_delete(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_delete(None)

        self.assertEqual('TBD', 'TBD')

    def test_print_topic(self):
        """
        Test print_topics(self, header, cmds, cmdlen, maxcol)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.print_topics(None, "help", None, None)
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("Command", output)
        self.assertIn("Description", output)

        self.assertEqual('TBD', 'TBD')

    @unittest.skip("todo")
    def test_do_set(self):
        """
        Test do_set(self, line)
        """
        sfcli = SpiderFootCli()
        sfcli.do_set(None)

        self.assertEqual('TBD', 'TBD')

    def test_do_shell(self):
        """
        Test do_shell(self, line)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stdout = io_output
        sfcli.do_shell("")
        sys.stdout = sys.__stdout__
        output = io_output.getvalue()

        self.assertIn("Running shell command:", output)

    def test_do_clear(self):
        """
        Test do_clear(self, line)
        """
        sfcli = SpiderFootCli()

        io_output = io.StringIO()
        sys.stderr = io_output
        sfcli.do_clear(None)
        sys.stderr = sys.__stderr__
        output = io_output.getvalue()

        self.assertEqual("\x1b[2J\x1b[H", output)

    def test_do_exit(self):
        """
        Test do_exit(self, line)
        """
        sfcli = SpiderFootCli()
        do_exit = sfcli.do_exit(None)
        self.assertTrue(do_exit)

    def test_do_eof(self):
        """
        Test do_EOF(self, line)
        """
        sfcli = SpiderFootCli()
        do_eof = sfcli.do_EOF(None)
        self.assertTrue(do_eof)
