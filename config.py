import os
from os import getenv

class Config(object):
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      BOT_ID = os.environ.get("BOT_TOKEN", "")
      COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
