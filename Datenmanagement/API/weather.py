import requests
import matplotlib.pyplot as plt

url = "https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relative_humidity_2m,surface_pressure"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    time = data["hourly"]["time"][:36]
    temperature = data["hourly"]["temperature_2m"][:36]
    humidity = data["hourly"]["relative_humidity_2m"][:36]
    surface_pressure = data['hourly']['surface_pressure'][:36]

    plt.subplot(1,3,1)
    plt.plot(time, temperature, marker = 'x', label = 'Temperature')
    plt.title('Temperature')
    plt.legend(loc = 'upper right')
    tick_positions = range(0, len(time), 6)
    plt.xticks([time[i] for i in tick_positions])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    
    plt.subplot(1,3,2)
    plt.plot(time, humidity, marker = 'x', label = 'Humidity')
    plt.title('Humidity')
    plt.legend(loc = 'upper right')
    tick_positions = range(0, len(time), 6)
    plt.xticks([time[i] for i in tick_positions])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    
    plt.subplot(1,3,3)
    plt.plot(time, surface_pressure, marker = 'x', label = 'Surface Pressure')
    plt.title('Surface Pressure')
    plt.legend(loc = 'upper right')
    tick_positions = range(0, len(time), 6)
    plt.xticks([time[i] for i in tick_positions])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    
    plt.suptitle('Weather in Bangkok')
    plt.show()

else:
    print(f"Fehler: {response.status_code} ")