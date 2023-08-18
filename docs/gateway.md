# Transaction interface

## Loading startup

### Loading VeighNa Station

After launching and logging in to VeighNa Station, click the [Trading] button and check the interface you want to trade in the [Trading Interface] field in the configuration dialog box.

### Script Loading

Take the CTP interface as an example, add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_ctp import CtpGateway

# Write after creating the main_engine object
main_engine.add_gateway(CtpGateway)
```


## Connecting to the interface

Click [System] -> [Connect CTP] in the menu bar on the graphical operator interface VeighNa Trader, and the account configuration window will pop up as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/gateway/1.png)

Enter the account number, password and other relevant information to connect to the interface, and immediately carry out the query work: such as query account information, query positions, query entrusted information, query transaction information and so on. After successful query, you can see the output log in the component of the main interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/gateway/5.png)

### Modify the json configuration file

The interface configuration related information is saved in a json file, which is placed in the .vntrader folder under the user directory, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/gateway/3.png)

If you need to modify the interface configuration file, you can either modify it in the GUI VeighNa Trader or modify the corresponding json file directly in the .vntrader folder.

Another advantage of separating the json configuration file from the vnpy is that it avoids having to reconfigure the json file for each upgrade.

### View tradable contracts

Login to the interface first, then click [Help] -> [Query Contracts] in the menu bar to bring up a blank [Query Contracts] window, and click the [Query] button to display the query results. If you leave it blank, you can check all the contracts, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/gateway/4.png)


## Interface Classification

| Interface | Type |
| ---------------------| :--------------------------------------------: |
| CTP | Futures, Futures Options (Live 6.5.1) |
| CTP Test | Futures, Futures Options (Test 6.5.1) |
| CTP Mini | Futures, Futures Options (Live 1.4) |
| Pegasus | Futures |
| CTP Options | ETF Options (Live 20190802) |
| Vertex HTS | ETF Options |
| CTP Options | ETF Options (Live 20190802) |
| Hang Seng UFT | Futures, ETF options |
| ESSENCE | Futures, Gold TD |
| HTS | ETF OPTIONS |
| CMT XTP | A-Share, Dual-Financing, ETF Options |
| Guotai Junan Unified Trading Gateway | A shares |
| Huaxin Qidian Stocks | A shares |
| Comstar | Interbank market |
| Oriental Securities OST | A shares |
| Reuters Securities | Overseas Multi-species |
| Edsa 9.0 | Futures | 
| Direct Futures | Futures |
| Straight Futures | Futures |
| Direct Futures | Futures |
| TTS | Futures |
| Gold TTS | Gold TD |


## Interface Details

### CTP

#### Interface Support

- Operating System
  - Ubuntu
  - Ubuntu

- Trading varieties
  - Futures
  - Futures Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:
#### Get Account Number

- SimNow account: Get it from SimNow website. Simply enter your cell phone number and SMS verification (SMS verification can sometimes only be received during normal business hours on weekdays). SimNow's username (InvestorID) is a 6-digit plain number, the Broker ID number is 9999, and it provides two environments for intraday simulation trading and after-hours testing. You need to change your password once before you can use it. Please note that the applicable time period for each set of simulation environment is different.
  
- Real trading account: open an account in a futures company, by contacting the account manager can be opened. The user name is a pure number and the brokerage number is also a 4-digit pure number (the brokerage number of each futures company is different). In addition, a live account can also be opened for simulated trading, again, you need to contact your account manager.

### CTPTEST (CTP Test)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading varieties
  - Futures
  - Futures Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Open an account with a futures company and apply to the futures company for a penetrating access test by contacting your account manager.

### MINI (CTP Mini)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading varieties
  - Futures
  - Futures Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Open an account with a futures company, which can be opened by contacting your account manager. The user name is a pure number and the brokerage number is also a 4-digit pure number (each futures company has a different brokerage number). Alternatively, a live account can be opened for simulated trading, again by contacting your account manager.

### FEMAS (Pegasus)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - Futures

- Position direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Open an account with a futures company, which can be opened by contacting your account manager. The user name is a pure number and the broker code is also a 4-digit pure number (each futures company has a different broker number). In addition, a live account can also be opened for simulated trading, again, you need to contact your account manager.

### SOPT (CTP Options)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading varieties
  - ETF Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Open an account with a futures company, which can be opened by contacting your account manager. The username is a pure number and the brokerage code is also a 4-digit pure number (the brokerage code is different for each futures company). Alternatively, a live account can also be opened for simulated trading, again by contacting an account manager.

### SEC (Vertex Feitron)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - ETF Options

- Position Direction
  - Stocks only support one-way positions
  - Stock options only support two-way positions

- Historical data
  - Not available

#### Related Fields

- Account Number:
- Password:
- Ticker Address:
- Trading Address:
- Running Protocol: TCP, UDP
- Authorization Code:
- Product Number:
- Capture Type: Vertex, Hang Seng, JSE, Jinshida
- Ticker Compression: N, Y

#### Get account number

Open an account with a futures company, which can be opened by contacting your account manager.

### HTS (Vertex HTS)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - ETF Options

- Position Direction
  - Bidirectional Positions

- Historical data
  - Not available

#### Related Fields

- Account:
- Password:
- Ticker Address:
- Trading Address:
- Running Protocol: TCP, UDP
- Authorization Code:
- Product Number:
- Capture Type: Vertex, Hang Seng, JSE, Jinshida
- Ticker Compression: N, Y

#### Get account number

Open an account with a futures company, which can be opened by contacting your account manager.

### UFT (Hang Seng UFT)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading Style
  - Futures
  - ETF Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Ticker Server:
- Trading Server:
- Server Type: Futures, ETF Options
- Product Name:
- Authorization Code:
- Delegation Type: q

#### Get Account Number

Test account please apply through Hang Seng Electronics.

### ESUNNY

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading varieties
  - Futures
  - Gold TD

- Position Direction
  - Support bi-directional positions

- Historical data
  - Not supported

#### Related Fields

- Row Account:
- Risk Password:
- Quotes Server:
- Ticker Port: 0
- Ticker Authorization Code:
- Trading Account Number:
- Trading Account Number: Trading Password:
- Trading Server:
- Trading Port: 0
- Trading Product Name:
- Trading Authorization Code:
- Trading System: Domestic, Foreign

#### Get an account

Please apply for a test account through the official website of eSun.

### XTP (China Pacific Desk)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu

- Trading varieties
  - A-share
  - Two Financing
  - ETF Options

- Position Direction
  - Stocks only support one-way position
  - The rest of the underlying supports two-way positions

- Historical Data
  - Historical data is not available

#### Related Fields

- Account:
- Password:
- Client Number: 1
- Running Address:
- Ticker Port: 0
- Trading Address:
- Trading Port: 0
- Trading Protocol: TCP, UDP
- Log Level: FATAL, ERROR, WARNING, INFO, DEBUG, TRACE
- Authorization Code:

#### Get Account

Please apply for a test account through CTS.

#### Other Features

XTP is the first Extreme Counter to provide financing and securities.

### HFT (Guotai Junan Unified Trading Gateway)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - A-shares

- Position direction
  - Only support one-way position

- Historical data
  - Not available

#### Related Fields

- Trading User Name:
- Trading Password. 
- Trading Server: Trading Server: Trading Server: Trading Server: Trading Server: Trading Server: Trading Server: Trading Server: Trading Server 
- Trading Port:
- Organization Code:
- Business Office Code:
- Gateway:
- Trading User Name:
- Ticker Password:
- Ticker Server. 
- Ticker Port:

#### Get Account

Test account please apply through Guotai Junan.

### TORASTOCK (Huaxin Singularity Stock)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - A Shares

- Position direction
  - Only support one-way position

- Historical data
  - Not available

#### Related Fields

- Account:
- Password:
- Quote Server:
- Trading server:
- Account Type: User Code, Funding Account
- Address Type: Front Address, FENS Address

#### Get account number

Test account please apply through Huaxin Securities.

### TORAOPTION (Huaxin Singularity Options)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - ETF Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Account:
- Password:
- Quote Server:
- Trading server:
- Account Type: User Code, Funding Account
- Address Type: Front Address, FENS Address

#### Get account number

Test account please apply through Huaxin Securities.

### COMSTAR (Zhongyi Huida)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - Interbank market

- Position direction
  - None

- Historical data
  - Not available

#### Related Fields

- Trading server:
- Username:
- Password:
- Key:
- Key: Key. routing_type: 5
- valid_until_time: 18:30:00.000

#### Get account number

It can only be used by large financial institutions (proprietary trading departments of brokerage firms, financial market departments of banks, etc.), but not by private equity firms or individuals. You need to purchase ComStar's trading interface service before you can use it.

### OST (Orient Securities)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - A-shares

- Position direction
  - Unidirectional Position

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Trading Server:
- SSE Snapshot Address:
- SSE Snapshot Port: 0
- SSE Snapshot Address:
- SSE Snapshot Port: 0
- Local ip address:

#### Get account number

Open an account at a securities company, which can be opened by contacting an account manager.

### IB (Intelligent Brokerage)

#### Interface Support

- Operating System
  - Windows
  - Ubuntu
  - Mac

- Trading varieties
  - Overseas Multi-species

- Position Direction
  - Only one-way positions are supported

- Historical Data
  - Provide

#### Related Fields

- TWS Address: 127.0.0.1
- TWS Port: 7497
- Client Number: 1
- Trading Account:

#### Get account number

You can get API access after opening an account with PCCW Securities and making a deposit.

#### Other features

Tradable varieties cover stocks, options and options of many overseas markets; relatively low commission.

Please note that the contract code of IB interface is quite special, please go to the product inquiry section of the official website to inquire. VeighNa Trader uses the unique identifier of each contract in a certain exchange ConId as the contract code, rather than Symbol or LocalName.

### TAP (eSun 9.0 Forex)

#### Interface Support

- Operating System
  - Windows

- Trading Instruments
  - Futures

- Position direction
  - Only one-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Ticker Account Number:
- Ticker Password:
- Ticker Server:
- Ticker Port: 0
- Trading Account:
- Trading Password:
- Trading Server:
- Trading Port: 0
- Authorization Code:

#### Get Account

Please apply for a test account through the official website of eSun.

### DA (Direct Access Futures)

#### Interface Support

- Operating System
  - Windows

- Trading varieties
  - Foreign Futures

- Position direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Trading Server:
- Ticker Server:
- Authorization Code:

#### Get an account

You can get API access after you open an account with DIRECT FUTURES and make a deposit.

### ROHON

#### Interface Support

- Operating System
  - Ubuntu
  - Ubuntu

- Transaction Type
  - Futures Management

- Position Direction
  - Only bi-directional positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Please apply for a test account through Ronghang.

Please note that the [Broker Code] of the Ronghang interface is no longer in pure numeric form, but a string that can contain both English and numbers; VeighNa connecting to Ronghang for trading belongs to the [Relay] mode in the passthrough authentication and is no longer in the [Direct Connection] mode when connecting to the counter (CTP, Hang Seng, etc.) for trading, so don't make a mistake in selecting the wrong option when applying for the passthrough authentication test fill in the form.

### TTS

#### Interface Support

- Operating System
  - Ubuntu
  - Ubuntu

- Trading varieties
  - Futures
  - Futures Options

- Position Direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Broker Code:
- Trading Server:
- Ticker Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Please get it through OpenCTP platform.

### SGIT (Flying Mouse)

#### Interface Support

- Operating Systems
  - Ubuntu

- Trading varieties
  - Gold TD

- Position direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Trading Server:
- Quote Server:
- Product Name:
- Authorization Code:

#### Get Account Number

Please get it through Gold Spot Broker.

### KSGOLD (KSGOLD)

#### Interface Support

- Operating System
  - Ubuntu

- Trading varieties
  - Gold TD

- Position direction
  - Only two-way positions are supported

- Historical data
  - Not available

#### Related Fields

- Username:
- Password:
- Trading Server:
- Ticker Server:
- Account Type: Bank Account, Gold Account

#### Get account number

Please get the account number through your gold spot broker.
