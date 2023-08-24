# ScriptTrader - Script Strategy Trading Module

## Functionality Overview

ScriptTrader is a functional module for **script strategy trading** that provides interactive quantitative analysis and programmatic trading functionality, as well as script strategy functionality that runs continuously with the entire strategy.

Therefore, it can be regarded as the direct use of Python to operate the trading client. It is different from the CTA strategy module:

- Breaking through the single exchange, a single subject of the limitations;
- Can be more convenient to realize such as stock index futures and a basket of stocks between the hedging strategy, cross-species arbitrage, stock market scanning automated stock selection and other functions.

## Load and start

### Loading VeighNa Station

After logging into VeighNa Station, click the [Trading] button and check [ScriptTrader] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_scripttrader import ScriptTraderApp

# Write after creating the main_engine object
main_engine.add_app(ScriptTraderApp)
```

## Start the module

Before starting the module, please connect to the trading interface (see the Connecting to the Interface section of the Basic Usage chapter for details on how to do this). Start the module after you see "Contract Information Query Successful" in the [Log] column of VeighNa Trader main interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not get all contract information automatically when you log in, but only when you subscribe to the market manually. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

After successfully connecting to the trading interface, click [Functions] -> [Script Strategy] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/0.png)

You can enter the UI interface of the script trading module, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/1.png)

If you have configured the data service (please refer to the Global Configuration section of the Basic Usage chapter for details), the data service login initialization will be executed automatically when you open the Script Trading Module. If the login is successful, the log of "Data service initialization successful" will be output, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/20.png)

Users can use the following functions through the UI interface:

### Startup

The script strategy requires a pre-written script strategy file, such as test_strategy.py (the script strategy template can be found in the [**Script Strategy**](#jump) section), so after clicking the [Open] button, you need to specify the path to the script strategy file, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/21.png)

After opening the script strategy, clicking the [Start] button will start the script strategy and output the related information in the following interface, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/8.png)

### Stop

If you want to stop the script strategy, click the [Stop] button, the strategy will be stopped, and the notification will output the log of "Strategy Trading Script Stopped" in the lower screen, as shown in the following figure:

The notification will output the "Strategy Trading Script Stopped" log as shown in the following figure: ![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/11.png)

### Clear

If you think there is too much information in the lower screen, or you want to open a new script strategy, you can click the [Empty] button, then all the information in the lower screen will be emptied, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/10.png)


## Script strategy template

<span id="jump">

Script strategy file writing need to follow a certain format, the following provides the use of the template, its role is:

- Subscribe to two varieties of quotes;
- Print contract information;
- Get the latest quotes every 3 seconds.

```python 3
from time import sleep
from vnpy_scripttrader import ScriptEngine

def run(engine: ScriptEngine):
    """"""
    vt_symbols = ["sc2209.INE", "sc2203.INE"]

    # Subscribe to the ticker
    engine.subscribe(vt_symbols)

    # Get contract information
    for vt_symbol in vt_symbols.
        contract = engine.get_contract(vt_symbol)
        msg = f "Contract information, {contract}"
        engine.write_log(msg)

    # Run continuously, using strategy_active to determine if you want to exit the program.
    while engine.strategy_active: # Poll for quotes.
        # Poll for quotes
        for vt_symbol in vt_symbols: # Poll for tick = engine.get_tick = engine.
            tick = engine.get_tick(vt_symbol)
            msg = f "Latest tick, {tick}"
            engine.write_log(msg)

        # Wait 3 seconds for the next round
        sleep(3)
```

Where engine.strategy_active is used to control the While loop, which can be thought of as a script strategy switch:

- Click the [Start] button to start the While loop and execute the script strategy;
- Click the [Stop] button to exit the While loop and stop the script strategy.


## Function Functions

Jupyter mode is based on the script engine (ScriptEngine) driven, the following through the jupyter notebook to illustrate the ScriptEngine engine function.

First open Jupyter notebook, then load the components, initialize the script engine:

```python 3
from vnpy_scripttrader import init_cli_trading
from vnpy_ctp import CtpGateway
engine = init_cli_trading([CtpGateway])
```

Among other things:

- The scripting engine can support connecting to multiple interfaces at the same time;
- init_cli_trading(gateways: Sequence[BaseGateway]) can pass multiple interface classes, as a list, to init_cli_trading;
- init_cli_trading can be regarded as a vnpy-sealed initialization startup function that encapsulates various objects such as the main engine, script engine, and so on.

### Connection interface

**connect_gateway**

* Input: setting: dict, gateway_name: str
* Output: none

Different interfaces require different configuration parameters, SimNow's configuration is as follows:
```json
setting = {
    "username": "xxxx",
    "Password": "xxxx",
    "BrokerCode": "9999",
    
    
    "Product Name": "simnow_client_test",
    "Authorization Code": "0000000000000000"
}
engine.connect_gateway(setting, "CTP")
```

Other interface configurations can be filled out by referring to default_setting in the different interface module classes (e.g. vnpy_ctp.gateway.ctp_gateway) in the site-packages directory.

### Subscribe to quotes

**subscribe**

* Input: vt_symbols: Sequence[str]
* Output: none

The subscribe() function is used to subscribe to ticker information, if you need to subscribe to a basket of contracts, you can use the list format.

```python 3
engine.subscribe(vt_symbols = ["rb2209.SHFE", "rb2210.SHFE"])
```

### Querying data
Here is a description of the data storage after connecting to the upper trading interface and successfully subscribing to the data:

- The underlying interface keeps pushing new data to the main engine;
- The main engine maintains a ticks dictionary to cache the latest tick data of different targets (only the latest data can be cached);
- The role of use_df is to convert to DataFrame format for data analysis.

#### Single query

**get_tick**

* Input: vt_symbol: str, use_df: bool = False
* Output: TickData

Query the latest tick of a single label, use_df is an optional parameter, used to transform the returned class object into DataFrame format for easy data analysis.

``` python 3
tick = engine.get_tick(vt_symbol="rb2210.SHFE",use_df=False)
```

Among them:

- vt_symbol: is the local contract code, the format is contract variety + exchange, such as rb2210.SHFE;
- use_df: is a bool variable, default False, return TickData class object, otherwise return the corresponding DataFrame, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/13.png)

**get_order**

* Input: vt_orderid: str, use_df: bool = False
* Output parameter: OrderData

Queries the details of a delegated order based on vt_orderid.

``` python 3
order = engine.get_order(vt_orderid="CTP.3_-1795780178_1",use_df=False)
```

Where vt_orderid is the local delegate number (the vt_orderid of the delegate is automatically returned when the delegate places an order).
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/14.png)

**get_contract**

* Input: vt_symbol, use_df: bool = False
* Output parameter: contractData

Queries the details of the corresponding contract object based on the local vt_symbol.

```python 3
contract = engine.get_contract(vt_symbol="rb2210.SHFE",use_df=False)
```

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/15.png)

**get_account**

* Input: vt_accountid: str, use_df: bool = False
* Outgoing reference: AccountData

Query the corresponding fund information based on the local vt_accountid.

```python 3
account = engine.get_account(vt_accountid="CTP.189672",use_df=False)
```
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/16.png)

**get_position**

* Input: vt_positionid: str, use_df: bool = False
* Output: PositionData

Query position based on vt_positionid, return object contains interface name, exchange, contract code, quantity, frozen quantity, etc.

``` python 3
position = engine.get_position(vt_positionid='CTP.hc2305.SHFE.multi')
```

Note that vt_positionid is a unique position number within vnpy for a particular position in the format "gateway_name.vt_symbol.Direction.value", where the position direction can be "long", "Short" and "Net", as shown below:
The following chart shows the position direction. [](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/17.png)

#### Multi Query

**get_ticks**

* Input: vt_symbols: Sequence[str], use_df: bool = False
* Output: Sequence[TickData]

Query the latest tick for multiple contracts.

```python 3
ticks = engine.get_ticks(vt_symbols=['rb2209.SHFE','rb2210.SHFE'],use_df=True)
```

vt_symbols is the list format, which contains multiple vt_symbols as shown.
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/18.png)


**get_orders**

* Input: vt_orderids: Sequence[str], use_df: bool = False
* Output: Sequence[OrderData]

Queries the details of multiple vt_orderid based on a query for them. vt_orderids is a list containing multiple vt_orderid.

```python 3
orders = engine.get_orders([orderid_one,orderid_two],use_df=True)
```

**get_trades**

* Input: vt_orderid: str, use_df: bool = False
* Output: Sequence[TradeData]

Returns all TradeData objects for this order process based on a given vt_orderid. vt_orderid is the local commission number, and each commission OrderData, due to the partial transaction relationship, can correspond to multiple transaction TradeData.

``` python 3
trades = engine.get_trades(vt_orderid=your_vt_orderid,use_df=True)
```

**get_bars**

* Input: vt_symbol: str, start_date: str, interval: Interval, use_df: bool = False
* Output: Sequence[BarData]

Queries historical data through the configured data service.

```python 3
bars = engine.get_bars(vt_symbol="rb2210.SHFE",start_date="20211201",
                        interval=Interval.MINUTE,use_df=False)
```

Among them:

- vt_symbol: local contract code in the format of contract code + exchange name;
- start_date: start date, in the format of "%Y%%m%d";
- interval: bar period, including: minutes, hours, days, weeks;
- bars: a list object containing a series of BarData data with the following BarData definition:

```python 3
@dataclass
class BarData(BaseData).

    symbol: str
    exchange: exchange
    datetime: datetime

    interval: Interval = None
    volume: float = 0
    turnover: float = 0
    open_interest: float = 0
    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0

    def __post_init__(self).
        self.vt_symbol = f"{self.symbol}. {self.exchange.value}"
```

#### Full-volume queries

In a full query, the only parameter is use_df, which defaults to False. what is returned is a List object containing the appropriate data, such as ContractData, AccountData, and PositionData.

**get_all_contracts**

* Input: use_df: bool = False
* Output: Sequence[ContractData].

Returns a list with market-wide ContractData by default, or the corresponding DataFrame if use_df = True.

**get_all_active_orders**

* Input: use_df: bool = False
* Output: sequence[OrderData]

Active orders means waiting for the order to be completely filled, so its status contains "submitted, not submitted, partially filled"; the function will return a list object containing a series of OrderData.

**get_all_accounts**

* Input: use_df: bool = False
* Output: Sequence[AccountData]

Returns the list object containing AccountData by default.

**get_all_positions**

* Input: use_df: bool = False
* Output: Sequence[PositionData]

Returns the list object containing PositionData by default, as shown below:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/script_trader/19.png)

### Trading Delegates

**buy**: buy to open position (Direction: LONG, Offset: OPEN)

**sell**: sell to close position (Direction: SHORT, Offset: CLOSE)

**short**: Sell to open position (Direction: SHORT, Offset: OPEN)

**cover**: buy to close position (Direction: LONG, Offset: CLOSE)

* Input: vt_symbol: str, price: float, volume: float, order_type: OrderType = OrderType.LIMIT
* Output: str

Take the commission buy as an example, the engine.buy() function in-parameters include:

- vt_symbol: local contract code (string format);
- price: the price of the order (floating-point type);; volume: the number of orders (floating-point type).
- volume: the number of orders (floating-point number type).
- order_type: OrderType enumeration constants, the default for the limit single (OrderType.LIMIT), while supporting the stop single (OrderType.STOP), FAK (OrderType.FAK), FOK (OrderType.FOK), the market price of the single (OrderType.MARKET), different exchanges. MARKET), different exchanges support order reporting methods are not exactly the same.

```python 3
engine.buy(vt_symbol="rb2210.SHFE", price=4200, volume=1, order_type=OrderType.LIMIT)
```

The local order number vt_orderid is returned after executing the trade order.

**send_order**

* Input: vt_symbol: str, price: float, volume: float, direction: Direction, offset: Offset, order_type: OrderType
* Output: str

The send_order function is a function called by the script trading strategy engine to send an order. Generally do not need to be called separately when the strategy is written, through the buy/sell/short/cover function to send the commission can be.

**cancel_order**

* Input: vt_orderid: str
* Output: none 

Revoke a delegation based on the local delegation number.

```python 3
engine.cancel_order(vt_orderid='CTP.3_-1795780178_1')
```

### Information output

**write_log**

* Input parameter: msg: str
* Outgoing parameter: none

Call the write_log function in a strategy to perform log output with the specified content.

**send_email**

* Input: msg: str
* Output: none

After configuring mailbox information (see Global Configuration section in Basic Usage), call send_email function to send an email with the title "Scripting Policy Engine Notification" to your mailbox.
