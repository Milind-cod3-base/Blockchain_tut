import hashlib
import json
from time import time


# class to hold the data of each block
class Block:
    
    # create a constructor
    def __init__(self, index, timestamp, previous_hash, image_data=None):
        # contains the index of the block
        self.index = index


        self.size = len(json.dumps(self.__dict__, sort_keys=True).encode('utf-8'))

        # stores the image/bogines
        self.image_data = image_data
        
        #self.transactions = transactions


        # creation time of the block
        self.timestamp = timestamp
        # contains/knows hash of the previous block
        self.previous_hash = previous_hash

        # contains its own hash number
        self.hash = self.calculate_hash()

    # function to calculate hash of given function
    def calculate_hash(self):

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
        # create a instance of a block class
        # index=0, no transaction to include in genesis block
        return Block(0, [], time(), "0")
    
    # get the latest/last block
    def get_latest_block(self):
        return self.chain[-1]
    
    # add a new block into the chain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

        
    
    # check the validity/corruption of chain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            # i starts from 1 as we dont need to check genesis block
            current_block = self.chain[i]

            previous_block = self.chain[i-1]

            # check if the hash has changed of the block
            if current_block.hash == current_block.calculate_hash():
                b = "valid"
                return b
                #print(b)
            
            # double verifying the hash of previous block
            # by checking hash stored in current block and 
            # hash stored in previous block 
            if current_block.previous_hash == previous_block.hash:
                a = "valid"
                return a
                #print(a)


#print("all ok")

if __name__ == "__main__":
    
    # create 1st chain
    blockchain1 = Blockchain()

    # add first block
    b1 = Block(1, time(),"")

    blockchain1.add_block(b1)


    # add second block
    b2 = Block(2, time(),"")

    blockchain1.add_block(b2)


    # below code is to check the attributes of a block
    #print(Block.__dict__)

    #blockchain1.is_chain_valid
    
    # get the details of desired
    print(blockchain1.chain[0].__dict__)

    print(blockchain1.chain[1].__dict__)

    print(blockchain1.chain[2].__dict__)