# Forex Trading Platform API

Description: RESTful API server that exposes a set of endpoints to simulate a trading platform

## Usage
  - The app can be run on a computer or using Docker.

## Computer
  - Install requirements from requirements.txt and requirements_test.txt
  - To start server in the root directory use the command below

  ```bash
  $ uvicorn app.main:app --port 8080
  ```
  - To run test suits use the command below in the test/ directory

  ```bash
  $ pytest
  ```

## Docker
**Install Docker**
  - The API and Test can be installed in seperate Docker container. 
    Due to the use of f-strings, this must be run with python 3.6+. 
    The Docker image is based on python:3.9-slim

# Building Docker Images

**API Docker**
To build the API Docker image, run the following command in the root directory:

  ```bash
  $ docker build -t [fastapi_container_name] -f Dockerfile.api .
  ```
NB: replace fastapi_container_name with desire name for container

To run the API Docker image, run the following command in the root directory:
  ```bash
  $ docker run -p 8080:8080 [fastapi_container_name]
  ```
**Test Docker**
To build the test Docker image, run the following command in the root directory:

  ```bash
  $ docker build -t [test_container_name] -f Dockerfile.test .
  ```
NB: replace test_container_name with desire name for container

To run the test Docker image, run the following command in the root directory:

  ```bash
  $ docker run --network host  [test_container_name]
  ```

Note the html for the test can be foun in "/tmp/report.html" in the test container and you can move it to your computer using 

  ```bash
  $ docker cp <container_id>:/tmp/report.html /path/on/host/report.html
  ```

## Swagger Documentation
After starting the server this can be found at "http://localhost:8000/docs".