from flask import Flask, request, jsonify
import datetime
import data_items as us

app = Flask(__name__)

@app.route('/items/post', methods=['POST'])
def register():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    halo = us.halo_items_name()
    data = [x for x in halo if x["name"]==name]

    if (data):
        return jsonify({'message': 'Cannot create item.'}), 401
    else:
        us.halo_name_add(name,category,price,instock)
        return jsonify({'message': 'Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)