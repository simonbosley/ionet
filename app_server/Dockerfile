# Get a slim python image.
FROM python:3.8-slim-buster
LABEL maintainer="Simon Bosley simon.bosley@gmail.com"

# Create a working directory in the container to copy files into.
WORKDIR /app

# Copy the python pip3 freeze generated requirements file into the container working directory
COPY requirements.txt requirements.txt

# Copy the flask app into the working directory.
COPY app.py app.py

# Install the requirements using pip3.
RUN pip3 install -r requirements.txt

# When we run the container this is the command that will be executed. Launches the Flask server.
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]