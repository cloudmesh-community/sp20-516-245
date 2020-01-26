import os
#from cloudmesh.common.util import banner

class Provider:

    def __init__(self, name):
        self.name = name

    def delete(self, name):
        os.system(f"multipass delete -p {name}") #don't need to call purge after since we use the p flag
        
    def images(self):
        os.system("multipass find")
        
    def get(self, key):
        os.system(f"multipass get {key}")
        
    def help(self, command=""):
        os.system(f"multipass help {command}")
        
    def info(self, instance):
        os.system(f"multipass info {instance}")
        
    def launch(self, image):
        os.system(f"multipass launch {image}")
        
    def list(self):
        os.system("multipass list")
        
    def mount(self, source, target):
        os.system(f"multipass mount {source} {target}")
        
    def purge(self):
        os.system("multipass purge")
        
    def recover(self, name):
        os.system(f"multipass recover {name}")
        
    def restart(self, name=""):
        os.system(f"multipass restart {name}")
        
    def set(self, key, value):
        os.system(f"multipass set {key}={value}")
        
    def shell(self, instance=""):
        os.system(f"multipass shell {instance}")
        
    def start(self, instance=""):
        os.system(f"multipass start {instance}")
        
    def stop(self, name):
        os.system(f"multipass stop {name}")
        
    def suspend(self, name):
        os.system(f"multipass suspend {name}")
        
    def transfer(self, source, dest):
        os.system(f"multipass transfer {source} {dest}")
        
    def umount(self, instance):
        os.system(f"multipass umount {instance}")
        
    def version(self):
        os.system("multipass version")
            
    def run(self, command):
        os.system(f"multipass exec {command}")
        
if __name__ == "__main__":
    p = Provider("cloudmesh")
    p.run("hallo")
    p.list()
    p.shell()