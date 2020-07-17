import json
import traceback
import amazon.ion.simpleion as ion
from abc import ABC, abstractmethod, abstractproperty
from cmdline_options_reader import read_cmdline_options, CommandLineOptions
from shared_module import JSIONException, JSIONConversionError ,read_file, write_file
from pyion2json import ion_to_json


class JSIONConverterBase(ABC):
    def __init__(self, config: CommandLineOptions) -> None:
        self._config = config

    @abstractmethod
    def convert(self):
        pass


class JSIONConvertIonToJson(JSIONConverterBase):
    def __init__(self, config) -> None:
        super().__init__(config)
        self._input_data = None
        self._output_data = None
        self._ion_data = None
        self._tasks = []

    def __load_input_data_from_file(self) -> str:
        input_data = u'%s' % read_file(filename=self._config.input_file)
        if input_data in (None, ''):
            raise JSIONException('Invalid input: \n %s' % input_data)
        self._input_data = input_data
        return input_data

    def __load_ion_data(self):
        ion_data = ion.loads(self._input_data, single_value=False)
        if isinstance(ion_data, list):
            self._ion_data = ion_data[0]   # TODO: what if len > 1?
        else:
            self._ion_data = ion_data
        return ion_data
    
    def __convert_ion_to_json(self):
        json_object = ion_to_json(self._ion_data)
        json_string = json.dumps(json_object, indent=' ')
        self._output_data = json_string
        return json_string

    def __prettify(self):
        pass  # TODO

    def __write_output(self):
        output_filename = self._config.output_file
        success = write_file(filename=output_filename, contents=self._output_data)
        if success:
            print('Converted data successfully written to %s' % output_filename)
            return
        print('Failed to write to %s' % output_filename)


    def __load_actions(self):
        self._tasks.append(self.__load_input_data_from_file)
        self._tasks.append(self.__load_ion_data)
        self._tasks.append(self.__convert_ion_to_json)
        self._tasks.append(self.__write_output)

        loaded_tasks = [t.__name__ for t in self._tasks]
        print("Tasks loaded:", loaded_tasks)
    
    def convert(self):
        print('Starting conversion: ION > JSON ...')
        try:
            self.__load_actions()
            for task in self._tasks:
                task()
            return True
        except Exception as identifier:
            traceback.print_exc()
            raise JSIONConversionError('ION to Json conversion failed. See logs above')




class JSIONConvertJsonToIon(JSIONConverterBase):
    def __init__(self, config):
        super().__init__(config)

    def convert(self):
        print('JSON to ION conversion not yet supported')



def converter_factory(cmdline_options: CommandLineOptions) -> JSIONConverterBase:
    config = cmdline_options  # ConverterConfiguration(cmdline_options)
    return JSIONConvertIonToJson(config) if not cmdline_options.reverse_conversion else JSIONConvertJsonToIon(config)
    


def main():
    print("Initialising cli converter...")
    cmdline_options = read_cmdline_options()
    print(cmdline_options)
    converter_instance = converter_factory(cmdline_options)
    converter_instance.convert()

if __name__ == "__main__":
    main()