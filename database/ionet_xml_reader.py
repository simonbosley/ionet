from sys import argv
from os.path import exists

import xml.etree.ElementTree as ET
from ionet import Domain, Component, Io, Slot, SubHost, Host

if __name__ != "__main__":
    print("ERROR: Please run as a script not a module.")
    exit(0)

# Check that the command line params are as expected.
num_cmd_args = len(argv)
if num_cmd_args < 2:
    print("Please pass command line param for xml file to import.")
    exit(0)
elif num_cmd_args > 3:
    print("Too many command line params, ignoring anything after xml file.")

# Get the path to the xml file that we are to import.
xml_file_path = argv[1]

if not exists(xml_file_path):
    print(f"The xml file at path: {xml_file_path} does not exist.")
    exit(0)

# Create the required namespaces of the IONet snapshot.
ns_ionet = "{http://schemas.datacontract.org/2004/07/SSL.IONet}"
ns_domains = "{http://schemas.datacontract.org/2004/07/SSL.IONet.Domains}"
ns_arrays = "{http://schemas.microsoft.com/2003/10/Serialization/Arrays}"

# Parse the XML specified by the user.
tree = ET.parse(xml_file_path)

ionet_snapshot_root = tree.getroot()

print(ionet_snapshot_root)

# Get the NetTable from the IONet snapshot.
net_table_element = ionet_snapshot_root.find(f"{ns_ionet}NetTable")

# Get the Domains from the NetTable.
domains_element = net_table_element.find(f"{ns_ionet}Domains")

# Get all the Hosts from Domains.
hosts_element = domains_element.find(f"{ns_domains}Hosts")

# Create some host objects to fill in.
hosts = []

# Loop the hosts and print some details from each.
host_limit = 1
num_hosts_processed = 0

for host_element in hosts_element:
    # Check if we've passed an imposed limit on how many hosts to import.
    if num_hosts_processed >= host_limit:
        print(f"Processed {num_hosts_processed} and reached imposed limit of {host_limit}, stopping now.")
        break

    # All the hosts data is stored in one element called 'Value'
    host_value_element = host_element.find(f"{ns_arrays}Value")

    # Get the host domain Index.
    host_value_index_element = host_value_element.find(f"{ns_domains}Index")
    host_id = host_value_index_element.text
    
    # Get the name.
    host_value_name_element = host_value_element.find(f"{ns_domains}Name")
    host_name = host_value_name_element.text
    
    # Now go through the SubHosts in the Host.
    subhosts = []
    subhost_elements = host_value_element.find(f"{ns_domains}SubHosts")

    for subhost_element in subhost_elements:
        # All the hosts data is stored in one element called 'Value'
        subhost_value_element = subhost_element.find(f"{ns_arrays}Value")

        # Get the host domain Index.
        subhost_value_index_element = subhost_value_element.find(f"{ns_domains}Index")
        subhost_id = subhost_value_index_element.text
        
        # Get the name.
        subhost_value_name_element = subhost_value_element.find(f"{ns_domains}Name")
        subhost_name = subhost_value_name_element.text
        
        # Now go through the Slots in the SubHost.
        slots = []
        slots_elements = subhost_value_element.find(f"{ns_domains}Slots")

        for slot_element in slots_elements:
            # All the hosts data is stored in one element called 'Value'
            slot_value_element = slot_element.find(f"{ns_arrays}Value")

            # Get the slot index.
            slot_value_index_element = slot_value_element.find(f"{ns_domains}Index")
            slot_id = slot_value_index_element.text
            
            # Get the slot name.
            slot_value_name_element = slot_value_element.find(f"{ns_domains}Name")
            slot_name = slot_value_name_element.text
            
            # Now go through the Io collection in the Slot.
            io_collection = []
            io_elements = slot_value_element.find(f"{ns_domains}IOItems")

            if io_elements == None:
                continue

            for io_element in io_elements:
                # All the hosts data is stored in one element called 'Value'
                io_value_element = io_element.find(f"{ns_arrays}Value")

                # Get the io index.
                io_value_index_element = io_value_element.find(f"{ns_domains}Index")
                io_id = io_value_index_element.text
                
                # Get the io name.
                io_value_name_element = io_value_element.find(f"{ns_domains}Name")
                io_name = io_value_name_element.text

                # Now go through the components in the Io collection. TODO
                components = [Component(host_id, subhost_id, slot_id, io_id, 1, Domain("1"))]

                # Create a Io object, pass in the domain and child components.
                io_domain = Domain(io_name)
                io = Io(host_id, subhost_id, slot_id, io_id, io_domain, components)
                io_collection.append(io)
            
            # Create a Slot object, pass in the domain and child Indexes.
            slot_domain = Domain(slot_name)
            slot = Slot(host_id, subhost_id, slot_id, slot_domain, io_collection)
            slots.append(slot)

        # Create a SubHost object, pass in the domain and child Slots.
        subhost_domain = Domain(subhost_name)
        subhost = SubHost(host_id, subhost_id, subhost_domain, slots)
        subhosts.append(subhost)


    # Create a Host object, pass in the domain and child SubHosts.
    host_domain = Domain(host_name)
    host = Host(host_id, host_domain, subhosts)
    hosts.append(host)

    num_hosts_processed += 1


# We've finished with the XML document, let's print the info that we collected.
for host in hosts:
    print(host)
    print()
