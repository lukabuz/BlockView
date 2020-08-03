from requests_respectful import RespectfulRequester
API_URL = "https://sochain.com/api/v2/"

class Requester:
    def __init__(self):
        self.rr = RespectfulRequester()
        self.rr.register_realm("sochain", max_requests=299, timespan=60)
        self.requestCount = 0

    def get_spent_transactions(self, address, after = ''):
        try:
            print("Request #" + str(self.requestCount) + " | Data on address " + address)
            response = self.rr.get(API_URL + "get_tx_spent/BTC/" + address + '/' + after, realms=["sochain"], wait=True)
            txs = response.json()['data']['txs']
            print("Request #" + str(self.requestCount) + " | Got " + str(len(txs)) + " transactions")
        except:
            print("Request #" + str(self.requestCount) + " | Got error")
            txs = []
        self.requestCount += 1
        return txs

    def get_transaction_data(self, txid):
        try:
            print("Request #" + str(self.requestCount) + " | Data on transaction " + txid)
            response = self.rr.get(API_URL + "get_tx_outputs/BTC/" + txid, realms=["sochain"], wait=True)
            outputs = response.json()['data']['outputs']
            print("Request #" + str(self.requestCount) + " | Got " + str(len(outputs)) + " outputs")
        except:
            print("Request #" + str(self.requestCount) + " | Got error")
            outputs = []
        self.requestCount += 1
        return outputs
