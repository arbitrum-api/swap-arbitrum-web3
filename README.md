# swap-arbitrum-web3
This Python script allows you to interact with the Arbitrum network via Web3 and a custom API. It supports transferring ERC-20 tokens, checking token balances, deploying smart contracts, and performing token swaps with decentralized exchanges like Uniswap.

Arbitrum API Documentation

This API allows interaction with the Arbitrum network for various functionalities such as token transfers, balance checks, contract deployments, and more. It integrates with the Arbitrum blockchain via HTTP requests and is designed for use with Web3 applications. Below are the key endpoints and methods available:
Base URL

https://arbitrum-api.co/api/v3

Endpoints
1. Transfer Tokens

    URL: /transfer

    Method: POST

    Description: Transfers ERC-20 tokens from one address to another.

    Request Parameters:
        from: Sender's address.
        to: Receiver's address.
        amount: Amount of tokens to transfer (must be a string).
        token: ERC-20 token address.
        private_key: Sender's private key (used for signing the transaction).

    Response:
        JSON response with transaction status and details.

2. Get Token Balance

    URL: /token-balance

    Method: GET

    Description: Fetches the balance of a specific ERC-20 token for a given address.

    Request Parameters:
        address: The address for which the token balance is being queried.
        token: The address of the ERC-20 token.

    Response:
        JSON response containing the balance in the specified token.

3. Deploy Smart Contract

    URL: /deploy-contract

    Method: POST

    Description: Deploys a new smart contract to the Arbitrum network.

    Request Parameters:
        from: Address deploying the contract.
        private_key: Private key of the deployer.
        bytecode: The compiled bytecode of the smart contract.

    Response:
        JSON response with the transaction status and deployment details.

Example Usage

Transfer Tokens
Make a POST request to /transfer with the required parameters to transfer tokens between two addresses.

Get Token Balance
Send a GET request to /token-balance with the address and token to get the balance of a specific token.

Deploy Smart Contract
Use the /deploy-contract endpoint to deploy your own smart contract, providing the bytecode and private key of the sender.
