import requests

url = 'https://ru.wttr.in/Череповец?n?M?T?q'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/London?n?M?T?q'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/SVO?n?M?T?q'
response = requests.get(url)
response.raise_for_status()
print(response.text)
