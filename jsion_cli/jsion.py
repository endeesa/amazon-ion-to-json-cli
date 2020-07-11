from cmdline_options_reader import read_cmdline_options
from shared_module import JSIONException


def main():
    cmdline_options = read_cmdline_options()
    print(cmdline_options)

if __name__ == "__main__":
    main()