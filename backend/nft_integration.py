```python
from web3 import Web3
from sqlalchemy.orm import Session
from models import NFTSchema

class NFTIntegration:
    def __init__(self, user, agent):
        self.user = user
        self.agent = agent
        self.web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    def create_nft(self, nft_data):
        nft = NFTSchema(**nft_data)
        session = Session()
        session.add(nft)
        session.commit()

        return nft

    def trade_nft(self, nft_id, buyer_address):
        nft = session.query(NFTSchema).get(nft_id)
        if not nft:
            raise Exception('NFT not found')

        if self.web3.eth.getBalance(self.user['address']) < nft['price']:
            raise Exception('Insufficient balance')

        self.web3.eth.sendTransaction({
            'from': self.user['address'],
            'to': buyer_address,
            'value': nft['price']
        })

        nft['owner'] = buyer_address
        session.commit()

        return nft

    def get_nft(self, nft_id):
        nft = session.query(NFTSchema).get(nft_id)
        if not nft:
            raise Exception('NFT not found')

        return nft
```