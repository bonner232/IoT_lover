import network
import time

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # STA_IF mode for station (client) mode
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            time.sleep(1)

    print("Connected to WiFi")
    #print("IP Address:", wlan.ifconfig()[0])

# Replace 'your_ssid' and 'your_password' with your Wi-Fi credentials
