#!/usr/bin/env python

from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route("/")
def hello():
	return """This message is coming from Flask.
			Running on {}, {}""".format(socket.gethostname(), request.remote_addr)
	# return render_template('index.html')

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 5000, debug=True)
