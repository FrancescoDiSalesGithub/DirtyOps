class graphics_controller:
	def __init__(self):
		pass
		
	def drawBanner(self):
		print("----------------------------------------------")
		print("DirtyOps")
		print("----------------------------------------------")
		
	def printHelp(self):
		print("deployment = downloads a deployment yaml file")
		print("service = downloads a service yaml file")
		print("configmap = downloads a configmap yaml file")
		print("secret = downloads a secret yanl file")
		print("--help = calls this help screen")
		print("help = calls this help screen")
		print("-h = calls this help screen")
