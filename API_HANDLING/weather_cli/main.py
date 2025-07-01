import requests
from config import WEATHER_API_KEY,NEWS_API_KEY


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city ,
        "appid": WEATHER_API_KEY,
        "units": "metric", 
    }
    response = requests.get(url,params=params)
    data = response.json()
    if response.status_code == 200:
        print(f'\n🌤️ Weather in {city}: {data['weather'][0]['description'].capitalize()}')
        print(f'Coordinates: \n Longitudes {data['coord']['lon']}°\n Latitudes: {data['coord']['lat']}°')
        print(f'Temperature: {data['main']['temp']}°C')
        print(f'Humidity: {data['main']['humidity']}%')
        print(f'Feels Like: {data['main']['feels_like']}°C')
    else:
        raise Exception("Failed to fetch weather data")
    
    
def get_news(topic,country):
    url=f"https://newsapi.org/v2/top-headlines?country={country}&category={topic}&apiKey={NEWS_API_KEY}"
    params = {
        "q": topic,
        "apiKey": NEWS_API_KEY,
        "pageSize": 3,
        "country": country.lower(),
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200 and data.get("status") == "ok":
        print(f"\n📰Top News in {country.upper()} on '{topic}':")
        for i,article in enumerate(data['articles'],1):
            print(f"{i}. {article['title']} ({article['source']['name']})") 
            print(f"Author: {article['author']}, \nDescription: {article['description']}")      
    else:
        print(f"Error : {data.get('message', 'Unable to fetch news')}")


def main():
    print("\"\"\"\n Welcome to CLI Weather & News App\n\"\"\"")
    city = input("Enter your city: ")
    topic = input("Enter a topic you're interested in: ")
    country = input("Enter your country 2-letter code (eg. us, in, gb)").lower()
    
    try:
        get_weather(city)
        get_news(topic,country)
    except Exception as e:
        print(e)   
    
    
    
    
if __name__ == "__main__":
    main()   
    