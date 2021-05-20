import json
from psycopg2.extras import RealDictCursor
from datetime import date
import decimal

class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()
        elif isinstance(o, decimal.Decimal):
            return str(o)
        return super(Encoder, self).default(o)