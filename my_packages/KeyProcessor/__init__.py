import pprint as pp

class KeyProcessor:
    def __init__(self, name, data={}):
        self.processor_name = name
        self.data = data
        self.data.update({self.processor_name: []})
        self.processing_result = False
    def process_key(self, config_string, value):
        config_boolean = False
        if config_string == 'True':
            config_boolean = True
        elif config_string == 'False':
            config_boolean = False
        elif config_string == 'return':
            if value == 'True':
                self.processing_result = True
            elif value == 'False':
                self.processing_result = False
        elif config_string == 'jobs':
            # config_boolean = True
            from DecisionTree import DecisionTree
            # data = {'test': 'test'}
            print('DecisionTree HERE:', value)
            decisionTree = DecisionTree(value, data=self.data)
        elif config_string == 'processors':
            config_boolean = True
            for processor in value:
                module_name = processor['name']
                data = processor['data']
                my_class = getattr(__import__(module_name), module_name)
                myClass = my_class(module_name, data)
                self.data[self.processor_name].append(myClass.process(processor))


        return config_boolean

    def process_value(self, value):
        print('Processing value: ', value)
        self.data[self.processor_name].append(value)
        return True
    
    def process(self, value):
        print('Processing process value: ')
        pp.pprint(value)
        return value
        # self.data[self.processor_name].append(value)       
        
        # print('PROCESSED process value:')
        # pp.pprint(value)