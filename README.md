If you have a MAC address of the machine, following are the steps to find it's vendor
1. Get your API key from https://macaddress.io   
2. Set your key in the shell execution environement.  
e.g in bash 
 export MACAPIKEY='api key from macaddress.io'
3. Clone the repo  
   git clone https://github.com/doiob/macdata.git   
3. Run the following command and pass MAC address on the command line   
  macvendor.py  &lt; Mac address &gt;

Common errors

Command not found : Add current directory to the path or execute with ./  
Permission denied : Add execute permission to the file.  
 chmod +x macvendor.py  
 Or  
 execute with python interpreter  
 python macvendor.py 44:38:39:ff:ef:57 

---------------
Build with Docker

1) From local Dockerfile

docker build -f Dockerfile . --build-arg  MACAPIKEY=$MACAPIKEY -t macvendor

2) From github   
docker build https://github.com/doiob/macdata.git  --build-arg  MACAPIKEY=$MACAPIKEY -t macvendor

Run the command

docker run  macvendor 44:38:39:ff:ef:57  
