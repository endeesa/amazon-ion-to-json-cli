FROM python:3.6-slim

# Configure working directory i.e. The root dir that docker will run from
WORKDIR /usr/src/app

RUN pip install --upgrade pip

# Copy requirements file from host machine to docker container
COPY requirements.txt ./

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code to the working directory
COPY . .

# First command to execute when the docker image is run
CMD [ "python", "./example1.py" ]