from fastapi import FastAPI
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from extractor import Extractor

app = FastAPI()


extractor = Extractor()

@app.get("/status")
def read_root():
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.get("/")
def get_alarm_group():
    alarm_group = extractor.get_alarm_group()
    return alarm_group
