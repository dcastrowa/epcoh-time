from flask import Flask
import calendar
import time
import os

app = Flask(__name__)


@app.route('/')
def epoch_time_now():
    return str(calendar.timegm(time.gmtime()))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
