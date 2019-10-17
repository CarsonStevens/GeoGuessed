import requests
from config import *

payload = """
{
	"img" : "abcdef.png"
}
"""

try:
	r = requests.post(url = EC2_ENDPOINT, data = payload)
	print("text: {}".format(r.text))
except Exception as e:
	print(e)