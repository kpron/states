import os
from flask import Flask
from states import http_check, SERVICES

app = Flask(__name__)


@app.route("/")
def states():
    page = '<html><body>'
    page += '<center>'
    for service in SERVICES:
        page += '<h2>%s</h2>' % service
        page += '<p>%s</p>' % http_check(service)
    page += '</center>'
    page += '</body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))