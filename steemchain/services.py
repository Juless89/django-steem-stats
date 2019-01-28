from steem.blockchain import Blockchain


# retrieve current blockchain statistics
def blockchain_data():
    blockchain = Blockchain()
    return blockchain.info()