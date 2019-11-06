import requests
from config import *

home = "{0}:{1}".format(EC2_ENDPOINT, EC2_PORT)
predict = "{0}:{1}/predict".format(EC2_ENDPOINT, EC2_PORT)
payload = """
{
	"img" : "abcdef.png"
}
"""

try:
	print("hitting", home)
	r = requests.get(url = home, data = payload)
	print("hitting", predict)
	r = requests.post(url = predict, data = payload)
	print("text: {}".format(r.text))
except Exception as e:
	print(e)