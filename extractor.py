import datetime
import re
from datetime import datetime, time
from urllib.request import urlopen

from config import APP_SEARCH_QUERY, APP_URL


class Extractor:
    def __init__(self):
        self.__cache = None
        self.__timestamp = None

    def get_alarm_group(self):
        if self.__cache is None or isinstance(self.__timestamp,
                                              datetime) and self.__timestamp < self.__get_next_midnight():
            self.__cache = self.__extract_alarm_group()
            self.__timestamp = datetime.now()

        return {"message":self.__cache,"timestamp": self.__timestamp}

    def __extract_alarm_group(self):
        site = self.__fetch_site()
        alarm_group_texts = re.findall(APP_SEARCH_QUERY, site)
        try:
            alarm_group = next(x for x in alarm_group_texts)
        except Exception as _:
            raise Exception("Alarm Group Element not found")
        return alarm_group

    def __fetch_site(self):
        return str(urlopen(APP_URL).read())

    def __get_next_midnight(self):
        return datetime.combine(datetime.now(), time.min)
