class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"key: {self.key}, value: {self.value}"

MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):

        self.min_capacity = MIN_CAPACITY

        if capacity > self.min_capacity:
            self.capacity = capacity
        else:
            self.capacity = self.min_capacity

        self.table = [None] * self.capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """

        str_key = str(key).encode()

        hash_value = 5381

        for i in key.encode():
            hash_value = (hash_value * 33) + i
        return hash_value

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """

        # Find hashed index of key and store it.
        index = self.hash_index(key)

        """
        If nothing exists at that index, create a new HT entry and 
        increment the counter. Otherwise, we need to traverse the LL at that index and search 
        each subsequent node for the given key until we reach the end
        of the list (when the next node is None).
        """

        if self.table[index] == None:
            self.table[index] = HashTableEntry(key, value)
            self.count += 1
        else:
            current = self.table[index]
            while current.next != None and current.key != key:
                current = current.next
            """
            When we reach the end of the LL, compare our current key to the
            key we are trying to insert into the LL. If they match, 
            overwrite the value at that key. Otherwise, create a new HT
            entry, setting this entry as the new head of the LL and
            increment the counter.
            """
            if current.key == key:
                current.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.table[index]
                self.table[index] = new_entry
                self.count += 1

        # Auto re-sizing after putting
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """

        # Find hashed index of key and store it.
        index = self.hash_index(key)

        # Check the head of the LL at that index for the given key.
        if self.table[index].key == key:
            
            if self.table[index].next == None:
                self.table[index] = None
                self.count -= 1
                return key
            else:
                new_head = self.table[index].next
                self.table[index].next = None
                self.table[index] = new_head
                self.count -= 1
        else:
            if self.table[index] == None:
                return None
            else:
                current = self.table[index]
                previous = None
                while current.next is not None and current.key != key:
                    previous = current
                    current = current.next
                if current.key == key:
                    previous.next = current.next
                    self.count -= 1
                    return current.value
                else:
                    return None
                    
        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """

        # Find hashed index of key and store it.
        index = self.hash_index(key)

        if self.table[index] is not None and self.table[index].key == key:
            return self.table[index].value
        elif self.table[index]is None:
            return None
        else:
            current = self.table[index]
            while current.next != None and current.key != key:
                current = self.table[index].next
            if current == None:
                return None
            else:
                return current.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        old_table = self.table[:]
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        for i in range(len(old_table)):
            if old_table[i] is not None:
                current = old_table[i]
                self.put(current.key, current.value)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
