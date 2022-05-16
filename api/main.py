
from flask import Flask, jsonify, request, Response
import logging

from repository import all_notices, create_notice, find_notice_by_title
from utils import format_date


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def get_notices():
    try:
        notices = all_notices()
    except Exception as e:
        app.logger.error(f"Connection failed... {e}")
        return Response(
            response=f"Connection failed: {e}",
            status=500,
        )

    return jsonify(notices=notices)

@app.route('/', methods=['POST'])
def save_notices():
    notices = request.json
    for notice in notices:
        if len(find_notice_by_title(notice['title'])):
            app.logger.info(f"{notice['title']} já existe")
            continue
        
        notice['date'] = format_date(notice['date'])
        try:
            create_notice(notice)
        except Exception as e:
            return Response(
                response=f"Connection failed: {e}",
                status=500,
            )
        
    return Response(
        status=201
    )