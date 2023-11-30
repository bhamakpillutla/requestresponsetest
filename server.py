from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)

@app.route('/')
def hello():
    response = {
            'message': 'Hello, world!',
            'status': 'success'
            }
    # time.sleep(2) # Simulate a 2-second delay
    # app.logger.warning('A warning occurred')
    # app.logger.error('An error occurred')
    # app.logger.info('Info')
    # Intentionally generate bad responses
    response['message']= 'Internal Server Error'
    response['status'] = 'error'
    return jsonify(response), 500

if __name__=='__main__':
    # time.sleep(120)
    # # logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.INFO)
    app.run(debug=False,host='0.0.0.0', port = 7000)
