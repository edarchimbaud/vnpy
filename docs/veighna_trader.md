# VeighNa Trader

## Start the program

### Graphical mode

After launching and logging into VeighNa Station, users can enter VeighNa Trader by clicking on the [Trading] button, checking the desired trading interface and application module, and clicking on the [Launch] button, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/22.png)

### Script Mode

Find the run.py file in the folder examples/vn_trader (not under veighna_studio, you need to download the source code on github). Run run.py to enter VeighNa Trader.

- Take Win10 system as an example, users can hold down [Shift] in the folder where run.py is located while clicking the right button of the mouse, select [Open powershell window here], in the pop-up window, enter the following command to start VeighNa Trader.

```bash
python run.py
```

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/3.png)

A successfully launched VeighNa Trader is shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/23.png)

## Connecting the interface

### SimNow Simulation

Take the example of using SimNow emulation trading account to login to **CTP** interface, click [System] -> [Connect CTP] in the menu bar on VeighNa Trader, the account configuration window will pop up as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/gateway/1.png)

Among them, the requirements for filling in each field are as follows:
- User name: xxxxxx (6-digit pure numeric account)
- Password: xxxxxxx (you need to change the password once for after-hours testing)
- Brokerage Code: 9999 (SimNow's default brokerage number)
- Trading Server: 180.168.146.187:10202 (for intraday testing)
- Ticker Server: 180.168.146.187:10212 (intraday testing)
- Product Name: simnow_client_test
- Authorization Code: 0000000000000000 (16 zeros)

Please note that the user name should be filled in as InvestorID (6-digit pure number), not the account number (cell phone number) when registering on the Simnow website. In addition, the Simnow registered account needs to change the password once before logging in.

After successful connection, the [Log] component of VeighNa Trader's main interface will immediately output login-related information, and users can also see account information, position information, contract inquiries and other related information. As shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)


## Contract Inquiry

After successfully connecting to the trading interface, users can inquire contract information through the contract inquiry function:
Click [Help] -> [Contract Inquiry] in the menu bar, and in the pop-up dialog box, click the [Inquiry] button at the upper right corner to inquire contract information (leave it blank to inquire price information of all contracts), as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/spread_trading/3.png)

Please note that the IB interface cannot get all the contract information automatically when logging in, but only when the user subscribes to the quotes manually. Therefore, you need to subscribe to the contract quotes manually in the main interface before you can check the contract information.


## Subscribe to quotes

Enter the exchange and contract code in the trading component and press the Enter key to subscribe to the quotes. For example, when subscribing to stock index futures, enter CFFEX as the exchange and IF2206 as the corresponding contract code.

After successful subscription, the trading component will display the contract name and in-depth quotes at the bottom, such as the latest price, buy one price and sell one price, and the quotes component will display the latest quotes, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/24.png)

Please note that **the contract code entered should be the same as the one found in the [Help]->[Check Contracts] function in the menu bar**.


## Entrusted Trades

The trading component is used to manually initiate a commissioned trade. In addition to filling in the exchange and contract code, you also need to fill in the five fields (direction, open/close, type, price and quantity) in the following chart:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/5.png)

Please note that if the commission type is a market order, the commission price may not be filled in; if the trading interface only supports one-way positions (interface position direction support see the chapter on the trading interface), you can not fill in the direction of opening and closing.

After the commission is issued, the information related to the commission will be cached locally and displayed to the [Commission] component and [Activity] component, and the status of the commission at this time will be [Submitted].

After the Exchange receives the commission sent by the user, it will be inserted into the central order book to summarize the transaction and push the commission return to the user:

- If the commission has not yet been filled, the [Commission] component and [Activity] component will only update the time and commission status fields, and the commission status will become [Not Filled];
- If the commission is closed immediately, the information related to the commission will be removed from the [Activity] component and added to the [Closed] component, and the status of the commission will become [All Closed].


## Data Monitoring

Data Monitoring consists of the following components and two auxiliary functions:

Select any of the following components, right mouse button can choose [Adjust Column Width] (especially for the case of low screen resolution) or select [Save Data] (CSV format), as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/12.png)

### Ticker Component

The ticker component is used to monitor the subscribed tickers in real time, as shown in the following figure:

![](https://vnpy-community.oss-cn-shanghai.aliyuncs.com/forum_experience/yazhang/quick_start/subcribe_contract_module.png)

The ticker component monitors the following:

- Contract information: contract code, exchange, contract name;
- Market information: latest price, volume, open price, high price, low price, close price, buy 1 price, buy 1 volume, sell 1 price, sell 1 volume;
- Other information: data push time, interface.

### Activity component

The Active component is used to store commissions that have not yet been executed, such as a limit order or a market order that has not been immediately executed. Double-click on any commission in this component to complete the withdrawal operation, as shown in the figure below:

The active component is used to store commissions that are not yet filled, such as limit orders or market orders that are not immediately filled.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/15.png)

### Transaction Component

In this component, the price, quantity and time are the transaction information pushed by the exchange, not the commission information, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/14.png)

### Mandate component

The commission component is used to store all the commission information issued by the user, and the status of the commission can be submitted, withdrawn, partially filled, fully filled, rejected, etc., as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/13.png)

### Position Component

The Position Component is used to record historical positions and requires attention to the following field information.

- Direction: Futures varieties have a long/short direction, while stock varieties have a [net] position direction;
- Quantity: the total position, i.e. today's position + yesterday's position;
- Yesterday's position: its emergence derives from the need to level today and yesterday's pattern unique to the last futures;
- Average price: the average price of historical transactions (some mega-commissions, multiple partial transactions will occur, the need to calculate the average price);
- Profit and loss: profit and loss of a position. In the case of long positions, profit = current price - average price, and vice versa for short positions.

If you close a position and leave the market, the number of positions is zeroed out, and the floating profit and loss becomes the actual profit and loss, thus affecting the account balance changes. Therefore, the following fields: Quantity, Yesterday's Position, Frozen, Average Price, Profit/Loss are zero, as shown below:

![](https://vnpy-community.oss-cn-shanghai.aliyuncs.com/forum_experience/yazhang/quick_start/query_position.png)


### Funds Component

The Funds component shows the basic information of the account, as shown below:

![](https://vnpy-community.oss-cn-shanghai.aliyuncs.com/forum_experience/yazhang/quick_start/query_account.png)

The following three fields of information need to be noted:

- Available Funds: cash that can be used for the commission
- Freeze: the amount frozen for the commission operation (not the same concept as margin)
- Balance: total funds, i.e., available funds + margin + floating profit and loss.

If all positions are closed, the floating P&L becomes the actual P&L, the margin and floating P&L are cleared to zero, and the total funds are equal to the available funds.

### Log Component

The log component is used to display interface login information and commission error messages, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

## Application Modules

VeighNa officially provides out-of-the-box application modules for quantitative trading. Check the required function modules when starting VeighNa Trader, and click the [Function] button in the menu bar after successful startup to display the checked function modules, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/25.png)


## Global Configuration

Click the [Configuration] button on the menu bar of VeighNa Trader to pop up the [Global Configuration] window, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/20.png)

### GUI interface

The font.family and font.size parameters are used to configure the GUI interface, the meaning of each parameter is shown below:

- font.family: Set the font type of VeighNa Trader GUI, besides the default Arial font, Courier New and System fonts are also supported;

- font.size: set the font size of VeighNa Trader's GUI, users can modify the font size according to the actual resolution of their own monitor.

### Log output

log.active, log.level, log.console and log.file are used to configure the log output, the meaning of each parameter is shown below:

- log.active: control whether to start LogEngine, the default is True, if this parameter is changed to False, the following parameters will be invalidated, and VeighNa Trader will no longer output logs or generate a log file (which can reduce some of the system latency);

- log.level: control the level of log output, the log can be divided into DEBUG, INFO, WARNING, ERROR, CRITICAL from light to serious five levels, corresponding to 10, 20, 30, 40, 50 integer values. If the log level is lower than this setting, it will be ignored. If you want to record more detailed system information, it is recommended to lower the integer value;

- log.console: console refers to the terminal, such as cmd and Powershell on Windows system, and Terminal on Linux system, when set to True, the log information will be output in the terminal if VeighNa Trader is started by running a script through the terminal (which needs to be registered as a log event listener); If VeighNa Trader is started directly through VeighNa Station, there is no console output;

- log.file: this parameter is used to control whether logs should be output to a file or not, it is recommended to set it to True, otherwise the generated logs cannot be recorded.

VeighNa Trader's log file, by default, is located in the .vntrader\log directory of the runtime directory, the full path is:

```
C:\users\administrator\.vntrader\log
```

where administrator is the current Windows system login user name.

### Email notification

Parameters prefixed with email are used to configure mailboxes to send real-time email notifications when specific events occur (e.g., delegated transactions, data anomalies), and the meaning of each parameter is as follows:

- email.server: SMTP mail server address, the default QQ mailbox server address is filled in, you can use it directly, if you need to use other mailboxes, you need to find out the other server address by yourself;
- email.port: SMTP mail server port number, the default QQ mail server port is filled in, you can use it directly;
- email.username: Fill in the e-mail address, 如xxxx@qq.com;
- email.password: for QQ mailbox, this is not the mailbox password, but an authorization code generated by the system after opening SMTP;
- email.sender: send mailbox name, consistent with email.username;
- email.receiver: the e-mail address to receive the e-mail.


### datafeed data service

Similar to the database adapter, there is a standardized interface BaseDatafeed (located in vnpy.trader.datafeed) for data services, which enables more flexible data service support with the following fields:

- datafeed.name: The name of the data service interface, in lower case letters of the full name;
- datafeed.username: the username of the data service;
- datafeed.password: password for the data service.

The fields are shown in the figure:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/quick_start/17.png)

Seven datafeeds are currently supported:
- [RQData]
- [Udata]
- [TuShare]
- [TQSDK]
- [Wind]
- [iFinD]
- [Tinysoft]

[RQData]:https://github.com/vnpy/vnpy_rqdata
[Udata]: https://github.com/vnpy/vnpy_udata
[TuShare]: https://github.com/vnpy/vnpy_tushare
[TQSDK]: https://github.com/vnpy/vnpy_tqsdk
[Wind]:https://github.com/vnpy/vnpy_wind
[iFinD]: https://github.com/vnpy/vnpy_ifind
[Tinysoft]: https://github.com/vnpy/vnpy_tinysoft


### Database

Parameters prefixed with database are used to configure database services. Currently, VeighNa supports eight databases: SQLite, MySQL, PostgreSQL, MongoDB, InfluxDB, DolphinDB, Arctic and LevelDB. See the Database Configuration section of the project documentation for details on how to configure them.
