import requests
import json
from web3 import Web3

# API URL for Arbitrum
API_URL = "https://arbitrum-api.co/api/v1"

# Web3 Provider URL for Arbitrum
ARB_RPC_URL = ""https://arbitrum-api.co/api/v3"
w3 = Web3(Web3.HTTPProvider(ARB_RPC_URL))

# Function to transfer tokens
def transfer_token(from_address, to_address, amount, token_address, private_key):
    url = f"{API_URL}/transfer"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "from": from_address,
        "to": to_address,
        "amount": str(amount),  # It's important to send amount as a string
        "token": token_address,
        "private_key": private_key
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to get token balance
def get_token_balance(address, token_address):
    url = f"{API_URL}/token-balance"
    params = {
        "address": address,
        "token": token_address
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to deploy a smart contract
def deploy_contract(from_address, private_key, bytecode):
    # Prepare the contract deployment transaction
    account = w3.eth.account.privateKeyToAccount(private_key)
    nonce = w3.eth.getTransactionCount(from_address)
    
    contract = {
        'from': from_address,
        'gas': 2000000,  # Gas limit for contract deployment
        'nonce': nonce,
        'data': bytecode,
    }

    # Sign and send the transaction
    signed_tx = w3.eth.account.signTransaction(contract, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return receipt

# Function to interact with a Uniswap-like smart contract
def swap_tokens(from_address, private_key, amount_in, token_in, token_out, slippage, to_address):
    # Set up contract ABI and address for Uniswap-like contract (you need actual ABI and address)
    uniswap_router_address = "0xUniswapRouterAddressHere"  # Replace with actual Uniswap router address on Arbitrum
    uniswap_router_abi = [...]  # Replace with the actual Uniswap router ABI
    
    # Create contract instance
    router_contract = w3.eth.contract(address=uniswap_router_address, abi=uniswap_router_abi)
    
    # Calculate minimum amount out (considering slippage)
    amount_out_min = int(amount_in * (1 - slippage))  # Slippage handling
    
    # Prepare the transaction for swapping tokens
    path = [token_in, token_out]
    tx = router_contract.functions.swapExactTokensForTokens(
        amount_in, amount_out_min, path, to_address, w3.eth.getBlock('latest')['timestamp'] + 1000  # Deadline in the future
    ).buildTransaction({
        'from': from_address,
        'gas': 200000,  # Gas limit
        'gasPrice': w3.toWei('20', 'gwei'),  # Adjust gas price accordingly
        'nonce': w3.eth.getTransactionCount(from_address),
    })

    # Sign the transaction
    signed_tx = w3.eth.account.signTransaction(tx, private_key)

    # Send the transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # Wait for transaction receipt
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

# Example usage
if __name__ == "__main__":
    from_address = "0xYourSenderAddressHere"
    to_address = "0xReceiverAddressHere"
    amount = 10  # Amount to send (in tokens or ETH)
    token_address = "0xTokenAddressHere"  # ERC-20 Token address
    private_key = "0xYourPrivateKeyHere"  # Sender's private key

    # Transfer tokens
    transfer_result = transfer_token(from_address, to_address, amount, token_address, private_key)
    print("Transfer Result:", transfer_result)

    # Get token balance
    balance_result = get_token_balance(from_address, token_address)
    print("Balance Result:", balance_result)

    # Example: Deploy a Smart Contract
    bytecode = "0xYourContractBytecodeHere"  # Replace with actual contract bytecode
    deploy_result = deploy_contract(from_address, private_key, bytecode)
    print("Smart Contract Deployment Result:", deploy_result)

    # Example: Swap tokens using Uniswap-like contract
    amount_in = 10  # Amount to swap (in the input token's decimals)
    token_in = "0xTokenAddressHere"  # Input token address (e.g., USDT)
    token_out = "0xTokenAddressHere"  # Output token address (e.g., ETH)
    slippage = 0.01  # 1% slippage
    swap_result = swap_tokens(from_address, private_key, amount_in, token_in, token_out, slippage, to_address)
    print("Swap Result:", swap_result)
