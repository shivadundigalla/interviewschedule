from flask import Flask, jsonify, request,render_template
from flask_jwt_extended import (
JWTManager, jwt_required, create_access_token,
get_jwt_identity
)
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)
# Provide a method to create access tokens. The create_access_token()
# function is used to actually generate the token, and you can return
# it to the caller however you choose.
@app.route('/')
def inde():
    return render_template("jwtlogin.html")
@app.route('/login', methods=["GET",'POST'])
def login():
    data=request.json
    username =data['username']
    password = data['password']
    if not username:
        return jsonify({"msg": "Missing username parameter","access_token":"access_token"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter","access_token":"access_token"}), 400
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password","access_token":"access_token"}), 401
# Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    print(access_token)
    #return render_template("files.html", pending="", reported="", fixed="")
    return jsonify({"msg": "Missing username parameter","access_token":access_token}), 200
# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/file', methods=['GET'])
@jwt_required
def protected():
# Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return render_template("files.html", pending="", reported="", fixed="")
    #return jsonify(logged_in_as=current_user), 200
if __name__ == '__main__':
    app.run()
