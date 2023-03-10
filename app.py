from flask import Flask, request
from logging import basicConfig, INFO
from msg_handlers import PrimaryMsgReceiver


app = Flask(__name__)
msg_receiver = PrimaryMsgReceiver()

basicConfig(level=INFO)


@app.route('/bot', methods=['GET', 'POST'])
def bot_endpoint()-> str:
    """End point for access bot conversation

    Returns:
        str: String who contains request values
    """
    req = request.values
    return str(msg_receiver.receive_new_msg(req))

if __name__ == '__main__':
    app.run(debug=True)