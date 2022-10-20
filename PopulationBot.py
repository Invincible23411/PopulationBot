import tweepy
import requests
import time

# These are the keys
api_key = "Your_key"
api_key_secret = "Your_key"
access_token = "Your_key"
access_token_secret = "Your_key"

# Authenticator section here
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

while True:
	url = "https://get-population.p.rapidapi.com/population"

	headers = {
	"X-RapidAPI-Key": "Rapid_api_key_here",
	"X-RapidAPI-Host": "get-population.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers,)

	population = response.text[39:52]

	api.update_status("The current world population is " + population)
	print("working")
	time.sleep(600)