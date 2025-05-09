from flask import Flask, render_template

app = Flask(__name__)

alerts = [
    "Port Scan detected from 192.168.1.5",
    "DDos attach from 10.0.0.2"
]

@app.route('/')

def show_alerts():
    return render_template('alerts.html', alerts=alerts)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# app.py