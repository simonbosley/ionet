# Get the postgres alpine3.15 image and create the IONet db and launch init.sql script. 
FROM postgres:alpine3.15
LABEL maintainer="Simon Bosley simon.bosley@gmail.com"

# Set the postgres env vars for the user password and the database name created.
ENV POSTGRES_PASSWORD mysecretpassword
ENV POSTGRES_DB ionetdb

# Copy the ionet database table creation script into the docker entry point that'll be run during building the image.
COPY init.sql /docker-entrypoint-initdb.d/