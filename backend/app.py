from flask import Flask, request, jsonify
import pandas as pd
from ml_model import predict_expenses

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_excel(file)
    result = predict_expenses(df)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
