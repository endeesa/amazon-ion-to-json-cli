import json
import amazon.ion.simpleion as ion
from pyion2json import ion_to_json


# Replace filename with your own ion filename
def read_file(filename='ion_file.txt'):
    with open(filename, 'r') as file_object:
        contents = file_object.read()
        return contents


ion_data = u'%s' % read_file()
ion_data = ion.loads(ion_data, single_value=False)
pretty_ion_data = ion.dumps(ion_data, binary=False, indent='  ')
# print("Pretty ION: \n", pretty)

print("\n\n==================================================================\n\n")
json_doc = ion_to_json(ion_data[0])
print("Pretty JSON: \n")
print(json.dumps(json_doc, indent=' '))
