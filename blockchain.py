from itertools import chain
import json
import hashlib
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Blockchain:
    def __init__(self):
        #block store in here
        self.chain = [] 
        #hash store in here
        self.blockhash = [0] 
        #genesis block
        self.create_block(tx = "start", previous_hash = "0")

    #block created here
    def create_block(self, tx, previous_hash):
        #block structure
        block={
            "index":len(self.chain),
            "tx":tx,
            "previous_hash":previous_hash,
        }
        self.chain.append(block)
        encoded = json.dumps(block, sort_keys=True).encode()
        self.blockhash.append(hashlib.sha256(encoded).hexdigest())
        return block
        
    #block hashing
    def hash(self, block):
        #sort data in blocks and hash it using sha256
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    #chain validate here
    def is_chain_valid(self,chain,count1,count2):
        
        while count2 < len(chain):
            head = chain[count1]
            tail = chain[count2]
            if tail["previous_hash"] == self.hash(head):
                count1 += 1
                count2 += 1
                
            else:
                print()
                print(Fore.RED + "Block number %d have been edit" %count1)
                return False

        return True

    #display chosen block data
    def display_tx(self,chain,num):
        block = chain[num]
        print("\nTransaction of Block number %d is \"%s\"" %(num, block["tx"]))
        return True

    #edit block
    def block_edit(self, chain, index, data):
        block = chain[index]["tx"] = data

    #display all chains
    def display_chains (self, chain):
        chainl = len(chain)
        count = 0
        while count < chainl:
            print()
            print("Block index %d = " %count, end="")
            print(chain[count], "block hash = ", self.hash(chain[count]), end="\n")
            count += 1


#use blockchain
blockchain = Blockchain()

control = 1

while control == 1:
    print()
    mode = int(input("Select Mode:\n1.Input mode\n2.Display mode\n3.Chain validate\n4.Edit Mode\n5.Display Chains\n6.Stop program\nAnswer = "))
    
    #input mode
    input_mode = "yes"
    if mode == 1:
        chain = blockchain.chain
        if len(chain) == 1:
            previoushash = blockchain.blockhash[-1]
            print()
            tx = input("Enter match result: ")
            blockchain.create_block(tx, previoushash)
            input_mode = input("\nAdd more(yes/no)?\nAnswer = ")
        while input_mode.lower() == "yes":
            chain = blockchain.chain
            if blockchain.is_chain_valid(chain, count1 = 0, count2 = 1):
                print(Fore.GREEN + "\nSystem message: Chain still valid, continue process")
                print()
                previoushash = blockchain.blockhash[-1]
                tx = input("Enter match result: ")
                blockchain.create_block(tx, previoushash)
            else :
                print(Fore.RED + "System message: Chain isn't valid, stop process")
            input_mode = input("\nAdd more(yes/no)?\nAnswer = ")
   
    #display mode
    elif mode == 2:
        display_mode = "yes"
        while display_mode.lower() == "yes":
            chain = blockchain.chain
            display_block = int(input("\nEnter Block index: "))
            blockchain.display_tx(chain, display_block)
            display_mode = input("\nDo you want to see more transaction(yes/no)?\nAnswer = ")
   
    #chain validate
    elif mode == 3:
        chain = blockchain.chain
        if len(chain) == 1:
            print()
            print(Fore.RED + "System message: Chain still empty, go add somthing to to the chain")
        else:
            if blockchain.is_chain_valid(chain, count1 = 0, count2 = 1):
                print()
                print(Fore.GREEN + "System message: Chain still valid")
    
    #to edit block transaction
    elif mode == 4:
        chain = blockchain.chain
        print()
        index = int(input("Which block you want to edit?: "))
        data = input("New Result: ")
        blockchain.block_edit(chain, index, data)

    #display all chains
    elif mode == 5:
        chain = blockchain.chain
        blockchain.display_chains(chain)

    #to stop the process
    elif mode == 6:
        control = 0
        print()
    #when input is put of bound
    else: 
        print(Fore.RED + "\nSystem message: Input must be in choices!")
