from flask import Flask, request, jsonify
import datetime
import data_items as us

app = Flask(__name__)
@app.route('/items/delete', methods=['DELETE'])
def delete():
    try:
        name = request.form.get('name')
        halo = us.find_halo_items_name(name)
        if halo:
            us.halo_items_delete(name)
            return jsonify({'message': 'Delete Successful.'}), 200
        else:
            return jsonify({'message': 'Cannot Delete.'}), 401
    except:
        return jsonify({'message': 'Cannot found items.'}), 401
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)