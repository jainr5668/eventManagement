import os
from threading import Thread


def runEws():
    os.system("cd ews && npx ng serve")


def runFastApi():
    os.system("cd fastApi && python -m uvicorn main:app --reload")


Thread(target=runEws).start()
Thread(target=runFastApi).start()
