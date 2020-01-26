import os
#from cloudmesh.common.util import banner

class Provider:

    def __init__(self, name):
        self.name = name

    def delete(self):
        os.system("multipass delete")
        
    def exec(self):
        os.system("multipass exec")
        
    def find(self):
        os.system("multipass find")
        
    def get(self):
        os.system("multipass get")
        
    def help(self):
        os.system("multipass help")
        
    def info(self):
        os.system("multipass info")
        
    def launch(self):
        os.system("multipass launch")
        
    def list(self):
        os.system("multipass list")
        
    def mount(self):
        os.system("multipass mount")
        
    def purge(self):
        os.system("multipass purge")
        
    def recover(self):
        os.system("multipass recover")
        
    def restart(self):
        os.system("multipass restart")
        
    def set(self):
        os.system("multipass set")
        
    def shell(self):
        os.system("multipass shell")
        
    def start(self):
        os.system("multipass start")
        
    def stop(self):
        os.system("multipass stop")
        
    def suspend(self):
        os.system("multipass suspend")
        
    def transfer(self):
        os.system("multipass transfer")
        
    def umount(self):
        os.system("multipass umount")
        
    def version(self):
        os.system("multipass version")

    # def list(self):
    #     os.system("multipass find")

    # def shell(self):
    #     print(f"shell {self.name}")
    #     #os.system("multipass shell")

    # def run(self, command):
    #     print (f"run {command}")
    #     #os.system(f"multipass exec {command}")

        
if __name__ == "__main__":
    p = Provider("cloudmesh")
    p.run("hallo")
    p.list()
    p.shell()