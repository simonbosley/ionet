# Get the postgres alpine3.15 image and create the IONet db and launch init.sql script. 
FROM postgres:alpine3.15
LABEL maintainer="Simon Bosley simon.bosley@gmail.com"
ENV POSTGRES_PASSWORD mysecretpassword
ENV POSTGRES_DB ionetdb
COPY init.sql /docker-entrypoint-initdb.d/

# Update the apk library and install python3. Print the version installed...
RUN apk add --update python3 py3-pip