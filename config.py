from os import environ

APP_URL = environ.get("APP_URL")
APP_SEARCH_QUERY = environ.get("APP_SEARCH_QUERY")

if APP_URL is None or APP_SEARCH_QUERY is None:
    raise Exception("Config initialization failed check APP_URL and APP_SEARCH_QUERY")
