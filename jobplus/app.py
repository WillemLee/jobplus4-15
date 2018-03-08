# -*- coding: utf-8 -*-
"""app.py
项目app配置
"""

from flask import Flask,render_template
from flask_migrate import Migrate
from jobplus.config import configs
from jobplus.models import db, User
from flask_login import LoginManager


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app

def register_blueprints(app):
	from .handlers import front
	app.register_blueprint(front)