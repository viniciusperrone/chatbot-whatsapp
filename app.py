from flask import Flask, request, jsonify
from services.waha import Waha

app = Flask(__name__)

@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json

    print(f'DE QUEM: {data}')

    print(data['payload']['from'])

    waha = Waha()

    waha.send_message(
        chat_id=data['payload']['from'],
        message=data["payload"]["body"]
    )

    return jsonify({ 'status': 'success'}), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)