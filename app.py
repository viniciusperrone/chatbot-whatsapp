from flask import Flask, request, jsonify
import time

from services.waha import Waha
from bot.ai_bot import AIBot

app = Flask(__name__)

@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json

    print(f'Event: {data}')

    waha = Waha()
    ai_bot = AIBot()

    chat_id = data['payload']['from']
    received_message = data['payload']['body']

    is_group = '@g.us' in chat_id
    is_status = 'status@broadcast' in chat_id

    if is_group or is_status:
        return jsonify({ 'status': 'success', 'message': 'Mensagem de grupo/status ignorado.'})

    # waha.start_typing(chat_id=chat_id)

    # time.sleep(4)

    # waha.stop_typing(chat_id=chat_id)

    # response = ai_bot.invoke(question=received_message)

    # waha.send_message(
    #     chat_id=chat_id,
    #     message=response
    # )

    return jsonify({ 'status': 'success'}), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)