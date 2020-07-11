"""
 Helper module that uses built-in argparse library to extract command line options from sys.argv
"""

__all__ = ['CommandLineOptions', 'read_cmdline_options']

import argparse

parser = argparse.ArgumentParser(description='Convert data from Amazon\'s ion format to json (or vice-versa)')


parser.add_argument('-i', '--infile', dest="input_file", required=True, help='Path to the input file to be converted')

parser.add_argument('-o', '--outfile', dest='output_file', required=False, help='Path to the output file. Output is sent to StdOut by default.')

parser.add_argument('-p', '--pretify', dest='pretify', type=bool, default=False, required=False, help="If false, output will not be formated.")

parser.add_argument('-q', '--quiet', dest='quiet_mode', action='store_true', required=False, help='Turn off debug logs')

parser.add_argument('-r', '--reverse', dest='reverse_conversion', action='store_true', required=False, help="Do the reverse conversion. i.e. Convert ION to JSON")


class CommandLineOptions:
    """
    Wrapper Object to encapsulate all supported command line options
    """

    def __init__(self, namespace_obj):
        self._input_file = namespace_obj.input_file
        self._output_file = namespace_obj.output_file
        self._pretify = namespace_obj.pretify
        self._quiet_mode = namespace_obj.quiet_mode
        self._reverse_conversion = namespace_obj.reverse_conversion

    @property
    def input_file(self) -> str:
        return self._input_file

    @property
    def output_file(self) -> str:
        return self._output_file

    @property
    def pretify(self) -> bool:
        return self._pretify

    @property
    def quiet_mode(self) -> bool:
        return self._quiet_mode

    @property
    def reverse_conversion(self) -> bool:
        return self._reverse_conversion

    def __str__(self):
        """Returns the string representation of the CommandLineOptions object. i.e. str(CommandLineOptions)"""

        cli_args_str = 'Command Line Options\n'
        cli_args_str += '=====\t====\t=====\n'
        cli_args_str += f'Input file \t{self._input_file}\n'
        cli_args_str += f'Output file \t{self._output_file}\n'
        cli_args_str += f'Prettify Output \t{self._pretify}\n'
        cli_args_str += f'Low verbosity \t{self._quiet_mode}\n'
        cli_args_str += f'Covert from Json to Ion \t{self._reverse_conversion}\n'
        return cli_args_str.strip()


def read_cmdline_options() -> CommandLineOptions:
    """Returns an instance of CommandLineOptions"""
    passed_args = CommandLineOptions(parser.parse_args())
    return passed_args
