#!/usr/bin/python3
import pyfiglet
import socket
import sys

banner = """
|                                                              |
|                     IP_GRABBER_TOOL                          |
|welcome to my simple tool                                     |
|design by osama_Shawabkeh                                     |
|how to use                                                    |
|* just but a real link for the website that you want its ip   |
|* ex:www.google.com ex:www.yahoo.com without http://          |
"""
print(banner)

ascii_banner = pyfiglet.figlet_format("osama_Shawabkeh")
print(ascii_banner)

website = input("enter website to get it ip :")
if (website == "") and (website == int(website)):
	print("dont keep it empty / dont type a nubmers just links")

else:
	try:
		getip = socket.gethostbyname(website)
		print("-"*20)
		print("the ip is --->" +str(getip))
		print("-"*20)
	except:
		print("plase but link only")
		sys.exit()
