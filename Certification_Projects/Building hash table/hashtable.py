

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,key=str):
        letters = list(key)
        unicodes = list(ord(letter)for letter in letters)

        return sum(unicodes)

    def add(self,key,value):
        hash_value = self.hash(key)

        if hash_value in self.collection:
            self.collection[hash_value][key] = value

        else:
            self.collection[hash_value] = {key:value}

    def remove(self,key):
        hash_value = self.hash(key)

        if hash_value in self.collection:
          if key in self.collection[hash_value]:
            if len(self.collection[hash_value])> 1:
              del self.collection[hash_value][key]
            else:
              del self.collection[hash_value]
          else:
            pass

    def lookup(self,key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            return self.collection[hash_value].get(key,None)
        else:
            return None