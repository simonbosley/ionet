CREATE DATABASE ionet;

CREATE TABLE domain {
    domain_id integer PRIMARY KEY DEFAULT nextval('serial'),
    display_name varchar NOT NULL CHECK (name <> '')
}

CREATE TABLE host (
    host_id integer PRIMARY KEY
    domain_id integer FOREIGN KEY
)