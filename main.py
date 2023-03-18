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

    # blockchain constructor
    def __init__(self):

        # list which contains genesis block as the first element
        self.chain = [self.create_genesis_block()]

    # create the genesis block to store it in the chain
    def create_genesis_block(self):
        pass
    
    # get the latest/last block
    def get_latest_block(self):
        pass
    
    # add a new block into the chain
    def add_block(self):
        pass
    
    # check the validity/corruption of chain
    def is_chain_valid(self):
        pass



#print("all ok")

if __name__ == "__main__":
    
    pass
    # below code is to check the attributes of a block
    #print(Block.__dict__)