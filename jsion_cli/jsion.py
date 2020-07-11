import json
import amazon.ion.simpleion as ion
from abc import ABC, abstractmethod, abstractproperty
from cmdline_options_reader import read_cmdline_options, CommandLineOptions
from shared_module import JSIONException, read_file
from pyion2json import ion_to_json


class ConverterConfiguration:
    __slots__ = ['_cli_options']

    def __init__(self, cli_options: CommandLineOptions) -> None:
        self._cli_options = cli_options

    @property
    def cli_options(self):
        return self._cli_options


class JSIONConverterBase(ABC):
    def __init__(self, config) -> None:
        self._config = config

    @abstractmethod
    def convert():
        pass


class JSIONConvertIonToJson(JSIONConverterBase):
    def __init__(self) -> None:
        pass

    def __load_actions(self):
        pass

    
    def convert():
        ion_data_str = u'%s' % read_file()
        ion_data = ion.loads(ion_data_str, single_value=False)
        #pretty_ion_data = ion.dumps(ion_data, binary=False, indent='  ')
        json_doc = ion_to_json(ion_data[0])
        json_data = json.dumps(json_doc, indent=' ')
        return json_data




class JSIONConvertJsonToIon(JSIONConverterBase):
    def convert():
        print('ION to Json conversion not yet supported')



def converter_factory(cmdline_options: CommandLineOptions) -> JSIONConverterBase:
    config = ConverterConfiguration(cmdline_options)
    return JSIONConvertIonToJson(config) if cmdline_options.reverse_conversion else JSIONConvertJsonToIon(config)
    


def main():
    print("JsIon cli converter init...")
    cmdline_options = read_cmdline_options()
    print(cmdline_options)

    config = ConverterConfiguration(cmdline_options)
    converter_instance = converter_factory(cmdline_options)
    converter_instance.convert()

if __name__ == "__main__":
    main()