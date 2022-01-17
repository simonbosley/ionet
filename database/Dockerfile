FROM postgres:alpine3.15
LABEL maintainer="Simon Bosley simon.bosley@gmail.com"
ENV POSTGRES_PASSWORD mysecretpassword
ENV POSTGRES_DB ionetdb
COPY init.sql /docker-entrypoint-initdb.d/