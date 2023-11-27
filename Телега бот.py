import telebot
import requests
import datetime
import pytz

# Получение текущего времени в Москве
moscow_timezone = pytz.timezone('Europe/Moscow')
current_time = datetime.datetime.now(moscow_timezone).time()

# Проверка, что текущее время 8:00 утра
if current_time.hour == 23 and current_time.minute == 16:
    # Получение данных о погоде в Минске через OpenWeatherMap API
    weather_api_key = 'a0c6d6c8243c4b7ad926cb76f34d7640'  # Замените на ваш ключ API для OpenWeatherMap
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=Minsk&appid={weather_api_key}&units=metric'
    response = requests.get(weather_url)
    weather_data = response.json()

    # Формирование сообщения с погодой и пожеланием
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    message = f'Доброе утро Бубля! В Минске сейчас {temperature}°C, {weather_description}.'

    # Отправка сообщения в телеграм
    bot = telebot.TeleBot('6910536186:AAEJA39qoi9hP6IWdEq7kDQloK2RxsfimWQ')  # Замените на ваш токен бота. Я - 449868007, Бубля - 928848734. 
    chat_id = '449868007'  # Замените на ваш chat_id
    bot.send_message(chat_id, message)
