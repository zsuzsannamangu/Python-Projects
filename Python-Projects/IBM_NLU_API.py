#This code utilizes the IBM Watson Natural Language Understanding API
#This API allows you to analyze text for sentiment, entities, keywords, concepts, categories, emotions, and more.

"""
First create a free IBM Cloud Account and log in
Go to the IBM Watson Natural Language Understanding page in the IBM Cloud Catalog.
Click on "Create" to create a new Natural Language Understanding service instance.
Choose the region, pricing plan (Lite plan is free), and other settings as per your requirements.
Click on "Create" to provision the service.

Once the Natural Language Understanding service is created, go to the service dashboard.
Click on "Manage" to view your service details.
Under "Service credentials," click on "New credential" to generate API credentials (API key and URL).
Note down the API key and URL, as you will need them to access the API

Install the IBM Watson SDK for Python using pip
pip install ibm-watson"""

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

# Set up IBM Watson Natural Language Understanding service
api_key = 'Add your API here'
url = 'Add URL here'
version = '2022-08-10'
authenticator = IAMAuthenticator(api_key)
nlu = NaturalLanguageUnderstandingV1(version=version, authenticator=authenticator)
nlu.set_service_url(url)

# Sample text for sentiment analysis
text = "The new movie exceeded my expectations, it was incredibly engaging and emotional."

# Analyze sentiment using IBM Watson NLU
response = nlu.analyze(text=text, features=Features(sentiment=SentimentOptions())).get_result()

# Print sentiment analysis results
sentiment = response['sentiment']['document']['label']
score = response['sentiment']['document']['score']
print(f"Sentiment: {sentiment}")
print(f"Sentiment Score: {score}")
