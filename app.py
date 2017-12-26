
import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://squiry.in')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)