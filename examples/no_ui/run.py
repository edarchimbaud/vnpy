import multiprocessing
import sys
from time import sleep
from datetime import datetime, time
from logging import INFO

from vnpy.event import EventEngine
from vnpy.trader.setting import SETTINGS
from vnpy.trader.engine import MainEngine

from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctastrategy.base import EVENT_CTA_LOG


SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True


ctp_setting = {
    "Username": "",
    "Password": "",
    "Broker's code": "",
    "Trade server": "",
    "Quotes server": "",
    "Product name": "",
    "Authorization code": "",
    "Product information": ""
}


# Chinese futures market trading period (day/night)
DAY_START = time(8, 45)
DAY_END = time(15, 0)

NIGHT_START = time(20, 45)
NIGHT_END = time(2, 45)


def check_trading_period():
    """"""
    current_time = datetime.now().time()

    trading = False
    if (
        (current_time >= DAY_START and current_time <= DAY_END)
        or (current_time >= NIGHT_START)
        or (current_time <= NIGHT_END)
    ):
        trading = True

    return trading


def run_child():
    """
    Running in the child process.
    """
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)
    cta_engine = main_engine.add_app(CtaStrategyApp)
    main_engine.write_log("Main engine created successfully")

    log_engine = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("Register log event listener")

    main_engine.connect(ctp_setting, "CTP")
    main_engine.write_log("Connecting CTP interface")

    sleep(10)

    cta_engine.init_engine()
    main_engine.write_log("CTA strategy initialization complete")

    cta_engine.init_all_strategies()
    sleep(60)   # Leave enough time to complete strategy initialization
    main_engine.write_log("CTA strategy all initialized")

    cta_engine.start_all_strategies()
    main_engine.write_log("CTA strategies all started")

    while True:
        sleep(10)

        trading = check_trading_period()
        if not trading:
            print("Shutting down child processes")
            main_engine.close()
            sys.exit(0)


def run_parent():
    """
    Running in the parent process.
    """
    print("Starting CTA strategy daemon parent process")

    child_process = None

    while True:
        trading = check_trading_period()

        # Start child process in trading period
        if trading and child_process is None:
            print("Starting sub-processes")
            child_process = multiprocessing.Process(target=run_child)
            child_process.start()
            print("Child process started successfully")

        # Exit sub-processes at non-recorded times
        if not trading and child_process is not None:
            if not child_process.is_alive():
                child_process = None
                print("Child process shutdown successful")

        sleep(5)


if __name__ == "__main__":
    run_parent()
