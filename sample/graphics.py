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
		print("4 - Download deployment and secret yaml file")
		print("5 - Download deployment and config yaml file")
		print("6 - Download deployment,config and secret yaml file")
		print("7 - Exit")
	
	def reloadRender(self):
		self.drawBanner()
		print("")
		self.drawMenu()
