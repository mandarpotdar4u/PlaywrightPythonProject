import json
import os

myjsonfile = open('/data/json_data.json', 'r')
jsondata = myjsonfile.read()


obj = json.loads(jsondata)

json_username = str(obj['username'])
print(json_username)
json_password = str(obj['username'])
print(json_password)
json_invalidusername = str(obj['invalid_username'])
print(json_invalidusername)
json_invalidpassword = str(obj['invalid_password'])
print(json_invalidpassword)
json_Actual_Title = str(obj['Actual_Title'])
print(json_Actual_Title)


def init_azure_clients():
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, '../dara/json_data.json')
    with open(config_path) as config_file:
        config_data = json.load(config_file)

    credential = init_azure_clients(
        json_username=config_data["username"],
        json_password=config_data["username"],
        json_invalidusername=config_data["invalid_username"],
        json_invalidpassword = config_data["invalid_password"],
        json_Actual_Title = config_data["Actual_Title"]
    )

