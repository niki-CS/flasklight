from gpiozero import LED
from time import sleep
from flask import Flask, render_template, request

app = Flask(__name__)
led = LED(17)
led.off()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animate', methods=['POST'])
def animate():
    light = request.form['light']
    
    if light == "blink":
        # while light == "blink":
        print('blink')
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)
        led.on()
        sleep(.5)
        led.off()


    elif light == "on":
       print('on')
       led.on()

    elif light == "off":
        print('off')
        led.off()
   
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5001')