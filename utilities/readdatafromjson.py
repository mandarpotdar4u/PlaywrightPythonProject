import json
import os

# myjsonfile = open('data/Json_data.json')
# jsondata = myjsonfile.read()

# obj = json.loads(jsondata)
#
# json_username = str(obj['username'])
# print(json_username)
# json_password = str(obj['username'])
# print(json_password)
# json_invalidusername = str(obj['invalid_username'])
# print(json_invalidusername)
# json_invalidpassword = str(obj['invalid_password'])
# print(json_invalidpassword)
# json_Actual_Title = str(obj['Actual_Title'])
# print(json_Actual_Title)


myjsonfile = os.path.dirname(__file__)
config_path = os.path.join(myjsonfile, '../data/Json_data.json')
with open(config_path) as config_file:
 obj = json.load(config_file)

json_username = str(obj['username'])
# print(json_username)
json_password = str(obj['password'])
json_invalid_username = str(obj['invalid_username'])
json_invalid_password = str(obj['invalid_password'])
json_Actual_Title = str(obj['Actual_Title'])

