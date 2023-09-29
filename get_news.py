
import requests
def get_latest_news():
    NEWS_API_KEY = "17872d9bca7343e4866348761f3d3476"
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
        print(article, sep='\n')
    return news_headlines[:5]
get_latest_news()

