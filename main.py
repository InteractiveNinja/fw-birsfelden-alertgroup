from fastapi import FastAPI
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from config import APP_URL,APP_SEARCH_QUERY
app = FastAPI()


@app.get("/status")
def read_root():
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.get("/config")
def read_root():
    return APP_URL + " " + APP_SEARCH_QUERY