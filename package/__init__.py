from flask_api import FlaskAPI
from flask_cors import CORS
import logging

app = FlaskAPI("cover-rest")
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# create logger
logging_time = logging.getLogger("main")
logging_time.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(threadName)s: %(message)s',
    "%Y-%m-%d %H:%M:%S"))
logging.root.handlers = [handler]

from package import routes
