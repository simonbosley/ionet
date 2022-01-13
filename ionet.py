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
        return f"\n\t\t\t\tComponent {self.id}: '{self.domain.name}'"

class Io:

    # Typedefs for params.
    Components = list[Component]

    def __init__(self, host_id: int, subhost_id: int, slot_id: int, id: int, domain: Domain, components: Components):
        self.host_id = host_id
        self.subhost_id = subhost_id
        self.slot_id = slot_id
        self.id = id
        self.domain = domain

    def __str__(self):
        return f"\n\t\t\tIo {self.id}: '{self.domain.name}'"

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

        # Get a collection of indexes as strings.
        indexes_as_string_collection = [str(index) for index in self.io_collection]

        # Join all the index strings into one big line separated string.
        indexes_as_string = "".join(indexes_as_string_collection)

        # Put this slot before the indexes.
        return f"\n\t\tSlot {self.id}: '{self.domain.name}'{indexes_as_string}"

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

