import json
import os
import re

from flask import Flask, render_template, request

import sys

sys.path.append('../')
from getcontact.getcontact import GetContactAPI

app = Flask(__name__)


@app.route('/find', methods=['GET'])
def upload_page():
    if request.method == 'GET':
        phone = request.args['phone']
        is_valid = re.findall(r'\d{11}', phone)
        if is_valid:
            g = GetContactAPI()
            return json.dumps(g.get_information_by_phone('+' + phone))
        else:
            return json.dumps({'displayName': 'Error'})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
