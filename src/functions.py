import hashlib, json, requests
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


def register_node(self, adress):
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(adress)
        self.nodes.add(parsed_url.netloc)
    
    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeros, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print('Last block: {}'.format(last_block))
            print('Block: {}'.format(block))
            print("\n----------\n")

            # check if that block's hash is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # check if that proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """
        neighbours = self.nodes
        new_chain = None

        # we're only looking for chains longer than ours
        max_length = len(self.chain)

        # grab and verifythe chains from all nodes in our network
        for node in neighbours:
            response = requests.get('http://{}/chain'.format(node))

            if response.status_code == 200:
                print(response)
                # length = response.json()['length']
                # chain = response.json()['chain']

                # check if the length is longer 'n the chain is valid
                # if length > max_length and self.valid_chain(chain):
                #     max_length = length
                #     new_chain = chain

        # replace our chain if we discover a new valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False