Note- before run this program, register free account on openweathermap.com. then you'll get app_id key, use that key in below url <your_secret_appid> section.

  
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=<your_secret_appid>&units=metric'.format(city)
