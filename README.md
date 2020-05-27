Get your API key from https://macaddress.io 
Set your key in the shell execution environement. 
e.g for bash 
 export MACAPIKEY='api key from macaddress.io'
Run the following command 
 macvendor.py <MAC address>

Common errors

Command not found : Add current directory to path or execute with ./
Permission denied : Add execute permission to file. 
 chmod +x macvendor.py
 or execute with python interpreter
 python macvendor.py 44:38:39:ff:ef:57

---------------
Build with Docker

docker build -f Dockerfile . --build-arg  MACAPIKEY=$MACAPIKEY -t macvendor
docker run  macvendor 44:38:39:ff:ef:57
