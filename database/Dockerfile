FROM postgres:alpine3.15
MAINTAINER "Simon Bosley"
COPY TABLES.sql /home/database/
COPY install_db.sh /home/database/
WORKDIR /home/database
CMD sh ./install_db.sh