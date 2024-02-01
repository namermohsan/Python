# Parsing Jason
# ---------------------------------------------------------------
# This script requires a JSON file (sample.json) in the same working directory so the script can read from it.
# Alternatively, we can input the content of this file as a string and assign it to a variable.
#the content of this file:
# {
#   "name": "John",
#   "age": 30,
#   "city": "New York",
#   "hobbies": [
#     "reading",
#     "running",
#     "traveling"
#   ],
#   "education": {
#     "degree": "Bachelor's",
#     "major": "Computer Science",
#     "university": "Harvard"
#   }
# }


import json

json_data = '''{
  "name": "John",
  "age": 30,
  "city": "New York",
  "hobbies": [
    "reading",
    "running",
    "traveling"
  ],
  "education": {
    "degree": "Bachelor's",
    "major": "Computer Science",
    "university": "Harvard"
  }
}
'''

output = json.loads(json_data)
print(type(output))     #this will print the datatype dictionary

from_file = open('sample.json', 'r')
output = json.load((from_file))     #notice that there is no letter s here because we are reading from a file and not string
print(type(output))        #this will also print dictionary, it will do the exact same thing except that this time it reads from a file 
from_file.close()

#All The Very Best,
    #Nameer