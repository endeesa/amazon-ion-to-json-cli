# amazon-ion-json-examples


>  Simple Python project(s) with a collection of examples for converting ion  data to json format(and vice-versa).


## Dependency List

* awscli
* amazon
* pyion2json


>If you are using a python version > 3.3, you might run into issues with collections module import. Try this [solution](https://stackoverflow.com/questions/59636631/aws-cli-with-python-3-9-0a1-error-from-collections-import-mutablemapping)

## Getting started

 - The examples use docker to ensure portability
 - Each example has a dockerfile which can be executed as follows:
 
 ====================================================


* docker build -t \<custom-image-name\> .
```bash
# example


docker build -t ionJsonImg .
```
* docker run -d --name \<custom-container_name\> \<custom-image-name\>
```bash
# example
docker run -d --name ionJson ionJsonImg
```


* You can learn more about docker [here](https://www.docker.com/101-tutorial)