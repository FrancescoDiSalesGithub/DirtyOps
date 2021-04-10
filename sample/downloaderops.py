
import urllib.request
import constantsurl

def deploy():
   urllib.request.urlretrieve(constantsurl.deploy,"deploy.yaml")

def configmap():
    urllib.request.urlretrieve(constantsurl.configmap,"configmap.yaml")

def secret():
    urllib.request.urlretrieve(constantsurl.secret,"secret.yaml")

def service():
    urllib.request.urlretrieve(constantsurl.service,"service.yaml")
