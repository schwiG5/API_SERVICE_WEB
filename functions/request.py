import requests
import json

url = "https://www.yammer.com/api/v1/messages.json"
message = url




data = {
    'content': message
}

header = {
    'authorization': 'MzAyNTE0OTk0NDk3NzE2MjI1.YiDQjg.TXr3sO2nhVWYS-Vd0smDG4oynVg'
}

r = requests.post('https://discord.com/api/v9/channels/944160113797791774/messages', 
                data=data, headers = header)

print(r.json())