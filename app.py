import os
from flask import Flask
from flask_cache import Cache
from states import http_check, SERVICES

app = Flask(__name__)

cache = Cache(app,config={'CACHE_TYPE': 'simple'})



@app.route("/")
@cache.cached(timeout=50)
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