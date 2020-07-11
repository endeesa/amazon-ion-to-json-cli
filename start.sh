#!/bin/bash

# TODO: Fail $1 is empty

cd $1
sudo docker build -t ion_json_img .
sudo docker run -d --name ion_json ion_json_img