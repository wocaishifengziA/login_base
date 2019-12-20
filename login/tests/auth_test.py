import requests



res = requests.get("http://127.0.0.1:8000/login")
print(res.text)


headers = {
    "Authorization": res.text
}
res = requests.get("http://127.0.0.1:8000/test", headers=headers)
print(res.text)