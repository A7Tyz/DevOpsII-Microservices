from flask import Flask, request, jsonify
import datetime
import data_items as us

app = Flask(__name__)
@app.route('/items/update', methods=['PUT'])
def update():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    halo = us.find_halo_items_name(name)
    if halo:
        us.update_halo_items(name,category,price,instock)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)