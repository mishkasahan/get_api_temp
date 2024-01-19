import requests


def get_temp(api_key, city):
    url = (f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            resp = response.json()
            temperatura = resp['main']['temp']
            print(f"Темперетура у місті {city} - {temperatura} градусів")
        else:
            print(f"Помилка отримання відповіді. Код помилки - {response.status_code}")

    except Exception as e:
        print(f"Виникла помилка: {e}")


misto = input("Введіть місто:")
api_kej = input("Введіть свій API KEY:")

get_temp(api_kej, misto)
