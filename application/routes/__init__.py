from flask import Flask

app = Flask(__name__)

import application.routes.option_routes
