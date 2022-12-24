import requests
API_KEY = "00b9150fb13196a06dc3bfad8d54de45"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Introdu numele orasului : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    vreme = data['weather'][0]['description']
    vantul = data['wind']['speed']
    presiunea = data['main']['pressure']
    temperature = round(data["main"]["temp"]-213.15, 2)
    print("Presiunea: ", presiunea)
    print("Vantul: ", vantul)
    print("Vremea: ", vreme)
    print("Temperature: ", temperature)
    f = open("file.txt", "w")
    f.write("presiunea:"+str(presiunea)+"\n"+"Vantul: "+str(vantul)+"\n"+"Vremea: "+str(vreme)+ "\n" + "Temperature: " +str(temperature))

else:
    print("Am intampinat o eroare")


