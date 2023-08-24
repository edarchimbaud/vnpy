# AlgoTrading - Algorithmic Mandate Execution Trading Module

## Introduction

AlgoTrading is a module for **Algorithmic Entrusted Execution Trading**, which allows users to conveniently accomplish tasks such as starting algorithms, saving configurations, stopping algorithms, etc. through the operation of its UI interface.

AlgoTrading is responsible for the specific execution process of delegated orders. Currently, AlgoTrading provides a variety of sample algorithms, the user can automatically split large orders into suitable small orders commissioned in batches, effectively reducing the cost of trading and impact costs (such as the iceberg algorithm, sniper algorithms), but also in the set thresholds for the operation of the high throw and low sucking (such as grid algorithms, arbitrage algorithms).

## Loading startup

### Loading VeighNa Station

After launching and logging in to VeighNa Station, click the [Trading] button and check [AlgoTrading] in the [Application Module] field in the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_algotrading import AlgoTradingApp

# Write after creating the main_engine object
main_engine.add_app(AlgoTradingApp)
```

## Start the module

For user-built algorithms, they need to be placed in the algo_trading.algos directory to be recognized and loaded.

Before launching the module, please connect the trading interface (see the Connecting the Interface section of the Basic Usage chapter for details on how to connect). Start the module after you see "Contract information query successful" in the [Log] column of VeighNa Trader's main interface, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not automatically get all contract information when logging in, but only when the user manually subscribes to the quotes. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

After successfully connecting to the trading interface, click [Functions] -> [Algorithmic Trading] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/1.png)

You can enter the UI of Algorithmic Entrusted Execution trading module, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/10.png)


## Configure Algorithm

The configuration parameter requirements are as follows:

- Algorithm: select the trading algorithm to be executed in the drop-down box;
- Local code: format is vt_symbol (contract code + exchange name);
- Direction: long, short;
- Price: the price at which the commission is placed;
- Quantity: the total quantity of the commission, which needs to be split into small batches of orders for trading;
- Execution time (in seconds): the total time in seconds to run the algorithmic trade;
- Interval of each round (seconds): how much time to carry out the commission to place an order operation, in seconds;
- Open and Flat: Open, Flat, Flat Today, Flat Yesterday.

### Save configuration

The configuration information of the trading algorithm can be saved locally in a json file, so that every time you open the algorithmic trading module, you do not need to repeat the input, as follows:

- Enter the name of the algorithm configuration information in the [Configuration Name] option, and then click the [Save Configuration] button below to save the configuration information locally;
- After saving the configuration, the [Configuration] component on the right side of the interface can see the configuration name and configuration parameters saved by the user.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/4.png)

The saved configuration file is in algo_trading_setting.json in the .vntrader folder, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/5.png)


## Startup Algorithms

VeighNa currently provides a total of six commonly used example algorithms. This document uses the Time Weighted Average Algorithm (TWAP) as an example to introduce the algorithm startup process.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/3.png)

After the parameter configuration is completed (the saved algorithm information can be switched to the information content configured on the left side of the interface by clicking [Use] under the corresponding algorithm in the [Configuration] column), click on the [Start Algorithm] button, and the algorithm transaction can be executed immediately.

If the startup is successful, you can observe the execution status of the algorithm in the upper-right corner of the [Execution in progress] interface.

Figure algorithmic execution of the task is specific: the use of time-weighted average algorithm, buy 10,000 lots of soybean oil 2109 contract (y2109), the implementation of the price of 9,000 yuan, the implementation time of 600 seconds, the interval between each round of 6 seconds; that is, every 6 seconds, when the contract price is less than or equal to the contract price of 9,000, to 9,000 price of buying 100 lots of soybean oil 2109 contract, will be divided into 100 times to buy the operation. into 100 times.

## CSV startup

When there are more algorithms to start, you can use CSV file to start them in batch at one time. Click the [CSV Start] button on the left side of the graphical interface, find the CSV file you want to import in the pop-up dialog box and open it to start the algorithm quickly.

Please note that the format of the CSV file should be consistent with the fields in the left editing area as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/12.png)

It is more convenient to add algorithms in batch by combining with Excel's table fast editing function. After successful startup, the execution of all the algorithms in the CSV file will be displayed under the [Execution in Progress] interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/14.png)

Please note that after the CSV is started, only the content output and changes can be observed in the [Executing], [Log] and [Finished] interfaces, and the algorithm information in the CSV file will not be added to the configuration.


## Stop Algorithm

When users need to stop an executing algorithm, they can click the [Stop] button in the [Executing] interface to stop an executing algorithm transaction, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/6.png)

Users can also stop all executing algorithmic trades with one click by clicking the [Stop All] button at the bottom of the Delegated Trades screen, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/7.png)


## Data Monitoring

The Data Monitoring interface consists of four components:

Executing Component: Displays the executing algorithmic transactions, including: algorithm, parameters and status. After successfully launching an algorithm, switching to the upper right corner of the [Execution in Progress] interface will display the execution status of the algorithm, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/6.png)

Ended Component: displays the completed algorithm transaction, again including: algorithm, parameters and status. After the algorithm is finished or stopped, switch to the upper right corner [Finished] interface, it will show the execution status of the algorithm, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/9.png)

Log component: displays log information related to starting, stopping, and completing the algorithm. After opening the algorithmic trading module, it will be initialized, so the [Log] component will first output "Algorithmic trading engine started" and "Algorithm configuration loaded successfully", as shown in the following figure:

The following figure shows: ![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/11.png)

Configuration component: Used to load the configuration information of algo_trading_setting.json and display it under [Configuration] column with graphical interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/algo_trading/8.png)

- Clicking the [Use] button of the configuration component immediately reads the configuration information and displays it on the delegated trading interface, and then clicking [Start Algorithm] can start trading;
- Clicking the [Remove] button of the configuration component removes the algorithm configuration and synchronizes the update to the json file.


## Example Algorithm

The path to the example algorithm is located in the algo_trading.algos folder (please note that individual algorithms are not written in the direction of the open and close, if necessary, based on their own needs for personalized modification). Currently, the algorithmic trading module offers the following six built-in algorithms:

### DMA - Direct Mandate Algorithm

The Direct Mandate Algorithm (DMA) sends new mandates (Limit, Stop, Market) directly.

### TWAP - Time Weighted Average Algorithm

The Time Weighted Average Algorithm (TWAP) is executed as follows:

- Distribute the number of commissions evenly over a certain time zone and place buy orders (or sell orders) at specified intervals with specified prices.

- Buy situation: Sell price is lower than the target price, the commission is issued, the number of commissions in the remaining commission volume and the commission to split the volume of the smallest value.

- Sell case: when the buy price is higher than the target price, the commission is issued, and the number of commissions is the smallest of the remaining number of commissions and the number of commission splits.

### Iceberg - Iceberg Algorithm

The Iceberg algorithm is executed as follows:

- Place a pending order at a certain price, but only a portion of it, until it is all filled.

- Buy: first check the withdrawal, the latest Tick sell one price is lower than the target price, the implementation of the withdrawal; if there is no activity commission, issued by the commission, the number of commissions in the remaining commission volume and the amount of pending commissions to take the smallest value.

- Sell situation: first check the withdrawal order, the latest Tick buy one price is higher than the target price, execute the withdrawal order; if there is no active commission, issue the commission, the commission quantity is the smallest among the remaining commission quantity and the pending commission quantity.

### Sniper - Sniper Algorithm

The Sniper algorithm (Sniper) is executed in the following steps:

- Monitor the quotes pushed by the latest Tick and find a good price to quote immediately to close the deal.

- Buy: When the latest Tick Sell One price is lower than the target price, issue a commission, and take the smallest of the remaining commission volume and Sell One volume.

- Sell: When the latest Tick Bid 1 price is higher than the target price, the commission will be issued and the number of commissions will be taken as the minimum value among the remaining commissions and the Buy 1 quantity.

### Stop - Conditional Entry Algorithm

The steps to execute the conditional order algorithm (Stop) are as follows:

- Monitor the latest Tick push market, find the market breakthrough and immediately quote a deal.

- Buy: If the latest Tick price is higher than the target price, the commission will be issued and the commission price will be the target price plus the overrun price.

- Sell: When the latest Tick price is lower than the target price, the order will be placed at the target price minus the overrun price.

### BestLimit - Best Limit Algorithm

The BestLimit algorithm is executed as follows:

- Monitor the latest Tick pushes, find a good price and immediately quote a deal.

- Buy: first check the withdrawal: the latest Tick buy one price is not equal to the target price, the execution of the withdrawal; if there is no activity commission, the commission is issued, the commission price for the latest Tick buy one price, the number of commissions for the remaining commission volume.

- Sell situation: first check the withdrawal: the latest Tick buy one price is not equal to the target price, the execution of the withdrawal; if there is no activity commission, issued by the commission, the commission price is the latest Tick sell one price, the commission quantity for the remaining commission.
