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
    app.logger.info(response*20)
    # time.sleep(2) # Simulate a 2-second delay

    # Intentionally generate bad responses
    response['message']= 'Internal Server Error'
    response['status'] = 'error'
    return jsonify(response), 500

if __name__=='__main__':
    # time.sleep(120)
    logging.basicConfig(level=logging.INFO)
    print("Server running...")
    app.run(debug=True,host='0.0.0.0', port = 7000)
