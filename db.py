import os

import records

db = records.Database('postgres://postgres:{}@postgres/{}'.format(
  os.environ['POSTGRES_PASSWORD'],
  os.environ['POSTGRES_DB'],
))


def record_item(item):
  db.query(
    'insert into items (item) values (%s)',
    params=[item],
  )
  db.db.commit()


def get_items():
  return db.query('select * from items').all()


def rollback():
  db.db.rollback()
