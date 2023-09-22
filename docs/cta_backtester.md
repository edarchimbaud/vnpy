# CtaBacktester - CTA Backtesting Research Module

## Introduction

CtaBacktester is a functional module for **CTA backtesting research**, which allows users to conveniently complete tasks such as data download, historical backtesting, result analysis and parameter optimization through its UI interface.

## Load and start

### Loading VeighNa Station

After logging in VeighNa Station, click the [Transaction] button and check [CtaBacktester] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_ctabacktester import CtaBacktesterApp

# Write after creating the main_engine object
main_engine.add_app(CtaBacktesterApp)
```


## Start the module

For user-developed strategies, they need to be placed in the **strategies** directory in the VeighNa Trader runtime directory in order to be recognized and loaded. The exact path to the runtime directory can be viewed in the title bar at the top of the VeighNa Trader main interface.

For users with a default installation on Windows, the path to the strategies directory where strategies are placed is usually:

```
C:\Users\Administrator\strategies
C:\Users\Administrator\strategies
```

where Administrator is the system user name currently logged on to Windows.

After launching VeighNa Trader, click [Functions] -> [CTA Backtest] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/00.png)

A graphical backtesting interface will open, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/25.png)


## Downloading Data

Before starting strategy backtesting, you first need to ensure that there is enough historical data in the database, and the CtaBacktester module also provides the ability to download historical data with one click.

To download the data, you need to fill in four fields: local code, bar data, start date and end date:

<span id="jump">

- Local Code
  - Format is Contract Code + Exchange Name
  - For example, IF888.CFFEX, rb2105.SHFE.
- bar period:
  - 1m (1 minute bar)
  - 1h（1小时K线）
  - d（日K线）
  - w（周K线）
  - tick（一个Tick）
- 开始和结束日期
  - 格式为yyyy/mm/dd
  - 如2018/2/25、2021/2/28

</span>

After filling out the form, click the [Download Data] button below to start the download task, after the success of the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/27.png)

Note that the historical data will be saved in the local database after the download is completed, and can be used directly in subsequent backtests without having to repeat the download each time.

### Data source: data services (futures, stocks, options)

Take RQData as an example, [RQData](https://www.ricequant.com/welcome/purchase?utm_source=vnpy) provides historical data of domestic futures, stocks and options. Before using it, you need to make sure that the data service has been configured correctly (see the Global Configuration section of the Basic Usage chapter for details on how to configure it). When you open CtaBacktester, it will automatically perform data service initialization, and if it succeeds, it will output the log of "Data Service Initialization Successful", as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/26.png)

### 数据来源：IB（外盘期货、股票、现货等）

Interactive Brokers Interactive Brokers (IB) provides a wealth of foreign market historical data downloads (including stocks, futures, options, spot, etc.), note that before downloading you need to start the IB TWS trading software, and in the main interface of the VeighNa Trader connected to the IB interface, and subscribe to the required contract quotes. Successful download is shown in the figure below.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/28.png)


## Execute Backtest

After preparing the data, you can start using historical data to backtest the strategy research, backtesting needs to be configured with the relevant parameters:

- Strategy Type
  - Trading Strategy: Select the name of the strategy to be backtested in the drop-down box;
  - Local Code: Be careful not to miss the exchange suffix;
- Data range
  - The format is described in detail in the [Download Data](#jump) section of this chapter;
- Trading Costs
  - Slippage: the difference between the point at which the order is placed for trading and the actual point at which it is traded;
  - Percentage handling fee: just fill in the number, do not fill in the percentage;
  - Fixed ratio commission: you can fill in 0 for the commission, then divide the commission by the contract multiplier and add it to the slippage;
- Contract Attributes
  - Contract multiplier: the trading unit of the contract;
  - Price Jump: the minimum price change of the contract price;
  - Backtest Funding: the funds in the account;
  - Contract Mode: Positive.

After the configuration is completed, click the [Start Backtesting] button below to bring up the Strategy Parameter Configuration dialog box for setting the strategy parameters, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/29.png)

Click the [OK] button to start the backtesting task, and the log interface will output relevant information, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/10.png)

After the backtesting is completed, the statistical indicators of the strategy's backtesting performance and the related charts will be automatically displayed on the right side area, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/30.png)

If you click [Start Backtest] without the required historical data in the database, the log interface will output the log "Insufficient historical data, backtest terminated", as shown in the following figure:

The following figure shows the termination of the test. [](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/15.png)


## Results Analysis

### Performance Chart

The performance chart on the right consists of the following four sub-charts:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/31.png)

The horizontal axis of the [ Account NAV ] chart is time and the vertical axis is money, reflecting how the account NAV changes over the trading session as a function of the trading day.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/32.png)

The horizontal axis is time and the vertical axis is retracement, reflecting the extent of retracement from the most recent high over the trading day.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/33.png)

The horizontal axis of the [Daily P&L] chart is time, and the vertical axis is the amount of daily P&L (settled at the closing price using the day-by-day staring rule), reflecting the daily change in the strategy's P&L over the entire backtesting period.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/34.png)

The horizontal axis of the chart is the daily profit/loss value, and the vertical axis is the probability of occurrence of that profit/loss value, reflecting the overall daily profit/loss probability distribution.

### Statistical Indicators

The Statistical Indicators area is used to display the statistical values related to the strategy's historical backtest performance, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/35.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/36.png)

Depending on the data type, the indicators can be categorized as:

- Date Information
  - First trading day
  - Last trading day
  - Total trading days
  - Profitable trading days
  - Loss day
- Profit/Loss
  - Starting capital
  - Ending funds
  - Total Return
  - Annualized Return
  - Maximum retracement
  - Percentage Maximum Retracement
  - Total Profit and Loss
- Trading Costs
  - Total commission
  - Total slippage
  - Total Turnover
  - Total number of transactions
- Average Daily Data
  - Average Daily Profit/Loss
  - Average Daily Fee
  - Average daily slippage
  - Average Daily Turnover
  - Average Daily Turnover
  - Average Daily Yield
  - Standard deviation of return (daily average)
- Performance Evaluation
  - Sharpe Ratio
  - Return Retracement Ratio

### Details

After the backtesting is completed, you can click the [Entrustment Record] button on the left side area to view the detail information of the strategy's entrustment stroke by stroke during the backtesting process:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/43.png)

If you find the table content display is incomplete, you can click the right mouse button to bring up a pop-up menu and select the [Adjust Column Width] button to perform automatic column width scaling:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/46.png)

The form also supports one-click to save the data in the table as a CSV file, in the previous step right-click to pop-up menu, click [Save Data] button, you can pop-up the dialog box shown below to select the save file name:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/42.png)

The **transaction price** of the commission issued by the strategy during the backtesting process is not necessarily the price of the original order, but has to be calculated by the backtesting engine based on the prevailing market data and the price of the order to be summarized, and the specific transaction details corresponding to each commission can be viewed by clicking the [Transaction Record] button:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/38.png)

After clicking the [Daily Profit/Loss] button, you can see the daily profit/loss details of the strategy as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/39.png)

The daily profit/loss statistics here are calculated using the Marking-to-Market rule, which is commonly used in the futures market:

- Position profit and loss: today's opening position of the portion of the position, the closing price of yesterday's opening, closing price of this day, the amount of profit and loss calculated;
- Trading Profit and Loss: part of today's intra-day transactions, the transaction price to open positions, the closing price of today's positions, the amount of profit and loss calculated;
- Total profit and loss: the amount after summarizing the profit and loss of positions and trading profit and loss;
- Net profit and loss: the total profit and loss after deducting the commission and slippage, but also the final calculation of the daily profit and loss amount used to display the four charts.

### Bar Charts

Clicking on the "Bar Charts" button opens a chart that displays the backtested Bar data, as well as the specific buy and sell point positions of the strategy, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/44.png)

Note that the charting may take some time (usually tens of seconds to a few minutes), so please be patient.

The legend description in the bar chart can be seen at the bottom of the window, and the overall color scheme and style is standard for the domestic market. The lines between open and closed positions are plotted using the First-in, First-out rule, where each transaction is automatically matched with other transactions according to its volume, so that even complex additions and subtractions to the strategy can be plotted correctly.


## Parameter Optimization

For the developed strategy, you can use CtaBacktester's built-in optimization algorithm to quickly perform parameter optimization, currently supporting two optimization algorithms: exhaustive and genetic.

### Setting Optimization Parameters

Click the "Optimize Parameters" button, the "Optimize Parameter Configuration" window will pop up:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/37.png)

Click the [Objective] drop-down box, select the objective function to be used in the optimization process (i.e. optimize with the objective of maximizing the value):

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/45.png)

For the strategy parameters to be optimized, you need to configure:

- [Start] and [End]: used to give the range of parameters to optimize;
- [Step]: for the value of each change of the given parameter;

Example: If the [start] of a parameter is set to 10, [end] is set to 20, and [step] is set to 2, the optimization space of the parameter in the optimization process is: 10, 12, 14, 16, 18, 20.

For strategy parameters with fixed values, please set both [Start] and [End] to the same value.

### Optimization of the poor-execution algorithm

After setting up the optimization parameters, click the [Multiprocessing Optimization] button at the bottom of the window. At this time, CtaBacktester will call Python's multiprocessing module, and according to the number of cores of the current computer's CPU, it will start the corresponding number of processes to carry out the optimization task in parallel.

During the optimization process, the exhaustive algorithm traverses each combination in the parameter optimization space. The traversal process runs a historical backtest using the combination as a strategy parameter and returns the value of the optimization objective function. After completing the traversal, all the values of the objective function are sorted according to each other to select the optimal parameter combination result.

The efficiency of the exhaustive optimization algorithm is directly related to the number of CPU cores: if the user's computer is 2-core, the optimization time is 1/2 that of a single core; if the computer is 10-core, the optimization time is significantly reduced to 1/10 that of a single core.

### Genetic algorithm optimization

After setting the parameters to be optimized, click the [Genetic Algorithm Optimization] button at the bottom of the window. At this time, CtaBacktester will call Python's multiprocessing module and deap module to perform the efficient and intelligent multi-process genetic algorithm optimization task.

Attached is a brief working principle of the genetic algorithm:

1. define the optimization direction, e.g. maximize the total yield; 
2. randomly select some combinations of parameters from the global optimization space to form an initial population; 
3. Evaluate all individuals in the population, i.e., run backtests to obtain the objective function results;
4. sort the individuals (parameter combinations) based on the results of the objective function, and eliminate those that do not perform well. 5. crossover the remaining individuals;
5. crossover or mutation of the remaining individuals to form a new population after evaluation and screening. 6;
6. The above 3-5 steps are a complete population iteration, which needs to be repeated several times during the whole optimization process;
7. After several iterations, the variability within the population is reduced, the parameters converge to the optimal solution, and the final output results.

### Optimization result analysis

After the optimization is completed, a message will be output in the log area:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/49.png)

At this time, click the [Optimization Result] button to view the results:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/50.png)

The parameter optimization results in the above figure are sorted from highest to lowest based on the value of the objective function [Total Return] selected when starting the optimization task.

Finally, the optimization results can be saved to a local CSV file by clicking the [Save] button in the lower right corner for easy use in subsequent analysis.


## Strategy Code

### Code Editing

If you need to modify the strategy, select the strategy from the drop-down box in the upper left corner of the CtaBacktester interface, and then click the [Code Edit] button in the lower left corner to automatically open Visual Studio Code for code editing. If Visual Studio Code cannot be found, the Failed to Launch Code Editor dialog box will pop up, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/61.png)

### Strategy Overloading

When users modify the strategy source code through CtaBacktester, the modification still stays at the level of the code file on the hard disk, and the strategy code before modification is still in the memory.

If you want the modification to take effect in memory immediately, you need to click the [Strategy Reload] button at the bottom left corner, at this time, CtaBacktester will automatically scan and reload all the strategy codes in the strategy files, and at the same time, there will be a relevant log output, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_backtester/59.png)

After the reloading and refreshing is completed, when you run the backtest or optimization again, the modified strategy code will be used.
