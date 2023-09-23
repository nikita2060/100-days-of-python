import requests  # requests is a python package that makes it easier to send http requests and handle the responses.
# It simplifies API integration
category = "happiness"
api_url = "https://api.api-ninjas.com/v1/quotes?category={}"
response = requests.get(api_url.format(category), headers={'X-Api-Key': 'S0rvl94oEYPUXHNBkb+FTQ==cvBVZmfn2J8QnqOG'})
response.raise_for_status()
quotes = response.json()
print(quotes)