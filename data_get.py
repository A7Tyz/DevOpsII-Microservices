from flask import Flask, request, jsonify
import datetime
import data_items as us

app = Flask(__name__)

@app.route('/items/get', methods=['GET'])
def items():
    halo = us.halo_items_name()
    return jsonify(halo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1