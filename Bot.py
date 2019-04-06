import time
import requests, json

print ("""
 _  __      ___                      
 | |/ /_ __ / _ \ _ __  _   _ ________
 | ' /| '__| | | | '_ \| | | |_  /_  /
 | . \| |  | |_| | | | | |_| |/ / / / 
 |_|\_\_|   \___/|_| |_|\__,_/___/___|
 """)
time.sleep(0.7)
print (" Tools	: BotChat ")
time.sleep(0.7)
print (" Author	: Kr0nuzz ")
time.sleep(0.7)
print (" Github	: https://github.com/Kr0nuzz")
time.sleep(0.7)

print ("Silahkan kirim pesan!")

while(True):
	try:
	    pesan = input("Anda: ")
	    url = "http://sandbox.api.simsimi.com/request.p?key=f9816a7b-c300-43e2-a224-11d6efb92fbb&lc=id&ft=1.0&text=%s" % pesan
	    link_json = requests.get(url)
	    data = json.loads(link_json.text)
	    print ("Bot: %s" %( data['response']))
	except KeyError:
		print("Saya Tidak Mengerti :(")