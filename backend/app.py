from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    df = pd.read_csv(file)
    total = df['Amount'].sum()
    groceries = df[df['Category'] == 'Groceries']['Amount'].sum()
    prediction = groceries * 0.85
    return jsonify({
        'total_spent': total,
        'groceries': groceries,
        'recommendation': f'Reduce groceries by 15%: ${prediction:.2f}'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
