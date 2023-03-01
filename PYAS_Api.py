import requests

def scan(types,text):
    response = requests.get("https://api.pyas.cf/pyas", params={types: text})
    if response.status_code == 200:
        if response.text == "True":
            return True
        else:
            return False
    else:
        return response.status_code

print(scan("md5","<md5 hashes>"))

# https://api.pyas.cf/pyas?md5=<md5 hashes>
# return string True, False
