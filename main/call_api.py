import requests


class CallApi():
	
	def __init__(self, url, params=None):
		self.url = url
		self.params = params
		
	def call_api(self):
		headers = {
			'x-rapidapi-key': "fba481570emsh5cac1f6f37eb44cp1cfc82jsnc77f26030c2d",
			'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
		}
		
		response = requests.request("GET", self.url, headers=headers, params=self.params)
		return response.json()
