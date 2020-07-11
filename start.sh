#!/bin/bash

# TODO: 

cd $1
sudo docker build -t ion_json_img .
sudo docker run --name ion_json ion_json_img