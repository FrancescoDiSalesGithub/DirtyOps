class graphics_controller:
	def __init__(self):
		pass
		
	def drawBanner(self):
		print("----------------------------------------------")
		print("DirtyOps")
		print("----------------------------------------------")
		
	def drawMenu(self):
		print("1 - Download deployment template yaml file")
		print("2 - Download config template yaml file")
		print("3 - Download secret template yaml file")
		print("4 - Download service template yaml file")
		print("5 - Download deployment and config yaml file")
		print("6 - Download deployment and service yaml file")
		print("7 - Download deployment and secret yaml file")
		print("8 - Download deployment with config and secret yaml file")
		print("9 - Download deployment,config, service and secret yaml file")
		print("10 - Exit")
	
	def reloadRender(self):
		self.drawBanner()
		print("")
		self.drawMenu()
