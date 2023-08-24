# PortfolioStrategy - Multi-Contract Portfolio Strategy Module

## Introduction

PortfolioStrategy is a functional module for **Multi-Contract Portfolio Strategies**, which allows users to easily perform tasks such as strategy initialization, strategy startup, strategy stop, strategy parameter editing, and strategy removal through its UI interface.

### Load and start

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check the [PortfolioStrategy] box in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
# Write at the top
from vnpy_portfoliostrategy import PortfolioStrategyApp

# Write after creating the main_engine object
main_engine.add_app(PortfolioStrategyApp)
```


## Starter module

<span id="jump">

For user-developed strategies, they need to be placed in the **strategies** directory under the VeighNa Trader runtime directory in order to be recognized and loaded. The exact path to the runtime directory can be found in the title bar at the top of the VeighNa Trader main interface.

For users with a default installation on Windows, the path to the strategies directory where strategies are placed is usually:

```
C:\Users\Administrator\strategies
```

where Administrator is the current system user name for logging on to Windows.

</span>

Before starting the module, please connect to the trading interface (for details on how to connect, please refer to the section on connecting to the interface in the chapter on basic usage). Start the module after you see "Contract Information Query Successful" in the [Log] column of the main interface of VeighNa Trader, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not get all contract information automatically when you log in, but only when you subscribe to the market manually. Therefore, it is necessary to manually subscribe to contract quotes on the main interface before launching the module.

After successfully connecting to the trading interface, click [Functions] -> [Portfolio Strategy] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/0.png)

You can enter the UI of Multi-Contract Portfolio Strategy module, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/1.png)

If you have configured the data service (please refer to the Global Configuration section of the Basic Usage chapter for details), the data service login initialization will be executed automatically when you open the Multi-Contract Combination Strategy Module. If the login is successful, a log message "Data service initialized successfully" will be output, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/2.png)


## Add Strategy

Users can create different strategy instances (objects) based on the written combined strategy templates (classes).

Select the name of the strategy to be traded in the drop-down box in the upper left corner, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/3.png)

Please note that the strategy name shown is the name of the **Strategy Class** (camel-named) and not the name of the strategy file (underline-patterned named).

After selecting the strategy class, click [Add Strategy] and the Add Strategy dialog box will pop up as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/4.png)

When creating a strategy instance, you need to configure related parameters, and the requirements of each parameter are as follows:

- Instance name
  - The instance name cannot be renamed;
- Contract Symbol
  - The format is vt_symbol (contract code + exchange name);
  - It must be a contract name that can be found in the real trading system;
  - Contract names are separated by "," with no space in between;
- Parameter settings
  - The parameter names shown are the names of the parameters written in the parameter list of the strategy;
  - The default values are the default values of the parameters in the strategy;
  - From the above figure, we can observe that the <> bracket after the parameter name shows the data type of the parameter, and the corresponding data type should be followed when filling in the parameter. Where <class 'str'> is a string, <class 'int'> is an integer, and <class 'float'> is a floating point number;
  - Note that if a parameter may be adjusted to a value with decimal places, and the default parameter value is an integer (e.g. 1). Please set the default parameter value to a float (e.g. 1.0) when writing the strategy. Otherwise, the strategy will default the parameter to an integer and will only allow integers to be filled in when you subsequently [Edit] the strategy instance parameters.

After the parameters are configured, click the [Add] button to start creating the strategy instance. After successful creation, you can see the strategy instance in the strategy monitoring component on the left side, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/5.png)

The top of the Strategy Monitor component shows the strategy instance name, the strategy class name, and the strategy author (the author defined in the strategy). The top button is used to control and manage the strategy instance. The first row of the table shows the parameter information inside the strategy (the parameter name needs to be written in the parameter list of the strategy for the graphical interface to be displayed), and the second row of the table shows the variable information during the running of the strategy (the variable name needs to be written in the variables list of the strategy for the graphical interface to be displayed). The [inited] field indicates the current initialization status of the strategy (whether or not historical data playback has been completed), and the [trading] field indicates whether or not the strategy is currently able to start trading.

From the above figure, we can observe that the [inited] and [trading] status of the strategy instance are both [False]. This means that the strategy instance has not yet been initialized and cannot send out trading signals.

After the strategy instance is successfully created, the configuration information of the strategy instance will be saved to the portfolio_strategy_setting.json file in the .vntrader folder.

Please note that if a strategy instance with the same name is added, it will fail to be created and the GUI will output the log message "Failed to create strategy, duplicate name exists" as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/8.png)


## Managing Policies

### Initialization

After the strategy instance is successfully created, you can initialize it. Click the [Initialize] button under this strategy instance, and if the initialization is successful, it is shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/6.png)

After the initialization is completed, you can observe that the [inited] state of the strategy instance is already [True]. This means that the strategy instance has already loaded historical data and completed initialization. [trading] state is still [False], that is, at this time the strategy instance can not start automatic trading.

Please note that unlike CTA strategies, if you enter the wrong vt_symbol when creating an instance, the Multi-Contract Portfolio Strategy module will report an error during initialization, not when creating the strategy instance, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/7.png)

### Startup

The auto-trading function of the strategy can only be activated when the strategy instance is initialized successfully and the [inited] status is [True]. Click the [Start] button under the strategy instance to start the strategy instance. The following image shows the successful startup of the strategy instance:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/10.png)

It can be observed that the [inited] and [trading] status of the strategy instance are both [True]. This means that the strategy instance has completed the historical data playback, and at this time the strategy within the transaction request class function (buy/sell/short/cover/cancel_order, etc.), as well as the information output class function (send_email/put_event, etc.), the real implementation and send the corresponding request instructions to the underlying interface ( actually execute the transaction).

During the initialization of the strategy in the previous step, although the strategy is also receiving (historical) data and calling the corresponding function, but because the [trading] state is [False], so there will not be any real commission to place orders or trading-related log information output.

If the strategy sends out a commission after startup, you can go to the VeighNa Trader main interface to view the commission order details in the [commission] column, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/9.png)

Please note that unlike the CTA strategy module, the Multi-Contract Portfolio strategy **does not provide local stop order functionality**, so there will be no stop order display area on the UI interface.


### Stop

If you want to stop, edit or remove a strategy after launching it due to certain circumstances (e.g. market close time, or intraday emergency), you can click the [Stop] button under the strategy instance to stop the automatic trading of the strategy instance. Successfully, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/11.png)

The Portfolio Strategy Engine will automatically revoke all active mandates previously issued by the strategy to ensure that no out-of-control mandates exist after the strategy is stopped. At the same time the latest variable information for this strategy instance is saved to the portfolio_strategy_data.json file in the .vntrader folder.

At this point, you can observe that the [trading] status of the strategy instance has changed to [False], indicating that the strategy instance has stopped automatic trading.

In the multi-contract combination of strategies in the real trading process, the normal situation should let the strategy in the entire trading session are automatically running, try not to have additional pause restart class operation. For the domestic futures market, the strategy should be started before the start of the trading session, and then until after the close of trading, and then turn off the automatic trading. Since CTP now also shuts down the system after the night close and restarts it in the morning before the market opens, you need to stop the strategy and close VeighNa Trader after the night close as well.

### Edit

If you want to edit the parameters of a strategy instance after creating the strategy instance (if you have already started the strategy, you need to stop the strategy first by clicking the [Stop] button under the strategy instance), you can click the [Edit] button under the strategy instance, and the parameter editing dialog box will be popped up for modifying the strategy parameters. As shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/12.png)

After editing the strategy parameters, click the [OK] button below and the corresponding changes will be updated in the parameter table immediately.

However, the trading contract code of the strategy instance cannot be modified, and the initialization operation will not be re-executed after the modification. Please also note that at this time, the modification is only the .vntrader folder porfolio_strategy_setting.json file in the strategy instance of the parameter values, and does not modify the original strategy file under the parameters.

Before the modification, the json file is shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/18.png)


After modification, the json file is shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/17.png)

If you want to start the strategy again after editing in the disk, click the [Start] button under the strategy instance to start the strategy instance again.

### Remove

If you want to remove a strategy instance after creating it (if you have already started the strategy, you need to click the [Stop] button under the strategy instance to stop the strategy), you can click the [Remove] button under the strategy instance. After successful removal, the strategy instance information will no longer be displayed in the Strategy Monitor component on the left side of the GUI. As shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/13.png)

At this time, the portfolio_strategy_setting.json file under the .vntrader folder also removes the configuration information of this strategy instance.

### Status tracking

If you want to track the status of a strategy through the GUI, there are two ways to do so:

1. call the put_event function

   All variables in a strategy instance need to have their names in the strategy's variables list before they can be displayed in the GUI. If you want to track the state of the variables, you need to call the put_event function in the strategy before the data is refreshed in the interface.

   Sometimes you may find that no matter how long the strategy runs, the variable information does not change. In this case, please check if you missed the call to put_event function in the strategy.

2. Calling the write_log function

   If you not only want to observe the state of variable information, but also want to output personalized logs based on the state of the strategy, you can call the write_log function in the strategy to output logs.

## Run log

### Log content

There are two sources of logs output on the UI interface of the Multi-Contract Combination Strategy module, which are the strategy engine and the strategy instance.

**Engine logs

The strategy engine generally outputs global information. The following figure shows the logs output by the strategy engine, except for the content with a colon after the strategy instance name.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/15.png)

**Strategy Log**

If the write_log function is called in the strategy, then the log contents are output via the strategy log. The content in the red box below is the strategy log output by the strategy instance. Before the colon is the name of the strategy instance and after the colon is the content output by the write_log function.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/16.png)

### Empty operations

If you want to empty the log output on the Multi-Contract Portfolio Strategy UI, you can click the [Empty Log] button on the upper right corner, and then you can empty the log output on the UI with one click.

After clicking [Empty Log], the following figure shows:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/14.png)

## Batch Operation

If the strategy has been fully tested, is stable in real trading, and does not need to be adjusted frequently, if there are multiple instances of combined strategies that need to be run, you can use the [Initialize All], [Start All] and [Stop All] functions at the upper right corner of the interface to perform the operations of batch initialization and starting of strategy instances before the trading session, and batch stopping of strategy instances after the trading session.

### Initialize All

After all strategy instances have been created successfully, click the [Initialize All] button at the upper right corner to batch initialize the strategy instances, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/19.png)

### Initialize All

After all strategy instances have been initialized successfully, click the [Start All] button on the upper right corner to start strategy instances in bulk, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/20.png)

### Stop All

After all strategy instances have been started successfully, click the [Stop All] button on the upper right corner to stop the strategy instances in batch, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/portfolio_strategy/21.png)

## Multi-Contract Combination StrategyTemplate - The Basics

Multi-Contract Portfolio Strategy Template provides signal generation and delegate management functions, based on which users can develop their own multi-contract portfolio strategies (located in site-packages\vnpy_portfoliostrategy\template).

User-developed strategies can be placed in the [strategies](#jump) folder under the user's runtime folder.

Please note that:

1. strategy file naming is in underscore pattern, e.g. portfolio_boll_channel_strategy.py, while strategy class naming is in camel case, e.g. PortfolioBollChannelStrategy.

2. Do not overlap the class name of the custom strategy with the class name of the example strategy. If they do, only one strategy class name will be displayed on the GUI.

The following PortfolioBollChannelStrategy strategy example demonstrates the specific steps of strategy development:

Before writing the strategy logic based on the strategy template, you need to load the internal components you need to use at the top of the strategy file, as shown in the code below:

```python 3
from typing import List, Dict
from datetime import datetime

from vnpy.trader.utility import ArrayManager, Interval
from vnpy.trader.object import TickData, BarData
from vnpy_portfoliostrategy import StrategyTemplate, StrategyEngine
from vnpy_portfoliostrategy.utility import PortfolioBarGenerator
```

where StrategyTemplate is the strategy template, StrategyEngine is the strategy engine, Interval is the data frequency, TickData and BarData are the data containers that store the corresponding information, PortfolioBarGenerator is the bar generation module for the portfolio strategy. PortfolioBarGenerator is the portfolio strategy bar generation module, and ArrayManager is the bar time series management module.

### Strategy Parameters and Variables

At the bottom of the strategy class, you can set the author, parameters, and variables of the strategy, as shown in the code below:

```python 3

    author = "Trader in Python"

    boll_window = 18
    boll_dev = 3.4
    cci_window = 10
    atr_window = 30
    sl_multiplier = 5.2
    fixed_size = 1
    price_add = 5

    parameters = [
        "boll_window",
        
        
        
        
        "fixed_size", "price_add", "price_add
        "price_add"
    ]
    variables = []

```

Although the parameters and variables of a strategy are subordinate to the strategy class, the strategy parameters are fixed (specified externally by the trader), whereas the strategy variables change with the state of the strategy over the course of the trade, so the strategy variables only need to be initialized to the corresponding base type at first. For example, integers are set to 0, floats to 0.0, and strings to "".

If you need the strategy engine to display the strategy parameters and variables on the UI interface during runtime and to save their values when the data is refreshed and the strategy is stopped, you need to add the names of the parameters and variables (in the data type of strings) to the parameters and variables lists.

Note that this list can only accept parameters or variables passed in as str, int, float, and bool data types. If you need to use other data types in your strategy, put the definition of the parameter or variable into the __init__ function.

### Class initialization

Input: strategy_engine: StrategyEngine, strategy_name: str, vt_symbols: List[str], setting: dict

Output: none

The __init__ function is the constructor of the strategy class and needs to be consistent with the inherited StrategyTemplate.

In this inherited Strategy class, initialization is generally done in four steps, as shown in the code below:

```python 3
    def __init__(
        self,
        strategy_engine: StrategyEngine,
        strategy_name: str,
        vt_symbols: List[str],
        setting: dict
    ):
        """"""
        super().__init__(strategy_engine, strategy_name, vt_symbols, setting)

        self.boll_up: Dict[str, float] = {}
        self.boll_down: Dict[str, float] = {}
        self.cci_value: Dict[str, float] = {}
        self.atr_value: Dict[str, float] = {}
        self.intra_trade_high: Dict[str, float] = {}
        self.intra_trade_low: Dict[str, float] = {}

        self.targets: Dict[str, int] = {}
        self.last_tick_time: datetime = None

        self.ams: Dict[str, ArrayManager] = {}
        for vt_symbol in self.vt_symbols:
            self.ams[vt_symbol] = ArrayManager()
            self.targets[vt_symbol] = 0

        self.pbg = PortfolioBarGenerator(self.on_bars, 2, self.on_2hour_bars, Interval.HOUR)
```

1. Inherit the strategy template through the super( ) method, and pass the strategy engine, strategy name, vt_symbols, and parameter settings in the __init__( ) function (all of the above parameters are automatically passed by the strategy engine when creating a strategy instance using the strategy class, and do not need to be set by the user).

2. Create a strategy that holds the ArrayManager instances for the different contracts and a dictionary of strategy variables.

3. Create ArrayManager and target position variables for each contract traded by the strategy and place them in the dictionary.

The default length of the ArrayManager is 100, if you need to adjust the length of the ArrayManager, you can pass in the size parameter to adjust it (size cannot be smaller than the cycle length of the calculated indicator).

4. Call the PortfolioBarGenerator module: synthesize Tick data into 1-minute bar data by time slicing. If required, longer time period data can also be synthesized, e.g. 15-minute bar.

If you only trade based on on_bar, the code here can be written as:

```python 3
        self.pbg = PortfolioBarGenerator(self.on_bars)
```

Instead of passing the pbg instance the longer K-period that needs to be synthesized based on the on_bars period, and the name of the function that receives the longer K-period.

Please note:

 - When synthesizing X-minute lines, X must be set to a number divisible by 60 (except for 60). There is no such restriction for hourly line synthesis.

 - PortfolioBarGenerator's default data frequency for synthesizing long period barrs based on the on_bar function is at the minute level, if you need to trade based on synthesized hourly or longer period barrs, please import Interval at the top of the strategy file and pass in the corresponding data frequency to the bg instance.

 - **self.on_hour_bars function name is used inside the program**, if you need to synthesize 1 hour bar, please use self.on_1_hour_bars or other naming.

### Functions called by the strategy engine

The update_setting function in StrategyTemplate and the four functions that start with get after this function, as well as the update_trade and update_order functions, are all functions that the strategy engine is responsible for calling, and generally do not need to be called when the strategy is being written.

### Strategy callback functions

Functions that begin with on in StrategyTemplate are called callback functions, and can be used to receive data or status updates when writing a strategy. The purpose of a callback function is that it is automatically called by the strategy engine when an event occurs (no active action is required in the strategy). Callback functions can be categorized into the following two types according to their function:

#### Strategy instance state control (required for all policies)

**on_init**

* Incoming reference: none

* Outgoing parameter: none

The on_init function is called when initializing a strategy. The default method is to call the write_log function to output the "strategy initialization" log, and then call the load_bars function to load the historical data. This is shown in the code below:

```python 3
    def on_init(self).
        """
        Callback when strategy is inited.
        """
        self.write_log("Strategy initialization")
        self.load_bars(10)
```

Unlike CTA strategies, multi-contract portfolio strategies only support bar backtesting, so multi-contract strategy templates do not have a load_ticks function.

When the strategy is initialized, the inited and trading status of the strategy are both [False], at this time, it just calls ArrayManager to calculate and cache the relevant calculation indicators, and cannot issue trading signals. After calling the on_init function, the inited state of the strategy is changed to [True], the strategy initialization is completed.

**on_start**

* Input parameter: none

* Output parameter: none

The on_start function is called when the strategy is started, and by default the write_log function is called to output the "strategy start" log, as shown in the following code:

```python 3
    def on_start(self).
        """
        Callback when strategy is started.
        """
        self.write_log("Strategy started")
```

After calling the strategy's on_start function to start the strategy, the strategy's trading state changes to [True], and only then can the strategy send out trading signals.

**on_stop

* Input parameter: none

* Exit parameter: none

The on_stop function is called when the strategy is stopped, the default is to call write_log to output the "strategy stopped" log, as shown in the code below:

```python 3
    def on_stop(self).
        """
        Callback when strategy is stopped.
        """
        self.write_log("Strategy stopped")
```

After calling the strategy's on_stop function to stop the strategy, the strategy's trading status changes to [False], at which point the strategy will not emit trading signals.

#### Receiving data, calculating indicators, issuing trading signals

**on_tick**

* Input parameter: tick: TickData

* Output parameter: none

The vast majority of trading systems only provide Tick data push. Even if some platforms can provide bar data push, the speed of these data arriving at the local computer will be slower than that of Tick data push, because it also needs to be synthesized by the platform before it can be pushed over. So in live trading, all the strategies in VeighNa have their bars synthesized from the Tick data received.

The on_tick function is called when the strategy receives the latest tick data from the live market. The default way to write this is to push the received tick data into the pbg instance created earlier in order to synthesize the 1-minute bar through the PortfolioBarGenerator's update_tick function, as shown in the code below:

```python 3
    def on_tick(self, tick: TickData).
        """
        Callback of new tick data update.
        """
        self.pbg.update_tick(tick)
```

Note that the on_tick function will only be called in live trading, backtesting is not supported.

**on_bars**

* Input: bars: Dict[str, BarData]

* out parameter: none

The on_bars function is called when the strategy receives the latest bar data (the default push is a one-minute bar based on Tick Synthesis for live trading, and for backtesting it depends on the frequency of the bar data filled in when selecting the parameters).

Unlike the CTA strategy module, the Multi-Contract Portfolio strategy module receives the bar pushes through the on_bars callback function to receive the bar data of all the contracts at that point in time at once, rather than through the on_bar function to receive them one by one (there is no way to determine whether the bar at the current point in time has all gone through).

There are two ways of writing this that have appeared in the example strategy:

1. If the strategy is based on on_bars advances to the bar transaction, then please write the transaction request class function under the on_bars function (because this example strategy class PortfolioBollChannelStrategy is not based on the on_bars transaction, so not an example of the explanation. Sample code based on on_bars trading can refer to other sample strategy);

2. If the strategy needs to be based on on_bars advances to the bar data through the PortfolioBarGenerator synthesized longer period of the bar to trade, then please on_bars in the call PortfolioBarGenerator update_bars function, the received bars into the previously created pbg instance, as shown in the code below:

```python 3
    def on_bars(self, bars: Dict[str, BarData]):
        """
        Callback of new bars data update.
        """
        self.pbg.update_bars(bars)
```

The sample strategy class PortfolioBollChannelStrategy is used to generate signals from 2-hour bar data returns. There are three parts in total, as shown in the code below:

```python 3
    def on_2hour_bars(self, bars: Dict[str, BarData]):
        """"""
        self.cancel_all()

        for vt_symbol, bar in bars.items():
            am: ArrayManager = self.ams[vt_symbol]
            am.update_bar(bar)

        for vt_symbol, bar in bars.items():
            am: ArrayManager = self.ams[vt_symbol]
            if not am.inited:
                return

            self.boll_up[vt_symbol], self.boll_down[vt_symbol] = am.boll(self.boll_window, self.boll_dev)
            self.cci_value[vt_symbol] = am.cci(self.cci_window)
            self.atr_value[vt_symbol] = am.atr(self.atr_window)

            current_pos = self.get_pos(vt_symbol)
            if current_pos == 0:
                self.intra_trade_high[vt_symbol] = bar.high_price
                self.intra_trade_low[vt_symbol] = bar.low_price

                if self.cci_value[vt_symbol] > 0:
                    self.targets[vt_symbol] = self.fixed_size
                elif self.cci_value[vt_symbol] < 0:
                    self.targets[vt_symbol] = -self.fixed_size

            elif current_pos > 0:
                self.intra_trade_high[vt_symbol] = max(self.intra_trade_high[vt_symbol], bar.high_price)
                self.intra_trade_low[vt_symbol] = bar.low_price

                long_stop = self.intra_trade_high[vt_symbol] - self.atr_value[vt_symbol] * self.sl_multiplier

                if bar.close_price <= long_stop:
                    self.targets[vt_symbol] = 0

            elif current_pos < 0:
                self.intra_trade_low[vt_symbol] = min(self.intra_trade_low[vt_symbol], bar.low_price)
                self.intra_trade_high[vt_symbol] = bar.high_price

                short_stop = self.intra_trade_low[vt_symbol] + self.atr_value[vt_symbol] * self.sl_multiplier

                if bar.close_price >= short_stop:
                    self.targets[vt_symbol] = 0

        for vt_symbol in self.vt_symbols:
            target_pos = self.targets[vt_symbol]
            current_pos = self.get_pos(vt_symbol)

            pos_diff = target_pos - current_pos
            volume = abs(pos_diff)
            bar = bars[vt_symbol]
            boll_up = self.boll_up[vt_symbol]
            boll_down = self.boll_down[vt_symbol]

            if pos_diff > 0:
                price = bar.close_price + self.price_add

                if current_pos < 0:
                    self.cover(vt_symbol, price, volume)
                else:
                    self.buy(vt_symbol, boll_up, volume)
            elif pos_diff < 0:
                price = bar.close_price - self.price_add

                if current_pos > 0:
                    self.sell(vt_symbol, price, volume)
                else:
                    self.short(vt_symbol, boll_down, volume)

        self.put_event()
```

- Empty unfilled commissions: In order to prevent the previously placed orders from being unfilled in the last 2 hours, but the price may have been adjusted in the next 2 hours, the cancel_all() method is used to immediately revoke all previously unfilled commissions, ensuring that the entire state of the strategy at the beginning of this current 2 hours is clear and unique;

- Call the bar time series management module: based on the latest 2-hour bar data to calculate the corresponding technical indicators, such as the upper and lower Bollinger Bands, CCI indicators, ATR indicators and so on. First get the ArrayManager object, and then push the received bar in, check the initialization status of the ArrayManager, if it has not yet been initialized successfully directly return, there is no need to go to the subsequent transaction-related logic judgment. Because many technical indicators require a minimum number of bars, if the number is not enough, the calculated indicator will be wrong or meaningless. On the contrary, if there is no return, you can start calculating technical indicators;

- Signal Calculation: Through the judgment of the position as well as the combination of CCI indicators, ATR indicators in the channel breakout point hung ** limit order commission ** (buy/sell), while setting the exit point (short/cover).

    Please note:
    1. In the CTA strategy module, position determination is usually done by accessing the strategy's variable pos to get the strategy position. But in the multi-contract portfolio strategy module, it is through the call get_pos function to get the current position of a contract for logical judgment, and then set the target position of the contract, and finally through the target position and the difference between the actual position to make logical judgments and then issue trading signals;

    2. If you need to refresh the indicator values in the graphical interface, please do not forget to call the put_event() function.

#### Delegation Status Update

Because of the need to trade multiple contracts at the same time in the portfolio strategy, it is not possible to determine the order of each contract's commission transaction within a certain bar during backtesting, so it is not possible to provide the on_order and on_trade functions to get the commission transaction push, but only through the get_pos and get_order to perform the relevant status query each time the on_bars callback. query.

### Active functions

**buy**: buy to open position (Direction: LONG, Offset: OPEN)

**sell**: sell to close position (Direction: SHORT, Offset: CLOSE)

**short**: sell to open (Direction: SHORT, Offset: OPEN)

**cover**: buy to close position (Direction: LONG, Offset: CLOSE)

* Input parameter: vt_symbol: str, price: float, volume: float, lock: bool = False, net: bool = False

* out reference: vt_orderids: List[str] / none 

buy/sell/short/cover are all trade request class functions within the strategy that are responsible for issuing orders. Strategies can use these functions to send trade signals to the strategy engine for the purpose of placing orders.

The following buy function code as an example, you can see, ** the specific contract to be traded code **, the price and quantity are required parameters, lock conversion and net position conversion is the default False. you can also see that the function received the parameters passed in the internal StrategyTemplate call send_order function to send an order (because it is the buy) order, it automatically fills in the direction as LONG and the open as OPEN).

Unlike the CTA strategy module, the Portfolio Strategy module does not provide a local stop order function, so the stop parameter is removed from the delegate function.

If lock is set to True, then the order will lock the commission conversion (in the case of today's position, if you want to close the position, it will first close all the yesterday's position, and then the rest of the part of the reversal of the position instead of closing today's position, in order to avoid closing today's commission penalties).

If net is set to True, then the order will be converted to a net position (based on all positions in the overall account, the opening and closing directions of the order under the strategy will be converted according to the net position holding method). However, the net position trading mode is mutually exclusive with the lock trading mode, so when net is set to True, lock must be set to False.

Please note that if you send a close order to SFE, because the exchange must specify close today, close yesterday, the bottom will automatically convert its close order. Because some varieties of the Shanghai Futures Exchange have a flat today preference, so the default is to send commissions with flat today priority (if the underlying of the transaction in the Shanghai Futures Exchange flat yesterday is more preferential, you can do your own in vnpy.trader.converter's convert_order_request_shfe function to make the appropriate changes).

```python 3
    def buy(self, vt_symbol: str, price: float, volume: float, lock: bool = False, net: bool = False) -> List[str].
        """
        Send buy order to open a long position.
        """
        return self.send_order(vt_symbol, Direction.LONG, Offset.OPEN, price, volume, lock, net)
```

Please note that the domestic futures have the concept of open and close positions, for example, buy operations should be distinguished as buy open and buy close; but for stocks, foreign futures are net position mode, there is no open and close the concept of the position, so only need to use the buy (BUY) and sell (SELL) these two instructions can be.

**send_order**

* Input: vt_symbol: str, direction: Direction, offset: Offset, price: float, volume: float, lock: bool = False, net: bool = False

* Exit: vt_orderids: List[str] / None

The send_order function is a function called by the strategy engine to send delegates. Generally do not need to be called separately when the strategy is written, through the buy/sell/short/cover function to send limit commissions can be.

Real-time, after receiving the parameters passed in, will call round_to function based on the contract's pricetick and min_volume on the commission of the price and quantity.

Please note that only after the start of the strategy, that is, after the strategy's trading status has changed to [True], you can send trading commissions. If the function is called when the strategy's trading status is [False], it will only return [].

**cancel_order**

* Input parameter: vt_orderid: str

* Output: none

**cancel_all**

* Input: none

* Exit: none

cancel_order and cancel_all are both trade request functions that are responsible for canceling orders. cancel_order is to cancel the specified active orders within the strategy, while cancel_all is to cancel all active orders of the strategy.

Please note that the order can only be withdrawn after the strategy has been activated, that is, after the trading status of the strategy has changed to [True].

### Function Functions

The following are function functions outside of the strategy:

**get_pos**

* Input: vt_symbol: str

* Output: int / 0 

Call the get_pos function within a strategy to get position data for a specific contract.

**get_order**

* Input parameter: vt_orderid

* Output parameter: orderData / none

Call the get_order function in a strategy to get the order data for a specific contract.

**get_all_active_orderids**

* Input parameter: None

* Output: List[OrderData] / None

Call the get_all_active_orderids function in a strategy to get all current active delegate numbers.

**get_pricetick**

* Input parameter: vt_symbol

* Outgoing reference: pricetick: float / None

Call the get_price function in the strategy to get the minimum price tick for a specific contract.

**write_log**

* Input parameter: msg: str

* Output parameter: none

Call the write_log function in a strategy to perform a log output of the specified content.

**load_bars** * Input: days: str * Output: none

* Input: days: int, interval: Interval = Interval.MINUTE

* Outgoing parameters: none

Calling the load_bars function in a strategy allows you to load bar data when the strategy is initialized.

As shown in the code below, when the load_bars function is called, the default number of days to load is 10 and the frequency is one minute, which corresponds to loading 10 days of 1-minute bar data. In backtesting, 10 days refers to 10 trading days, while in the real market, 10 days refers to natural days, so it is recommended to load the number of days rather than too few. Loading will first try to get historical data through the trading interface, data service, and database in turn until it gets historical data or returns null.

```python 3
    def load_bars(self, days: int, interval: Interval = Interval.MINUTE) -> None.
        """
        Load historical bar data for initializing strategy.
        """
        self.strategy_engine.load_bars(self, days, interval)
```

**put_event**

* Input parameter: none

* Output parameter: none

Calling the put_event function in a strategy notifies the GUI to refresh the strategy state related display.

Please note that the GUI can only be refreshed after the initialization of the strategy is completed and the inited state is changed to [True].

**send_email**

* Input: msg: str

* Output parameter: none

After configuring the mailbox information (see Global Configuration section in Basic Usage for details), call send_email function in the strategy to send emails with specified content to your own mailbox.

Please note that you can only send emails after the initialization of the strategy is completed and the inited state is changed to [True].

**sync_data**

* Input parameter: none

* Outgoing parameter: none

Call sync_data function in the strategy, you can synchronize the strategy variables into the json file for local caching every time you stop or close a deal in the real market, so that you can easily read and restore them the next day when you initialize the strategy (the strategy engine will call it, no need to call it actively in the strategy).

Please note that the strategy information can only be synchronized after the strategy has been launched, that is, after the trading status of the strategy has changed to [True].

## Multi-Contract StrategyTemplate - Advanced

The PortfolioStrategy module is designed for quantitative strategies with multiple underlying portfolios, which seek to adjust the positions of the strategy portfolio to the target state at the execution level without paying too much attention to the underlying commission trading details.

First of all, we introduce the functional functions of position target adjustment trading to show the functional support of position target adjustment trading:

### Functional introduction to position target adjustment trades

The following are the functional functions called by the strategy in the Position Target Adjustment Trading mode:

**set_target**

* Input parameter: vt_symbol: str, target: int

* Output: none

The set_target function is called in a strategy to set a target position for a specific contract.

Please note that the target position is a persistent state, so it is set and will continue to be set at subsequent times until it is set again.

**get_target**

* Input parameter: vt_symbol: str

* Outgoing parameter: int

The get_target function is called from within a strategy to retrieve a set target position for a specific contract.

Please note that the state of the strategy's target position is automatically persisted to a hard disk file at sync_data (closed, stopped, etc.) and is restored when the strategy is restarted.

**rebalance_portfolio**

* Input parameter: bars: Dict[str, BarData]

* Outgoing reference: none

Calling the rebalance_portfolio function from within a strategy allows you to execute a position reversal trade based on a set target position for a specific contract.

Please note: Only contracts that have a bar in the current bars dictionary will participate in the execution of this position adjustment trade, thus ensuring that contracts in non-trading sessions (no market push) will not be incorrectly issued commissions.

**calculate_price**

* Input parameter: vt_symbol: str, direction: Direction, reference: float

* out reference: pricetick: float

Overloading the calculate_price function in a strategy allows you to set the target price for a specific contract on demand (e.g. fixed price overrun, fixed pricetick overrun, percentage overrun, etc.).

If not passed then the default return to the reference price (if not overloaded in the strategy, in the rebalance_portfolio function to the closing price of the K line as the commission price issued).

### Example of the use of the function function of the position target adjustment trade

The biggest difference between the Position Target Adjustment Trading function and the base usage of StrategyTemplate lies in the processing differences in the strategy on_bars function. The following is an example of a TrendFollowingStrategy strategy to show the exact steps of a position target adjustment trade:

**on_bars**

* Input parameter: bars: Dict[str, BarData]

* out parameter: none

The on_bars function is called when the strategy receives the latest bar data (the default advance is a one-minute bar based on Tick Synthesis for live trades, and for backtests it depends on the frequency of the bar data that was filled in when the parameter was selected).

The example strategy class TrendFollowingStrategy is used to generate signals from one-minute bar data returns. There are three parts, as shown in the code below:

```python 3
    def on_bars(self, bars: Dict[str, BarData]) -> None:
        """Bar Slice Retracement""""
        # Update the bar to calculate the RSI value
        for vt_symbol, bar in bars.items():
            am: ArrayManager = self.ams[vt_symbol]
            am.update_bar(bar)

        for vt_symbol, bar in bars.items():
            am: ArrayManager = self.ams[vt_symbol]
            if not am.inited:
                return

            atr_array = am.atr(self.atr_window, array=True)
            self.atr_data[vt_symbol] = atr_array[-1]
            self.atr_ma[vt_symbol] = atr_array[-self.atr_ma_window:].mean()
            self.rsi_data[vt_symbol] = am.rsi(self.rsi_window)

            current_pos = self.get_pos(vt_symbol)
            if current_pos == 0:
                self.intra_trade_high[vt_symbol] = bar.high_price
                self.intra_trade_low[vt_symbol] = bar.low_price

                if self.atr_data[vt_symbol] > self.atr_ma[vt_symbol]:
                    if self.rsi_data[vt_symbol] > self.rsi_buy:
                        self.set_target(vt_symbol, self.fixed_size)
                    elif self.rsi_data[vt_symbol] < self.rsi_sell:
                        self.set_target(vt_symbol, -self.fixed_size)
                    else:
                        self.set_target(vt_symbol, 0)

            elif current_pos > 0:
                self.intra_trade_high[vt_symbol] = max(self.intra_trade_high[vt_symbol], bar.high_price)
                self.intra_trade_low[vt_symbol] = bar.low_price

                long_stop = self.intra_trade_high[vt_symbol] * (1 - self.trailing_percent / 100)

                if bar.close_price <= long_stop:
                    self.set_target(vt_symbol, 0)

            elif current_pos < 0:
                self.intra_trade_low[vt_symbol] = min(self.intra_trade_low[vt_symbol], bar.low_price)
                self.intra_trade_high[vt_symbol] = bar.high_price

                short_stop = self.intra_trade_low[vt_symbol] * (1 + self.trailing_percent / 100)

                if bar.close_price >= short_stop:
                    self.set_target(vt_symbol, 0)

        self.rebalance_portfolio(bars)

        self.put_event()
```

- Call the bar time series management module: based on the latest minute bar data to calculate the corresponding technical indicators, such as the ATR indicator, RSI indicator and so on. First get the ArrayManager object, and then push the received bar in, check the initialization status of the ArrayManager, if it has not been initialized successfully on the direct return, there is no need to go to the subsequent transaction-related logic judgment. Because many technical indicators require a minimum number of bars, if the number is not enough, the calculated indicator will be wrong or meaningless. On the contrary, if there is no return, you can start calculating technical indicators;

- Calculation of signals: by determining the position (get_pos) and combining the results of the indicator calculations at the channel breakout point **setting the target position** (set_target)

- Execute a position adjustment transaction (rebalance_portfolio)

**calculate_price**

* Input: vt_symbol: str, direction: Direction, reference: float

* out parameter: prcie: float

When the rebalance_portfolio function detects a difference between the target position and the actual position, it calls the calculate_price function to calculate the price of the adjustment commission.

The default way to write this function within the strategy is to calculate the commission price based on the set price_add for the direction of the commission, or you can refer to the example strategy PairTradingStrategy for calculating the commission price based on the set tick_add.

```python 3
    def calculate_price(self, vt_symbol: str, direction: Direction, reference: float) -> float.
        """Calculate the price of a transfer commission (on-demand reloading implementation supported)""""
        if direction == Direction.
            price: float = reference + self.price_add
        LONG: price: float = reference + self.price_add
            price: float = reference - self.price_add

        return price
```

### Differences from the base usage of StrategyTemplate

**on_bars**

1. There is no need to clear the outstanding commissions: the logic to call cancel_all function is already present in the rebalance_portfolio, so there is no need to call cancel_all function to withdraw the outstanding commissions when you receive a push from the on_bars function.

2. No need to use self.targets dictionary to cache the contract target position: directly call set_target function to pass in the contract and the target position (a positive number represents a long position, a negative number represents a short position) can be set.

3. No need to hand-write the commissioning logic based on the cached target position within the strategy: the rebalance_portfolio function has automatically taken over the transfer transaction, will be based on the target position for commissioning.

**calculate_price**

Position target transfer transactions need to call the calculate_price function to calculate the transfer commission price.
