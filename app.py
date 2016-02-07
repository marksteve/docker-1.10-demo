import os

from db import get_items, record_item, rollback
from flask import abort, Blueprint, Flask, jsonify, request
from rq import Queue
from rq.cli.helpers import get_redis_from_config

q = Queue(connection=get_redis_from_config(os.environ))
root = Blueprint('root', __name__)


@root.route('/')
def index():
  return "Hello, world"


@root.route('/items', methods=['GET', 'POST'])
def items():
  if request.method == 'GET':
    return jsonify({'items': get_items()})
  elif request.method == 'POST':
    q.enqueue(record_item, request.get_json())
    return jsonify({'ok': True})
  else:
    abort(405)


@root.teardown_request
def rollback_on_exception(exc):
  if exc:
    rollback()
  return exc


def create_app():
  app = Flask(__name__)
  app.config['PROPAGATE_EXCEPTIONS'] = True
  app.register_blueprint(root)
  return app

