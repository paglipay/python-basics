# import json

# class DTree:
#     def __init__(self):
#         self.import_obj_instance = {}
#         self.current_module_name = None
#         self.data = None

#     def init_import_obj(self, module_name, data):
#         if module_name in self.import_obj_instance:
#             self.current_module_name = module_name
#         else:
#             my_class = getattr(__import__(module_name), module_name)
#             self.current_module_name = module_name
#             self.import_obj_instance[self.current_module_name] = my_class(module_name, data)

# # Read the JSON document
# with open('processors.json', 'r') as f:
#     processors = json.load(f)['processors']

# # Create a DTree instance
# dtree = DTree()

# # Import the processors and process the data
# for processor in processors:
#     dtree.init_import_obj(processor['name'], processor['data'])
#     result = dtree.import_obj_instance[processor['name']].process()
#     print(f'Result from {processor["name"]}: {result}')

import json
from DecisionTree import DecisionTree

# Read the JSON document
with open('processors.json', 'r') as f:
    config = json.load(f)

# Create a DTree instance and process the config
data = {'test': 'test'}
decisionTree = DecisionTree(config, data=data)
print(data)