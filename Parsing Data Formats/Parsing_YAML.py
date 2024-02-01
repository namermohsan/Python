# Parsing Yaml Files
# ------------------------------------------------------------------------------
#This script requires a file saved in the same working directory called sample.yaml
#it also requires installing The library pyyaml, you can use this command to install it : #pip install pyyaml
#The sample file content:
# people:
#   - name: John
#     age: 30
#     city: New York
#     hobbies:
#       - reading
#       - running
#       - traveling


from yaml import load , load_all #load_all is used for this example to load everything and because people is not commented in the YAML file
import yaml

stream = open('sample.yaml', 'r')
documents = load_all(stream , Loader=yaml.SafeLoader) #we also have FullLoader the difference is FullLoader is used with trusted sources

print(type(documents)) #the data type will be generator, to dig in we need a loop

for doc in documents:
    print(doc['people'])
     #the type will be a list as follows: [{'name': 'John', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'running', 'traveling']}]
    print(doc['people'][0]['name']) 
    #the result will be John
    #to get only the name because everything will be in a list as one element and the first element of the list is zero
    #note that when we include the people element in yaml, this works only with load_all


# Another example:

#This script requires a file saved in the same working directory called sample.yaml
#it also requires installing : #pip install pyyaml
#The sample file content:
#   - name: John
#     age: 30
#     city: New York
#     hobbies:
#       - reading
#       - running
#       - traveling


from yaml import load , load_all #load is used for this example to load everything and because people element is not here anymore
import yaml

stream = open('sample.yaml', 'r')
documents = load(stream , Loader=yaml.SafeLoader) #we also have FullLoader the difference is FullLoader is used with trusted sources

print(type(documents)) #the data type will be LIST, because we removed element people, to dig in we need a loop

for doc in documents:
    print(type(doc)) #the type here will be dictionary
    print(doc['name']) #the result will be John


#All The Very Best,
    #Nameer