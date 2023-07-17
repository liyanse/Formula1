import requests

url = "https://suitecrmdemo.dtbc.eu/index.php?action=ajaxui#ajaxUILoc=index.php%3Fmodule%3DLeads%26action%3Dindex"
response = requests.get(url)
    
print(response.text)