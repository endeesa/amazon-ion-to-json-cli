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
    def __init__(self, config: CommandLineOptions) -> None:
        self._config = config

    @abstractmethod
    def convert():
        pass


class JSIONConvertIonToJson(JSIONConverterBase):
    def __init__(self) -> None:
        self._input_data = None
        self._output_data = None
        self._ion_data = None

    def __load_input_data_from_file(self) -> str:
        input_data = u'%s' % read_file(filename=self._config.input_file)
        if input_data in (None, ''):
            raise JSIONException('Invalid input: \n %s' % input_data)
        self._input_data = input_data
        return input_data

    def __load_ion_data(self):
        ion_data = ion.loads(ion_data_str, single_value=False)
        if isinstance(ion_data, list):
            self._ion_data = ion_data[0]   # TODO: what if len > 1?
        self._ion_data = ion_data
        return ion_data
    
    def __convert_ion_to_json(self):
        json_object = ion_to_json(self._ion_data)
        json_string = json.dumps(json_object)
        self._output_data = json_string
        return json_string


    def __load_actions(self):
        """
        Read input file
        Load ion file
        convert to output
        prettify output
        """
        

    
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