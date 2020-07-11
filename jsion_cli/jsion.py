from abc import ABC, abstractmethod, abstractproperty
from cmdline_options_reader import read_cmdline_options, CommandLineOptions
from shared_module import JSIONException


class ConverterConfiguration:
    __slots__ = ['_cli_options']

    def __init__(self, cli_options: CommandLineOptions) -> None:
        self._cli_options = cli_options

    @property
    def cli_options(self):
        return self._cli_options


class JSIONConverterBase(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def convert():
        pass


class JSIONConvertIonToJson(JSIONConverterBase):
    pass



class JSIONConvertJsonToIon(JSIONConverterBase):
    pass



def converter_factory(cmdline_options: CommandLineOptions) -> JSIONConverterBase:
    config = ConverterConfiguration(cmdline_options)
    return JSIONConvertIonToJson(config) if cmdline_options.reverse_conversion else JSIONConvertJsonToIon(config)
    


def main():
    print("JSION cli converter init...")
    cmdline_options = read_cmdline_options()
    print(cmdline_options)

    config = ConverterConfiguration(cmdline_options)
    converter_instance = converter_factory(cmdline_options)
    converter_instance.convert()

if __name__ == "__main__":
    main()