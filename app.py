#!/usr/bin/env python
import json, os
from urllib.parse import urlparse, parse_qs
from chalice import Chalice, Response
from chalicelib import roll

app = Chalice(app_name='roll')
app.debug = True

@app.route('/', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def handle_slack():
    request_body = app.current_request.raw_body.decode('utf-8')
    data = parse_qs(request_body)

    response_body = {}
    response_body['success'] = False
    response_body['error'] = 'Bad Request'
    response_code = 400
    headers = {'Content-Type': 'application/json'}

    try:
        if data['token'][0] == os.environ['SLACK_TOKEN']:
            response_body['success'] = True
            response_body['error'] = ''
            response_body['text'] = roll.parse_shorthand(data['text'][0])
            response_code = 200
        else:
            response_body['error'] = 'Unauthorized'
            response_code = 401

    except Exception as e:
        print('Error: ' + str(e))
    finally:
        return Response(body=response_body, status_code=response_code, headers=headers)
