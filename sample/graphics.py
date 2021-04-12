class graphics_controller:
	def __init__(self):
		pass
		
	def draw_banner(self):
		print("----------------------------------------------")
		print("DirtyOps")
		print("---------------------------------------------- \n")
		
	def print_help(self):
		print("------------------------------------------------")
		print("Example usage")
		print("------------------------------------------------ \n")
		print("example usage for linux users: dirtyops.py deployment /home/user/myproject")
		print("example usage for windows users: dirtyops.py deployment C:/user/myproject \n \n")
		print("------------------------------------------------")
		print("Arguments")
		print("------------------------------------------------ \n")		
		print("deployment = downloads a deployment yaml file")
		print("service = downloads a service yaml file")
		print("configmap = downloads a configmap yaml file")
		print("secret = downloads a secret yanl file")
		print("--help = calls this help screen")
		print("help = calls this help screen")
		print("-h = calls this help screen \n")
