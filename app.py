import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '510623477:AAEjEtCeCohX8B0N5PbqMRX9ixYkHlOciP0'
WEBHOOK_URL = 'https://bc79b51b.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'choose',
        'breakfast',
        'lunch',
        'dinner',
        'satisfied',
        'search',
        'recommend'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'choose',
        },
        {
            'trigger': 'advance',
            'source': 'choose',
            'dest': 'breakfast',
            'conditions': 'is_going_to_breakfast'
        },
        {
            'trigger': 'advance',
            'source': 'choose',
            'dest': 'lunch',
            'conditions': 'is_going_to_lunch'
        },
        {
            'trigger': 'advance',
            'source': 'choose',
            'dest': 'dinner',
            'conditions': 'is_going_to_dinner'
        },
        {
            'trigger': 'advance',
            'source': [
                'choose',
                'breakfast',
                'lunch',
                'dinner'
            ],
            'dest': 'satisfied',
            'conditions': 'is_going_to_satisfied'
        },
        {
            'trigger': 'advance',
            'source': 'satisfied',
            'dest': 'recommend' ,
            'conditions': 'is_going_to_recommend'
        },
        {
            'trigger': 'advance',
            'source': 'satisfied',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'satisfied',
            'dest': 'choose',
            'conditions': 'is_going_to_choose'
        },
        {
            'trigger': 'go_back',
            'source': [
                'search',
                'recommend'
            ],
            'dest': 'choose',
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
