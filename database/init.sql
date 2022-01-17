CREATE TABLE domains (
    domain_id serial PRIMARY KEY,
    display_name varchar NOT NULL CHECK (display_name <> '')
);

CREATE TABLE hosts (
    host_id integer PRIMARY KEY,
    domain_id integer REFERENCES domains (domain_id)
);
