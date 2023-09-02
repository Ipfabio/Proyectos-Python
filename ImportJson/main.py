from urllib.request import urlopen
import json
from pprint import  pprint
url = "http://localhost:8000/api/persona/"

response = urlopen(url)
data = json.loads(response.read())
for i in data:
    pprint(i)
    break
