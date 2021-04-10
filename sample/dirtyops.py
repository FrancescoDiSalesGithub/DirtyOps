import sys
import os

from graphics import graphics_controller
import downloaderops

try:    
	render = graphics_controller()
	if len(sys.argv) == 1:
		render.drawBanner()
		print("Insert at least an argument \n")
		render.printHelp()

	data = sys.argv[1]
	render.drawBanner()

	if data == "deploy":
		downloaderops.deploy()
	elif data == "configmap":
		downloaderops.configmap()
	elif data == "secret":
		downloaderops.secret()
	elif data == "service":
		downloaderops.service()
	elif data == "help" or data=="--help" or data=="-h":
		render.printHelp()
	else:
		print("Wrong argument passed \n")
		render.printHelp()
except:
	print("Something bad happened check your internet connection")
