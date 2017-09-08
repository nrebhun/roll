#!/usr/bin/env python
from chalice import Chalice, Response
from chalicelib import roll
import urlparse, json

app = Chalice(app_name='roll')
app.debug = True

SLACK_TOKEN="<REDACTED>"

@app.route('/', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def handle_slack():
    data = urlparse.parse_qs(app.current_request.raw_body)
    print data

    body = {}
    body['success'] = False
    body['error'] = 'Bad Request'

    response_code = 400

    headers = {'Content-Type': 'application/json'}

    try:
        if data['token'][0] == SLACK_TOKEN:
            body['success'] = True
            body['error'] = ''
            body['text'] = roll.parse_shorthand(str(data['text'][0]))
            response_code = 200
        else:
            body['error'] = 'Unauthorized'
            response_code = 401

    except Exception as e:
        print str(e)
    finally:
        return Response(body=body, status_code=response_code, headers=headers)