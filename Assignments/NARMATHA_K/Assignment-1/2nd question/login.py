# -*- coding: utf-8 -*-
"""


@author: NARMATHA
"""

# -*- coding: utf-8 -*-
"""
@author: NARMATHA
"""
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s to Flask programming' % name
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
if __name__ == '__main__':
    app.run(debug=True)
