# Get a slim python image.
FROM python:3.8.2-alpine
LABEL maintainer="Simon Bosley simon.bosley@gmail.com"

# Create a working directory in the container to copy files into.
WORKDIR /app

# Copy the python pip3 freeze generated requirements file into the container working directory
COPY requirements.txt requirements.txt

# Copy the flask app into the working directory.
COPY app.py app.py

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
# For python3 you need to add python3-dev *please upvote the comment
# of @its30 below if you use this*
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

# Install the requirements using pip3 (includes psycopg2).
RUN pip3 install -r requirements.txt

# Delete build dependencies
RUN apk del .build-deps

# When we run the container this is the command that will be executed. Launches the Flask server.
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]