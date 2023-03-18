import hashlib
import json
from time import time


# class to hold the data of each block
class Block:
    
    # create a constructor
    def __init__(self, index, transactions, timestamp, previous_hash):
        # contains the index of the block
        self.index = index

        self.transactions = transactions
        # creation time of the block
        self.timestamp = timestamp
        # contains/knows hash of the previous block
        self.previous_hash = previous_hash

        # contains its own hash number
        self.hash = self.calculate_hash()

    # function to calculate hash of given function
    def caculate_hash(self):
        
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


# class to add and validate the blocks in a chain
class Blockchain:
    pass


#print("all ok")

if __name__ == "__main__":
    
    pass
    # below code is to check the attributes of a block
    #print(Block.__dict__)