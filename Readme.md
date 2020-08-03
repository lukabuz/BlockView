# BlockFollow
This is a python script that can be used to track transactions on the bitcoin blockchain.
It starts from an initial bitcoin address, and creates a tree from where that address has sent bitcoin, where those addresses sent that bitcoin, and so on.


The depth of the search and the starting address can both be changed in the main.py file.


Since this tool uses an api that has a limit of 300 requests per minute, a throttling library is used to adhere to this limit. This throttling library requires a redis instance to be running on localhost:6379. A default redis installation will work fine.

## Inspiration
The inspiration for this script comes from a recent attack performed on a US Travel firm. The attackers encrypted the files of the company and managed to get them to pay 410BTC through an [interestingly civil](https://twitter.com/jc_stubbs/status/1289199296328298497) conversation.


I wanted to find out more about where the trail of bitcoin from this attack led, so I wrote this script.



The repo includes a small result json file(data.json) that is a result of the search done at depth=4 