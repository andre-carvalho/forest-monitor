# Forest Monitor BackEnd Server

## Publishing on DockerHub

To publish a new image to DockerHub, that the application version at forest_monitor/setup.py was increased.

### Building with Docker

To build and push an image to Docker Hub, just run:

$ Docker/docker-build.sh

## Running locally

### Dependencies

To run the application locally, be sure too to install the following dependencies:

We remommends that you use the virtual environment of python. The following steps assums that you use a Linux O.S. as development environment system.

Command steps:
```sh
# Go to the base directory of workspace project and runs
python3 -m venv venv
source venv/bin/activate
# we assums that your anvironment have the libraries that python dependencies need.
pip install -r docker-base/requirements.txt
```


.. code-block:: shell
$ apt-get update 
$ apt-get install -y build-essential libpq-dev python3-pip git
$ pip3 install -r requirements.txt

### Running

To run the application:

.. code-block:: shell
$ python3 Docker/manage.py run

