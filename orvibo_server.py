from flask import Flask
import subprocess
app = Flask(__name__)

@app.route('/socket/<socketIp>/<socketMac>/<call>')
def orviboCall(socketIp,socketMac,call): 
     return subprocess.check_output(['perl', '/home/pi/s20.pl',socketIp,socketMac,call])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
