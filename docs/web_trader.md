# WebTrader - Web Server Module

## Functional Description

WebTrader is a functional module for **Web Application Backend Service** that allows users to run and manage VeighNa quantitative strategy trades via a browser (not the PyQt desktop).

## Architecture Design

WebTrader uses FastAPI as the backend server, supports REST active request calls and WebSocket passive data push, the overall runtime framework diagram is as follows:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_1.png)

The backend service consists of two separate processes:
- Strategy Trading Process
  - The process running VeighNa Trader is responsible for all strategy trading functions;
  - The RpcServer is started for function calls to the Web service process;
- Web service process
  - Running the FastAPI process, which is responsible for providing external Web access services;
  - RpcClient is started for calling the functions of the strategy trading process.

The two-way communication mode from the web side to the strategy trading process includes:
- unsolicited calls (subscribe to quotes, pending withdrawal orders, query data)
  - The browser initiates a REST API call (accessing a URL address to submit data) to the web service process;
  - Web service process received, converted to RPC requests (Req-Rep communication mode) sent to the strategy trading process;
  - The strategy transaction process executes the request and returns the result to the Web service process;
  - Web service process returns data to the browser.
- Passive data push (quote push, commission push)
  - The browser initiates a Websocket connection to the Web service process;
  - The strategy trading process pushes the data to the Web service process through RPC push (Pub-Sub communication);
  - The Web service process receives and pushes the data to the browser in real time (JSON format) via Websocket API.

## Load startup

### Loading VeighNa Station

After starting to log in VeighNa Station, click the [Trading] button and check [WebTrader] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_webtrader import WebTraderApp

# Write after creating the main_engine object
main_engine.add_app(WebTraderApp)
```

### Start the module

Before starting the module, please connect to the login trading interface (see the Connecting to the Interface section of the Basic Usage chapter for details on how to connect). Start the module after you see "Contract Information Query Successful" in the [Log] column of VeighNa Trader main interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/market_radar/1.png)

After successfully connecting to the trading interface, click [Functions] -> [Web Services] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_0.png)

You can enter the UI interface of RPC service module, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_3.png)

At this time, only the strategy transaction process is running in the system, and the server configuration options in the upper left area include:
- User name and password: the user name and password used when logging into the web application from the web side, when using it, please modify it to the user name and password you want to use (through the startup directory.vntrader under the web_trader_setting.json to modify it), please note that the user name and password here have nothing to do with the underlying trading interface;
- Request and subscription address: the address for RPC communication between the web service process and the strategy trading process in the architecture diagram, just be careful that the port does not conflict with other programs.

After clicking the Start button, the Web service process will be started in the system background according to the configuration information input by the user, and the log information related to the running process of Fast API will be output in the right area at the same time.


## Interface Demo

After starting the web service, open the URL <http://127.0.0.1:8000/docs> in the browser, you can see the interface documentation page as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_2.png)

Here contains relevant interface information currently supported by WebTrader, the following combines with the [Jupyter Notebook](https://github.com/vnpy/vnpy_webtrader/blob/main/script/test. ipynb).

### Getting a token

```python 3
import requests
import json

url = "http://127.0.0.1:8000/"
username = "vnpy"
password = "vnpy"

r = requests.post(
    url + "token", data={"username": username, "password": password}, "password": vnpy
    data={"username": username, "password": password},
    headers={"accept": "application/json"}
)
token = r.json()["access_token"]
```

First of all, import the corresponding module requests and json, then define the url and username and password, through the requests of the post method to pass the appropriate parameters will be able to obtain the token (token), subsequent access to use a variety of interfaces directly into the token can be.

### Quote subscription

```python 3
r = requests.post(url + "tick/" + "cu2112.SHFE", headers={"Authorization": "Bearer " + token})
```

With the above command, you can subscribe to the contract cu2112.SHFE and at the same time, you can receive the contract's tick data push in the graphical interface, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_4.png)

### Batch query

```python 3
### Query function
def query_test(name).
    """Query the corresponding type of data""""
    r = requests.get(
        url + name,
        headers={"Authorization": "Bearer " + token}
    )
    return r.json()

# Batch query
for name in ["tick", "contract", "account", "position", "order", "trade"].
    data = query_test(name)
    print(name + "-" * 20)
    print(name + "-" * 20) if data.
        print(data[0])
```

If necessary, you can also send unsolicited requests to query related data, such as tick data, contract data, account data, position data, order data, and transaction data.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_5.png)

### Delegation test

```python 3
### Delegation test
req = {
    "symbol": "cu2112",
    "exchange": "SHFE",
    "direction": "multiple",
    "type": "Limit", "volume": 1, "type": "SHFE", "direction": "Multi", "type": "Limit", "volume": 1, "volume": 1
    "volume": 1, "price": 71030
    "price": 71030, "offset": "open", "price": 71030, "price": 71030
    "offset": "on", "reference": "WebTraffic", "reference": "WebTraffic": "WebTraffic": "WebTraffic".
    "reference": "WebTrader"
}

r = requests.post(
    url + "order",
    json=req,
    headers={"Authorization": "Bearer " + token}
)
vt_orderid = r.json()

print(vt_orderid)
```

After placing an order you can also see the delegation information in the graphical interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_6.png)

### Withdrawal test

```python 3
### Withdrawal test
r = requests.delete(
    url + "order/" + vt_orderid,
    headers={"Authorization": "Bearer " + token}
)
```

If you want to undo a previously placed delegation, you can send an unsolicited request, and the result will be updated in the GUI as well, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_7.png)

### Websocket test

```python 3
## Weboscket test
from websocket import create_connection

ws = create_connection("ws://127.0.0.1:8000/ws/?token=" + token)

while True: result = ws.recv()
    result = ws.recv()
    print("Received '%s'" % result)

ws.close()
```

Websocket can be used to passively receive quotes, commissions, etc. pushed by the strategy trading process, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/web_trader/web_trader_8.png)

## Follow-up plan

WebTrader only implements the back-end of the web application (providing an interface for the browser to access the data), while the front-end page (i.e. the web page seen in the browser) is left to the community users to implement according to the previous plan, and you are welcome to contribute code.

Meanwhile, WebTrader only supports basic manual trading functions, and will gradually add the management functions related to strategy trading applications (such as CtaStrategy related calls).
