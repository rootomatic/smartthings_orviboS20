# smartthings orvibo S20 integration using raspberry pi


Grab the Device Handler [here](https://github.com/rootomatic/SmartThingsPublic/blob/master/devicetypes/rootomatic/orvibo-s20-switch.src/orvibo-s20-switch.groovy)  

In the smartthings app, add a new device with your Raspberry Pi IP, along with the IP & Mac Address of the Orvibo S20 socket. You should be able to get this information from your router/switch, or running arp -a {IP address} from your pi.

>Note: You will need to have set the S20 up already using the ios/android app.

Set up python / flask on the Raspberry Pi:  
`sudo apt-get install python-pip`    
`sudo pip install flask`    

Clone the repo:  
`git clone https://github.com/rootomatic/smartthings_orviboS20.git`    

Run the server orvibo_server.py 
`sudo python orvibo_server.py`

>Note: You should be aware that running the server as root is a security risk, and make the necessary access changes to this code to secure it, necessary to your requirements.
