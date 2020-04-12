import threading
import time
from datetime import datetime
import requests
from threading import Thread

from urllib3.exceptions import NewConnectionError

from Config import Config


def get_content():
    config = Config("appsettings.json")
    headers = {'Authorization': '{}'.format(config.token_track_link)}
    try:
        response = requests.get(config.url_backend_track_link, headers)
        print(response.content, datetime.now())
        time.sleep(0.5)
    except ConnectionError:
        print("Ocurrió un problema de conexión")
    except Exception:
        print("Ocurrió un error inesperado")


def execute():
    threading.Timer(5.0, execute).start()
    tasks = []
    print("***********************************************")
    for i in range(5):
        task = Thread(target=get_content)
        tasks.append(task)
        task.start()


execute()
