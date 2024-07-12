from typing import Union

from fastapi import FastAPI
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

app = FastAPI()


@app.get("/status")
def read_root():
    return Response(status_code=HTTP_204_NO_CONTENT)
