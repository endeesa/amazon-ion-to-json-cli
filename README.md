# amazon-ion-json-examples


>  Simple Python project(s) with a collection of examples for converting ion  data to json format(and vice-versa). Recommended python version **3.6x**


## Dependency List

* awscli
* amazon
* pyion2json


>If you are using a python version > 3.3, you might run into issues with collections module import. Try this 

## Getting started

 - The examples use docker to ensure portability
 - Each example has a dockerfile which can be executed as follows:
 
 ====================================================


* docker build -t \<custom-image-name\> .
```bash
# example
docker build -t ion_json_img .
```
* docker run --name \<custom-container_name\> \<custom-image-name\>
```bash
# example
docker run --name ion_json ion_json_img
```


* You can learn more about docker [here](https://www.docker.com/101-tutorial)

<hr/>

## TroubleShooting

i. **cannot import name 'MutableMapping' from 'collections'**


*  [Stack overflow solution](https://stackoverflow.com/questions/59636631/aws-cli-with-python-3-9-0a1-error-from-collections-import-mutablemapping)