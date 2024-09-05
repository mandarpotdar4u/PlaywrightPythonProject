import json
import os

from config import settings


config_path = settings.json_config_path
with open(config_path) as config_file:
 obj = json.load(config_file)

json_username = str(obj['username'])
# print(json_username)
json_password = str(obj['password'])
json_invalid_username = str(obj['invalid_username'])
json_invalid_password = str(obj['invalid_password'])
json_Actual_Title = str(obj['Actual_Title'])

