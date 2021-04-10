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
		os.abort()

	if len(sys.argv) == 2:
		render.drawBanner()
		print("Directory argument is missing \n")
		render.printHelp()
		os.abort()
        
	if len(sys.argv) > 3:
		render.drawBanner()
		print("Too much arguments \n")
		render.printHelp()
		os.abort()
                
	data = sys.argv[1]
	directory = sys.argv[2]
	currentdir = os.getcwd()
		
	render.drawBanner()

	if data == "deploy":
		os.chdir(directory)
		downloaderops.deploy()
	
		print("deploy template downloaded in: ")
		print(directory)
                
		os.chdir(currentdir)
	elif data == "configmap":
		os.chdir(directory)
		downloaderops.configmap()
		
		print("configmap template downloaded in: ")
		print(directory)
                
		os.chdir(currentdir)
	elif data == "secret":
		os.chdir(directory)
		downloaderops.secret()
		
		print("secret template downloaded in: ")
		print(directory)
                
		os.chdir(currentdir)
	elif data == "service":
		os.chdir(directory)
		downloaderops.service()
		
		print("service template downloaded in: ")
		print(directory)
                
		os.chdir(currentdir)
	elif data == "help" or data=="--help" or data=="-h":
		render.printHelp()
	else:
		print("Wrong argument passed \n")
		render.printHelp()
except Exception as e:
	print(e)
