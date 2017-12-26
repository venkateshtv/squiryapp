
import os, json
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
	url = 'https://squiry.in/paymentsuccess'
	if(request.form is not None):
		url+='?txnid='+request.form.get('txnid')
	elif request.data is not None:
		url+= '?txnid='+json.loads(request.data.txnid)
		
    return redirect(url)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)