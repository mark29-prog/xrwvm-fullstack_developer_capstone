import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = "https://afriyiemark1-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai"

sentiment_analyzer_url = "https://sentianalyzer.29ylvu4124fo.us-south.codeengine.appdomain.cloud/"


# ✅ GET request to backend
def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from:", request_url)

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("GET error:", e)
        return {}


# ✅ Sentiment analysis microservice
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Sentiment error:", e)
        return {}


# ✅ POST review to backend
def post_review(data_dict):
    request_url = backend_url + "/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except Exception as e:
        print("POST error:", e)
        return {}