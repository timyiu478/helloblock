#!/usr/local/bin/python3

from web3 import Web3
from eth_abi import decode
import os
from dotenv import load_dotenv

ETHEREUM_NETWORK = os.getenv("ETHEREUM_NETWORK")

# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider(ETHEREUM_NETWORK))

# Function signature for SayHello()
function_signature = "SayHello()"

# Encode the function signature to get the function selector
function_selector = web3.keccak(text=function_signature)[:4].hex()

# Query the blockchain (replace example parameters)
data = web3.eth.call({
		'value': 0, 
		'gas': 2173600, 
		'maxFeePerGas': 40000000000, 
		'maxPriorityFeePerGas': 1000000000, 
		'to': '0xe35EabbF16226BEda3fde7Bffca24890FCcB24eC',
		'data': function_selector
		}) 

response = decode(['string'], data)[0]

print(response)
