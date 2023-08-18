
# PortfolioManager - Portfolio Management Module

## Functional Description

PortfolioManager is a functional module for **Portfolio Management**, which allows users to perform real-time performance tracking and profit/loss analysis of trading strategies through its UI interface during trading.  


## Loading Startup

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check [PortfolioManager] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_portfoliomanager import PortfolioManagerApp

# Write after creating the main_engine object
main_engine.add_app(PortfolioManagerApp)
```


## Start the module

Click [Functions] -> [Portfolio] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_manager/1.jpg)

You can enter the UI interface of the Portfolio Management module, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_manager/6.png)


## Portfolio Information Table

The interface can be divided into left and right parts, the left side shows the information table of the existing portfolios, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_manager/7.png)


The meaning of each column in the portfolio information table is as follows:

 - Portfolio Name: Delegation source identifier (reference), all delegation requests from VeighNa can be directly distinguished by this identifier to its trading source, such as manual trading, algorithmic execution, quantitative strategies, etc., each trading source can be regarded as a separate portfolio.

   - Manual Trading: ManualTrading

   - CTA Strategy: CtaStrategy_Strategy_Name

   - Spread Trading: SpreadTrading_Spread Name

   - Option Trading: OptionMaster_ElectronicEye/DeltaHedging

   - Algorithmic Trading: AlgoTrading_Algorithmic Number

   - Script Strategy: ScriptTrader

   - Portfolio Strategy: PortfolioStrategy_Strategy Name

 - Native Code: Contract code with exchange suffix (vt_symbol)

 - Opening position: position of the contract in the portfolio at yesterday's close (today's open)

 - Current position: the result of the opening position plus the number of transactions today (long transactions - short transactions)

 - Trading profit and loss: all transactions today, the transaction price mapped to the latest price of the current profit and loss

 - Position P&L: the combination of the opening position, the closing price yesterday mapped to the current latest price of the profit and loss

 - Total P&L: The sum of the trade and position P&L.

 - Long position: the number of open and close trades of the contract in the portfolio today.

 - Short position: the number of open and close trades of the contract in the portfolio today.

Among them, TradingPnl and HoldingPnl are calculated using the Marking to Market algorithm used by the futures exchanges for daily settlement, as shown below:

 - TradingPnl = Position * (Day's Close - Yesterday's Close) * Contract Size  

 - Position P&L = Position Change * (Day's Close - Yesterday's Close) * Contract Size  

 - Gross P&L = Trading P&L + Position P&L  

 - Net P&L = Total P&L - Total Commission - Total Slippage  

Users can expand and collapse portfolios and adjust column widths to view information:

 - Click on the arrows to the left of each portfolio to expand and collapse the information for each portfolio;

 - Click on the [Expand All] and [Collapse All] buttons at the top to perform batch operations on all portfolios;

 - Click the [Adjust Column Width] button to automatically adjust the width of each column of the table.

## Transaction Log Table

The right part of the interface shows all the transaction records, click the drop-down box in the upper right corner to filter by portfolio, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_manager/8.png)


## Refresh Frequency

The profit/loss of a portfolio is automatically calculated based on a timing logic, the frequency of calculation can be adjusted by the option box at the top center, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_manager/5.png)


Please note that all portfolio position data is written to the cache file when closing VeighNa Trader, so don't kill the process and exit directly, you will lose the data.  

When loading every other day, the program will automatically settle yesterday's total position into today's yesterday's position data field. This logic is not necessarily appropriate for markets with 24-hour trading (foreign futures), and subsequent consideration will be given to adding a daily timed settlement or manual settlement function.

If you find that a position has been recorded incorrectly, or the strategy has been removed, you can manually modify the cache file, and then restart VeighNa Trader can be.

The default path to the cache file on Windows systems is located at:

`C:\Users\Administrator\.vntrader\portfolio_manager_data.json`

where Administrator is the user name of the current Windows system.