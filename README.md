# ionet
python ionet tools

if you're setting up a development environment for python, then you should use virtualenv.

Currently we activate the virtual environment from the ionet root project folder, then if you need the requirements of a particular server (such as the app_server), then use the requirements file from within that folder, i.e. something like:

python3 -m venv .venv
pip3 install -r app_server/requirements.txt

You can use multiple requirements files at once, if you want to set-up more than one servers requirements.

# app_server

This project connects to a postgres database using the psycopg2 python library. This library is part of the pip3 requirements.txt file.

psycopg2 library in the requirements, needs your system to have libpq already installed. On the macOs you can use homebrew to install just the lib or postgres client.

Example brew install:

brew doctor
brew upgrade
brewq install postgresql
