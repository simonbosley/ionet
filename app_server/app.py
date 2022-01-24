# Import the Flask server classes.
from flask import Flask
from flask import jsonify

import psycopg2

conn = psycopg2.connect(dbname="ionetdb", user="postgres", password="mysecretpassword", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("INSERT into domains (display_name) VALUES ('Local Host')")

cur.execute("SELECT * FROM domains")

records = cur.fetchall()

cur.close()
conn.close()

# A class to store hosts.
class Host:
    def __init__(self, id, name):
        self.__id__ = id
        self.__name__ = name
    
    def get_id(self):
        return self.__id__ 

    def get_name(self):
        return self.__name__
    
    def get_dict(self):
        return {'id': self.__id__, 'name': self.__name__}

# Create some hosts test data.
hosts_by_host_id = {
        1: Host(1, "Local Console"),
        2: Host(2, "Logicals")
    }

# Create the Flask server
app = Flask(__name__)

# Useful test page.
@app.route("/api/v1/testdb/", methods={'GET'})
def testdb():
    htmlPage = "<h1>Testing the database connection.</h1>"
    htmlPage += f"<p>{records}</p>"
    return htmlPage

# Create our home page with useful links.
@app.route("/api/v1/", methods={'GET'})
def rootPage():
    htmlPage = "<h1>IoNet API version 1.</h1>"
    htmlPage += "<a href='/api/v1/hosts/'>Hosts"
    return htmlPage


@app.route("/api/v1/hosts/", methods={'GET'})
def hosts():
    '''
    Return this page when the user doesn't specify an individual host.
    This will return all of the hosts.
    '''

    # A list of each host represented as a dictionary.
    hostsAsDicts = []

    for host in hosts_by_host_id.values():
        # Add the current host's data fields as a dictionary to the list.
        hostsAsDicts.append(host.get_dict())

    # Wrap all the hosts in one outer key/value called 'Hosts'
    allHosts = [{'Hosts': hostsAsDicts}]

    # Convert to json and return.
    return jsonify(allHosts)

@app.route("/api/v1/hosts/<int:host_id>/", methods={'GET'})
def host(host_id):
    '''
    This page will return the information about the host specified with host_id parameter.
    '''
    
    if host_id in hosts_by_host_id:
        # Convert host to json and return.
        return jsonify(hosts_by_host_id[host_id].get_dict())
    else:
        # Could not find host, display error and return http status error code 404.
        return f"<h1>Error</h1><p>Host {host_id} not found</p>", 404