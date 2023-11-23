import json
from DecisionTree import DecisionTree
import pprint as pp

# Read the JSON document
with open('processors.json', 'r') as f:
    config = json.load(f)

# Create a DTree instance and process the config
data = {'test': 'test'}
decisionTree = DecisionTree(config, data=data)
print("OUTPUT HERE:")
pp.pprint(data)