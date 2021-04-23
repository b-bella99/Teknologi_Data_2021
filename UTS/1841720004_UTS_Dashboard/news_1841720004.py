import requests

url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=75af8344ed354520b74a09ab060950ad"
headlines = []

def GetNews():
    print("-GATHERING NEWS")

    response = requests.get(url)
    response_json = response.json()

    for news in response_json['articles']:
        headlines.append(news['title'])

    return headlines