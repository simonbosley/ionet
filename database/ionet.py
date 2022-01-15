import sys

if __name__ == "__main__":
    print(f"Error: Running {sys.argv[0]} as a script, it's a module.")

# Create the classes that we'll use.
class Domain:
    def __init__(self, name):
        self.name = name

class Component:
    def __init__(self, host_id: int, subhost_id: int, slot_id: int, io_id: int, id: int, domain: Domain):
        self.host_id = host_id
        self.subhost_id = subhost_id
        self.slot_id = slot_id
        self.io_id = io_id
        self.id = id
        self.domain = domain

    def __str__(self):
        return f"{self.domain.name}"

class Io:

    # Typedefs for params.
    Components = list[Component]

    def __init__(self, host_id: int, subhost_id: int, slot_id: int, id: int, domain: Domain, components: Components):
        self.__host_id__ = host_id
        self.__subhost_id__ = subhost_id
        self.__slot_id__ = slot_id
        self.__id__ = id
        self.__domain__ = domain
        self.__components__ = components

    def get_components(self) -> Components:
        return self.__components__

    def __str__(self):
        return f"{self.__id__}"

class Slot:

    # Typedefs for params.
    IoCollection = list[Io]

    def __init__(self, host_id: int, subhost_id: int, id: int, domain: Domain, io_collection: IoCollection):
        self.host_id = host_id
        self.subhost_id = subhost_id
        self.id = id
        self.domain = domain
        self.io_collection = io_collection

    def __str__(self):

        # Get the first and last Io to display as a range, as they're too many to print.
        io_range_string = ""
        component_range_string = ""

        io_length = len(self.io_collection)

        if io_length > 0:

            # Get the first io in the range.
            first_io = self.io_collection[0]

            if io_length == 1:
                io_range_string = f"\n\t\t\tIo: {first_io}"
            else:
                last_io = self.io_collection[io_length - 1]
                io_range_string = f"\n\t\t\tIo Range: {first_io} - {last_io}"

            # We have at-least one Io item, get the components from that one as an example for the rest (usually they're all the same in each Io).
            components = first_io.get_components()
            components_length = len(components)
            
            # Check whether there is one component, a range of components, or ignore if none.
            if components_length > 0:
                first_component = components[0]

                if components_length == 1:
                    component_range_string = f"\n\t\t\t\tComponent: {first_component}"
                else:
                    last_component = components[components_length - 1]
                    component_range_string = f"\n\t\t\t\tComponents: {first_component} - {last_component}"

        # Put this slot before the io range and component range.
        return f"\n\t\tSlot {self.id}: '{self.domain.name}'{io_range_string}{component_range_string}"

class SubHost:

    # Typedefs for params.
    Slots = list[Slot]

    def __init__(self, host_id: int, id: int, domain: Domain, slots: Slots):
        self.host_id = host_id
        self.id = id
        self.domain = domain
        self.slots = slots
    
    def __str__(self):
        # Get a collection of slots as strings.
        slots_as_string_collection = [str(slot) for slot in self.slots]

        # Join all the slots strings into one big line separated string.
        slots_as_string = "".join(slots_as_string_collection)

        # Put this subhost before the slots.
        return f"\n\tSubHost {self.id}: '{self.domain.name}'{slots_as_string}"

class Host:

    # Typedefs for params.
    SubHosts = list[SubHost]
    
    def __init__(self, id: int, domain: Domain, subhosts: SubHosts):
        self.id = id
        self.domain = domain
        self.subhosts = subhosts
    
    def __str__(self):
        # Get a collection of subhosts as strings.
        subhosts_as_string_collection = [str(subhost) for subhost in self.subhosts]
        
        # Join all the subhost strings into one big line separated string.
        subhosts_as_string= "".join(subhosts_as_string_collection)

        # Put this host before the sub hosts.
        return f"Host {self.id}: '{self.domain.name}'{subhosts_as_string}"

