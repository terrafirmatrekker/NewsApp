from flask import render_template
from newsapi import NewsApiClient
import requests

from app import app

NEWS_API_KEY = "b45857456cc24d44828e244b7fff7c6b"


@app.route("/")
def Index():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english, bbc-news")

    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []
    # url = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])
        # url.append(myarticles["url"])

    mylist = zip(
        news,
        desc,
        img,
        # url,
    )

    return render_template("index.html", context=mylist)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/crypto")
def Crypto():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    topheadlines = newsapi.get_everything(
        q="crypto",
        language="en",
        sort_by="relevancy",
        page=2,
    )
    articles = topheadlines["articles"]

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles["title"])
        desc.append(myarticles["description"])
        img.append(myarticles["urlToImage"])

    mylist = zip(
        news,
        desc,
        img,
    )

    return render_template("crypto.html", context=mylist)


@app.route("/weather")
def get_weather():
    api_key = "858e77ff0c7c2272f4ad4ab4def26472"
    city = "Louisville"
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid="
        + api_key
        + "&units=imperial"
    )
    request = requests.get(url)
    json = request.json()
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    speed = json.get("wind").get("speed")
    return {
        "description": description,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "speed": speed,
    }
    weather_report = zip(description, temp_min, temp_max, speed)

    return render_template("weather.html")
