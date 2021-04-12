
import urllib.request
import constantsurl

class downloader:

		
	def deploy(self):
	   urllib.request.urlretrieve(constantsurl.deploy,"deploy.yaml")

	def configmap(self):
	    urllib.request.urlretrieve(constantsurl.configmap,"configmap.yaml")

	def secret(self):
	    urllib.request.urlretrieve(constantsurl.secret,"secret.yaml")

	def service(self):
	    urllib.request.urlretrieve(constantsurl.service,"service.yaml")
	
