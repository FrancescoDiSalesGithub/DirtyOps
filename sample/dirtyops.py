import sys
import os

from graphics import graphics_controller
from downloaderops import downloader
import errormessage

try:
	render = graphics_controller()
	operations = downloader()
	
	if len(sys.argv) == 1:
		render.draw_banner()
		print(errormessage.one_argumenter)
		render.printHelp()
		os.abort()

	if len(sys.argv) == 2:
		render.draw_banner()
		print(errormessage.directory_error)
		render.printHelp()
		os.abort()
        
	if len(sys.argv) > 3:
		render.draw_banner()
		print(errormessage.toomuch_argumenter)
		render.printHelp()
		os.abort()
                
	data = sys.argv[1]
	directory = sys.argv[2]
	currentdir = os.getcwd()
		
	render.draw_banner()
	os.chdir(directory)
	
	if data == "deployment":
		
		operations.deploy()
		print("deploy template downloaded in: ")
		print(directory)
		
	elif data == "configmap":
		
		operations.configmap()
		print("configmap template downloaded in: ")
		print(directory)
		
	elif data == "secret":

		operations.secret()
		print("secret template downloaded in: ")
		print(directory)
		
	elif data == "service":
		
		operations.service()
		print("service template downloaded in: ")
		print(directory)
		
	elif data == "help" or data=="--help" or data=="-h":
		render.print_help()
	else:
		print("Wrong argument passed \n")
		render.print_help()
		
	os.chdir(currentdir)
except Exception as e:
	print(e)
