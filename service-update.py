from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update():

    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.find_username(user)
    if _user:
        us.user_name_update(user,passwd,name)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Update unsuccessfully.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1