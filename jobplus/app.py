# -*- coding: utf-8 -*-
"""app.py
项目app配置
"""

from flask import Flask
from flask_migrate import Migrate
from jobplus.config import configs
from jobplus.models import db, User
from flask_login import LoginManager


def create_app(config):
    app = Flask(__name__)
    # app.config.from_object(configs.get(config))

    return app