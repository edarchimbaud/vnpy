from time import sleep

from vnpy.event import EventEngine, Event
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.trader.event import EVENT_LOG

from vnpy_ctp import CtpGateway
from vnpy_rpcservice import RpcServiceApp
from vnpy_rpcservice.rpc_service.engine import EVENT_RPC_LOG


def main_ui():
    """"""
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(RpcServiceApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


def process_log_event(event: Event):
    """"""
    log = event.data
    msg = f"{log.time}\t{log.msg}"
    print(msg)


def main_terminal():
    """"""
    event_engine = EventEngine()
    event_engine.register(EVENT_LOG, process_log_event)
    event_engine.register(EVENT_RPC_LOG, process_log_event)

    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)
    rpc_engine = main_engine.add_app(RpcServiceApp)

    setting = {
        "Username": "",
        "Password": "",
        "Broker's code": "9999",
        "Trade server": "180.168.146.187:10101",
        "Quotes server": "180.168.146.187:10111",
        "Product name": "simnow_client_test",
        "Authorization code": "0000000000000000",
        "Product information": ""
    }
    main_engine.connect(setting, "CTP")
    sleep(10)

    rep_address = "tcp://127.0.0.1:2014"
    pub_address = "tcp://127.0.0.1:4102"
    rpc_engine.start(rep_address, pub_address)

    while True:
        sleep(1)


if __name__ == "__main__":
    # Run in GUI mode
    # main_ui()

    # Run in CLI mode
    main_terminal()
