# A class that represents a node in the tree of transactions.
# Each node is a bitcoin adress, with the parent being the address that sent BTC to it
# and the children being all addresses it sent BTC to after it got BTC from the parent
class Leaf:
    def __init__(self, address, amountRecieved, txid, requester, parent = None,):
        self.address = address
        self.amountRecieved = amountRecieved
        self.txid = txid
        self.children = []
        self.parent = parent
        # The requester is a class from blockchain.py, it requires only the get_spent_transaction and
        # get_transaction_data methods, but because of the api this class should also implement request
        # throttling
        self.requester = requester

    def add_child(self, child):
        self.children.append(child)

    # Populates children with nodes this address has sent BTC to
    def populate_children(self):
        if(self.parent):
            after = self.parent.txid
        else:
            after = ''
        # Get all transactions sent from this address(after it received BTC from parent)
        spentTransactions = self.requester.get_spent_transactions(self.address, after)
        for transaction in spentTransactions: # Loop through transactions and create nodes for them
            outputs = self.requester.get_transaction_data(transaction['txid'])
            for output in outputs:
                newChild = Leaf(output['address'], output['value'], transaction['txid'], self.requester, self)
                self.add_child(newChild)
        return self.children

    # Creates a python dict recursively
    def make_json(self):
        children = []
        for child in self.children:
            children.append(child.make_json())
        return {'address': self.address, 'amountRecieved': self.amountRecieved, 'txid': self.txid, 'children': children}


# Create a tree starting from an original node of the given depth
# If the transaction trail being followed is run through a tumbler,
# any depth more than 5 is going to get a lot of transactions and take a lot of time to track down
def populate_tree(original, depth):
    children = [original]
    for i in range(0, depth):
        print("Level " + str(i))
        newChildren = []
        for child in children:
            print("getting children for " + child.address)
            gottenChildren = child.populate_children()
            newChildren.extend(gottenChildren)
            print("found " + str(len(gottenChildren)) + " children for " + child.address)
        children = newChildren
    return original
