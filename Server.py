from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
from INTELLIGENT_ENGINE.lstm_test import cropRecommend
app = Flask(__name__)
CORS(app)   



@app.route('/form',methods=['POST'])
def index():
    send=request.get_json()
    Predicted_JSON=cropRecommend(send)
    print(Predicted_JSON)
    return jsonify(Predicted_JSON)

if __name__ == "__main__":

    app.run(debug=True)





    