import hashlib
import datetime


class Block:
    
    def __init__(self, timestamp, data , previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None
        self.next = None

    def calc_hash(self):
        # combine all data to be encoded
        encode_info = (str(self.timestamp) +
                      str(self.data) +
                      str(self.previous_hash)).encode('utf-8')
        # hash all block data(s)
        sha = hashlib.sha256(encode_info).hexdigest().encode('utf-8')
        block_hash = hashlib.sha256(sha).hexdigest()

        return block_hash

    @staticmethod
    def create_genesis():
        return Block(datetime.datetime.now(), 'I am the genesis block!', '0')

    def __iter__(self):
        node = self
        while node:
            yield 'my timestamp is: {}'.format(node.timestamp)
            yield 'my data is: {}'.format(node.data)
            yield 'my previous hash is: {}'.format(node.previous_hash)
            yield 'MY hash is: {}'.format(node.hash)
            break

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