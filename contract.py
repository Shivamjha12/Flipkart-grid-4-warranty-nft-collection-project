from dotenv import load_dotenv
from thirdweb import ThirdwebSDK
from web3 import Web3
from eth_account import Account
import os
from ecommerece_main.nft_collection import PRIVATE_KEY

load_dotenv()

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
