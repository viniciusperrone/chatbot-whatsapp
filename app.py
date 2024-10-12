from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json()

    print(f'EVENTO RECEBIDO: {data}')

    return jsonify({ 'status': 'success'}), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)