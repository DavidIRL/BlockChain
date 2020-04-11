import datetime
from block import Block


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, block):
        # check if block is Block
        if not isinstance(block, Block):
            raise TypeError()
        if block == None:
            return
        
        if self.head == None:
            self.head = block
            self.tail = block
        # if chain only genesis block
        elif self.head.next == None:
            last_hash = self.head.hash
            # checking to be sure the head hash value
            # and prev_hash value of current block match
            if last_hash != block.previous_hash:
                raise ValueError('Previous hash value in block does not make the hash value from the previous block')
            head = self.head
            head.next = block
            block.prev = head
            # set tail to new block for faster adding
            self.tail = block
        else:
            last_hash = self.tail.hash
            # checking to be sure the current tail hash
            # and prev_hash value of current block match
            if last_hash != block.previous_hash:
                raise ValueError('Previous hash value in block does not make the hash value from the previous block')
            # chain is established
            tail = self.tail
            new_tail = block
            # add block to chain
            tail.next = new_tail
            # make current tail prev to new_tail
            new_tail.prev = tail
            # make new_tail the proper tail
            self.tail = new_tail

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        return str([value for value in self])



if __name__ == '__main__':

    genesis = Block.create_genesis()
    print(genesis)
    print('\n')

    new_data = 'an irrelevant string of characters to be used as data for encoding our new block'
    b1 = Block(datetime.datetime.now(), new_data, genesis.hash)
    print(b1)
    print('\n')

    # a new block w/ same data to show hash is unique per block
    newer_data = 'an irrelevant string of characters to be used as data for encoding our new block'
    b2 = Block(datetime.datetime.now(), newer_data, b1.hash)
    print(b2)
    print('\n')

    blockchain = BlockChain()

    blockchain.add_block(genesis)
    blockchain.add_block(b1)
    blockchain.add_block(b2)
    print('\n')
    print(blockchain)
