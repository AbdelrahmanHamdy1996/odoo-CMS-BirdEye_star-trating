from urllib.request import Request, urlopen
import xmltodict
import json

request = Request(
    'https://api.birdeye.com/resources/v1/review/businessid/158170949468469/summary?api_key=bJQGlIUGx2ZZ9YlnuVPPYMVR3yhrmWAU')

response_body = urlopen(request).read()
# print(response_body)
my_dict = xmltodict.parse(response_body)
json_data = json.dumps(my_dict)

print(json_data)
