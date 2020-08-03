from Classes import Leaf, populate_tree
from Blockchain import Requester
import json


requester = Requester()
originalNode = Leaf("13nmJ3SsNB5pSyQrmX3e6zveY9kHGw8Vs3", 410, "eb4a367416e02d1fd77d78d530a0f7f1ff7f84cffb3b595deeb7d5ea399d9100", requester)


populatedOriginal = populate_tree(originalNode, 4)

with open('data.json', 'w') as fp:
    json.dump(populatedOriginal.make_json(), fp, indent=4)