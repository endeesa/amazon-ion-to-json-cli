class JSIONException(Exception):
    pass


class JSIONConversionError(Exception):
    pass


def read_file(filename, mode='r'):
    with open(filename, mode) as file_object:
        contents = file_object.read()
        return contents



def write_file(filename, contents, mode='w'):
    with open(filename, mode) as file_object:
        contents = file_object.write(contents)
        return True