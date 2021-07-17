import wifi
import time
import adafruit_requests
import socketpool
import ssl
import rtc

class Network():

    secrets = {
        'ssid' : ',
        'passwd' : '',
        'aio_username' : '',
        'aio_key' : '',
        'timezone' : "", # http://worldtimeapi.org/timezones
        }
        
    # Get our username, key and desired timezone
    aio_username = secrets["aio_username"]
    aio_key = secrets["aio_key"]
    location =secrets.get("timezone", None)
    TIME_URL = "https://io.adafruit.com/api/v2/%s/integrations/time/struct?x-aio-key=%s"% (aio_username, aio_key)
    

    def __init__(self):
        # Iniatialise the network
        for network in wifi.radio.start_scanning_networks():
            print(network, network.ssid, network.channel)
        wifi.radio.stop_scanning_networks()

        print("joining network...")
        print(wifi.radio.connect(ssid=self.secrets["ssid"],password=self.secrets["passwd"]))
        # the above gives "ConnectionError: Unknown failure" if ssid/passwd is wrong

        print("my IP addr:", wifi.radio.ipv4_address)
        
       
        
    def get_time(self):
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        self.adaTime = requests.get(self.TIME_URL).json() 
        return self.adaTime
        

    def syncRTC_time(self):
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        adaTime = requests.get(self.TIME_URL).json() 
        boardRTC = rtc.RTC()
        boardRTC.datetime = time.struct_time((adaTime["year"], 
         adaTime["mon"], adaTime["mday"], adaTime["hour"], 
         adaTime["min"], adaTime["sec"], adaTime["wday"], 
         adaTime["yday"], adaTime["isdst"]))
