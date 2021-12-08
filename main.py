from flask import Flask, render_template, Markup, request
import fetchconfig
import commitconfig
import monitor

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("monitor.html")

@app.route('/monitor')
def monitor_page():
    return render_template("monitor.html")

@app.route('/poll_r1',methods=['POST'])
def poll_r1():
    statusR1 = monitor.fetch_params(request.form['value1'],request.form['value2'],request.form['value3'])
    return render_template("monitor.html", statusR1=statusR1)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

