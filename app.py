from flask import Flask, request, Response, jsonify
import requests
from datetime import date, timedelta
import json
import random


def get_random_quote():
    """ Returns random quote from quotes file"""

    with open('quotes.json', 'r') as quotes:
        bobbyb_quotes = json.load(quotes)
    
    return random.choice(bobbyb_quotes)



app = Flask(__name__)
@app.route('/bobbyb', methods=['POST'])
def lunch():
    text = request.form.get('text', '')
    if 'sup?' in text.lower(): #and get_random_quote() not in text:
        return {"text": f"{get_random_quote()}"}  # DYI JSON
    if 'bobby' in text.lower(): #and get_random_quote() not in text:
        return {"text": f"{get_random_quote()}"}  # DYI JSON
    return Response(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
