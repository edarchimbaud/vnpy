# PaperAccount - Local Simulation Trading Module


## Introduction

PaperAccount is a functional module for **localized simulation trading**, which allows users to perform localized simulation trading based on real market quotes through its UI interface.

## Load and start

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check [PaperAccount] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_paperaccount import PaperAccountApp

# Write after creating the main_engine object
main_engine.add_app(PaperAccountApp)
```


## Start the module

Before launching the module, please connect the interface where you want to make a demo trade (see the Connecting Interface section of the Basic Usage chapter for details on how to do this). Start the module after you see "Contract Information Query Successful" in the [Log] column of the main interface of VeighNa Trader, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not automatically get all contract information when logging in, but only when the user manually subscribes to the quotes. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

Once the trading interface is connected, the local demo trading module starts automatically. At this time, all contract orders and withdrawal requests are **taken over by the local simulation trading module** and will not be sent to the live server.


## Function Configuration

Click [Function] -> [Demo Trading] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/4.png)

You can enter the UI interface of the local demo trading module, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/5.png)

Users can configure the following functions through the UI interface:

- Slippage for Market and Stop orders.
  - Used to influence the **slip jump** of the transaction price relative to the intraday price when the market order and stop order are transacted;

- Calculation Frequency of Position P&L for Demo Trading
  - How many seconds to perform a position P&L calculation update, if more positions found program lag, it is recommended to try to reduce the frequency;

- Immediately after the order is placed to use the current market summarization
  - By default, the commission issued by the user needs to ** wait until the next TICK market push will be summarized ** (simulation of real-time scenarios), for the TICK push frequency of inactive contracts can be checked this option, the commission will be ** immediately based on the current summary of the latest TICK market **;

- Empty All Positions
  - A key to clear all local position data.

The Local Simulation Trading module can also be used together with other strategy application modules (e.g. CtaStrategy module, SpreadTrading module, etc.) to enable localized quantitative strategy simulation trading tests.


## Data Monitoring

Users can query the trading interface status of confirmed contracts through [Query Contracts]:

Click [Help] -> [Contract Query] in the menu bar, and in the pop-up dialog box, directly click the [Query] button in the upper right corner, and find that the [Trading Interface] column of all contracts are displayed as PAPER, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/2.png)

Before placing and withdrawing an order on a contract, the user must first **SUBSCRIBE** the quotes of that contract.

The interface columns of the information displayed in the three monitoring components [Commission], [Transaction] and [Position] in the following chart are all PAPER (local simulation data):

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/paper_account/3.png)

Please note that the local demo trading module **does not provide the funds calculation function**, so the [Funds] component displays the funds of the live account, which will not be changed by the commissions generated in the local demo trading module.


## Business Logic

The business logic of the local demo trading module is shown below:

- Supported commission types (unsupported types will be rejected):

  - Limit orders;
  - Market orders;
  - Stop orders;

- Entrusted to summarize the rules using ** to the price of the transaction ** mode, to buy entrusted as an example:

  - Limit order: when the market price ask_price_1 is less than or equal to the commission price, the transaction;
  - Stop order: when the plate selling 1 price ask_price_1 is greater than or equal to the commission price, then the transaction;

- Delegation transaction **does not take into account the amount of pending orders on the disk**, a one-time full transaction;

- After the commission is closed, the commission status update OrderData is pushed first, and then the transaction information TradeData is pushed, **and the order in real trading is consistent**;

- After the commission is closed, the module will automatically record the corresponding position information PositionData:

  - According to the position mode (long/short vs. net position) information of the contract itself, the corresponding position information is maintained;
  - **When a position is opened and closed, the cost price of the position is updated using a weighted average calculation;**
  - When closing a transaction, the cost price of the position remains unchanged
  - Under the long/short position mode, the corresponding position quantity will be frozen after the closing order is placed, and the order will be rejected when the available quantity is insufficient;
  - The profit and loss of the position will be calculated based on the cost price of the position and the latest transaction price at regular intervals (default frequency 1 second);

- Data persistence:

  - The transaction data and commission data are not saved and will disappear when VeighNa Trader is closed;
  - Position data will be written to the hard disk file **immediately when there is a change** and can be seen after restarting VeighNa Trader and logging into the trading interface (to receive the corresponding contract information).
