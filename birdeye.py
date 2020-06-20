from urllib.request import Request, urlopen

request = Request('https://api.birdeye.com/resources/v1/review/businessid/158170949468469/summary?api_key=bJQGlIUGx2ZZ9YlnuVPPYMVR3yhrmWAU')



response_body = urlopen(request).read()
print(response_body)