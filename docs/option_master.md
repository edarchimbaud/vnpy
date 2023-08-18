# OptionMaster - Option Volatility Trading Module

## Functional Description

OptionMaster is a functional module for **Options Volatility Trading**, which allows users to accomplish real-time options pricing, volatility surface tracking, position Greek value monitoring, portfolio stress testing, electronic eye auto trading and other functions.


### Load startup

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check [OptionMaster] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_optionmaster import OptionMasterApp

# Write after creating the main_engine object
main_engine.add_app(OptionMasterApp)
```


## Start the module

After starting VeighNa Trader, click [Functions] -> [Option Trading] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/1.png)

You can enter the OptionMaster management interface (hereinafter referred to as the management interface), as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/2.png)


## Configure Portfolio

In the management interface, select the option product to be traded and click the [Configure] button to open the Portfolio Configuration dialog box as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/3.png)


The configuration parameters are as follows:

* Pricing model
  * Black-76 model: for European-style futures options (stock index options);
  * Black-Scholes model: for European-style stock options (ETF options);
  * Binomial-Tree model: for American-style futures options (commodity options);
* Annualized Interest Rate
  * Risk-free discount rate used in pricing models;
* Contract models
  * Positive: Includes most products such as ETF options, futures options, and stock index options;
* Greeks Decimal Places
  * The number of decimal places retained when displaying Greek values;
* Pricing Underlying corresponding to the option chain
  * Note that only option chains with selected underlying will be added to the trading portfolio;
  * Pricing Underlying Support
    * Futures contracts: futures prices provided by the exchange itself;
    * Synthetic Futures: synthetic futures prices calculated based on option prices;
    * OptionMaster automatically corrects the premium and discount of the underlying price relative to the option chain during the pricing calculation process, so it is recommended to select the most actively traded contract as the underlying.

Click the [Confirm] button at the bottom to complete the initialization of the option portfolio. At this point, the [Configuration] button on the management interface will be locked, while other buttons will be activated.


## Quote Monitoring

Click the [T-quotes] button on the management interface to open the T-quotes window:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/4.png)

The whole window is divided into left and right areas, with the white column in the center as the strike price, call options on the left, and put options on the right.

Each line displays the information corresponding to an option with a certain strike price, and the information displayed from the outside inward includes:

* Contract Code
* The real-time cash Greek value of the option
  * Vega
  * Theta
  * Gamma
  * Delta
* Transaction information
  * Positions
  * Volume
* 1-step order information
  * Buy Hidden Wave
  * Buy Volume
  * Bid price
  * Sell price
  * Sell volume
  * Sell Hidden Wave
* Net position


## Quick Trade

Click the [Quick Trade] button in the management interface to open the manual order window:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/5.png)

The overall usage is similar to the trading component of VeighNa Trader's main interface. After entering the contract code, bid/offer direction, open/close direction, trading price and quantity, click the [Entrust] button to issue a Limit Entrustment, and click the [All Withdrawal] button to all withdraw all current active entries with one click.

Double-click the cell of an option in the T-quote to quickly populate the [Code] edit box in this window.


## Position Greek Value

Click the [Position Greek] button in the management interface to open the Greek Risk Monitoring window:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/16.png)

The monitoring information in the window is divided into four dimensions:

* Trading Portfolio (including all subordinate option chains and underlying aggregated data)
* Underlying Contracts
* Option Chain (including all subordinate option summary data)
* Option Contracts

The monitoring information for each dimension includes:

* Position Related
  * Long Positions: current long positions
  * Short position: current short position
  * Net Position: Long Position - Short Position
* Total Greek value
  * Delta: the amount of profit and loss in this dimension corresponding to a 1% rise or fall in the underlying price
  * Gamma: 1% increase or decrease in the underlying price corresponds to the change in the dimension of the Delta
  * Theta: the amount of profit and loss in this dimension for each past trading day
  * Vega: the amount of profit/loss in this dimension corresponding to a 1% increase or decrease in implied volatility.

## Appreciation and discount monitoring

Clicking on the Appreciation Monitor button in the administration interface opens the window for monitoring the calibrated range of the Appreciation and Discount of the Option Chain Pricing:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/6.png)

As you can see in the above figure as an example:

* IO2104, priced with the corresponding month's futures IF2104, has an uplift and discount close to 0;
* IO2105, IO2106, IO2109, priced on active contract IF2104, with the discount increasing in turn;
* IO2112, IO2203, priced with synthetic futures for the corresponding month, with an uplift and discount of 0.


## Volatility Curve

Click the [Volatility Curve] button in the management interface to open the current market volatility curve monitoring chart:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/7.png)

The volatility curves of each option chain in the chart are displayed in different colors, the legend of the specific color corresponding to the option chain is on the left side.

Each option chain will include three curves:

* Upward arrow: the median 1-step intraday implied volatility for that month's call option, i.e., the average of the bid-1 and ask-1 intraday volatilities;
* Downward arrow: the median of the 1-strike implied volatility of the put options priced for that month;
* Dot: the value of the priced volatility for the month, the priced volatility is used for Greek value calculation and electronic eye trading and is set through the [Volatility Management] component at the back.

The curves displayed in the chart are controlled by the checkboxes corresponding to each option chain at the top of the window, which can be adjusted according to the needs, as in the following chart only one option chain, IO2109, is displayed:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/17.png)


## Delta Hedge

Click the [Delta Hedge] button in the management interface to turn on the Delta auto hedge function of the trading portfolio:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/8.png)

* Underlying Hedge: You can select any one of the underlying contracts within the portfolio;
* Execution frequency: how often to execute the check to determine whether to execute the hedge;
* Delta target: if the hedge is triggered, hedge the Delta value to how much;
  * Select 0, which is to keep the overall portfolio Delta neutral;
  * Positive, which is to maintain a long Delta exposure for the overall portfolio;
  * A negative number is selected to maintain a short Delta exposure for the overall portfolio;
* Delta Range: triggers a hedge mandate when the Delta value of a position type deviates by more than the above Delta target;
* Entrusted Overpricing: the price overpricing relative to the opposite side of the market at the time of issuing the hedging mandate;

Click the [Start] button to start the automatic hedging function. A check will be performed when the reading reaches the execution interval, and if the conditions are met, the TWAP algorithm will be activated to execute the hedging operation.

Click the [Stop] button to stop the automatic hedging function.

## Scenario Analysis

Click the [Scenario Analysis] button in the management interface to open the function of stress test and scenario analysis of the overall position risk of the trading portfolio:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/9.png)

First configure the analysis tasks to be performed:

* Target Data: Profit/Loss, Delta, Gamma, Theta, Vega are supported;
* Time decay: number of days of decay of the trading day;
* Price movement:
  * The range of price movements in the analysis of up and down;
  * Assuming a pre-order price of 100 and a 10% change, the range is 90 to 110;
* Volatility Change:
  * Range of upward and downward movements of volatility in the analysis;
  * Range from 10% to 30% assuming current volatility is 20% and change is 10%.

After clicking the Execute Analysis button, the stress test engine will calculate the corresponding target data based on the current trading portfolio positions, as well as the price and implied volatility scenarios for each scenario, and plot the results as a 3D surface.

The graph below shows the results for a 10% price change and a 15% volatility change using the Gamma value as the calculated target:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/18.png)

The vertical axis in this 3D graph is the value of the calculation target, and the horizontal axes are the values of the price and volatility movements.


## Volatility Management

Click the [Volatility Management] button in the management interface to open the Pricing Volatility Management interface:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/11.png)

Click the Option Chain tab at the top to switch the Pricing Volatility Management component of the corresponding option chain. When you open it for the first time, the values of [Pricing Hidden Volatility] in the table below are all zero.

First of all, initialize the pricing curve, click the [Reset] button at the top to map the median implicit wave of the current strike price of the dummy option to the pricing implicit wave.

After the mapping is complete, you can view the current shape of the pricing volatility curve in the Volatility Chart, and if the pricing hermitian of a strike price is not smooth compared to the overall curve, you can fit it based on the pricing hermitian of a relatively smooth strike price.

In the "Perform Fitting" column of the component form, check the checkboxes of the strike prices to be fitted, and then click the "Fit" button at the top of the form to perform the volatility curve fitting based on OptionMaster's built-in Cubic Spline algorithm.

If you are not satisfied with the fit, you can fine-tune it manually by clicking on the scroll box in the Pricing Cubic Spline column, clicking on the up and down arrows to move up or down by 0.1% at a time, or you can directly enter the value you want to change.

When an overall panning of the curve is required because of an overall view of the volatility curve's highs and lows, you can adjust the panning of the priced volatility for all strike prices by using the [+0.1%] and [-0.1%] buttons at the top of the component.

## Electronic Eye

Click the [Electronic Eye] button in the management interface to open the Electronic Eye automatic arbitrage algorithm function for the trading portfolio:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/12.png)

The Electronic Eye algorithm can automatically capture transient trade execution opportunities that arise in the market based on the trader's preset priced volatility profile within the allowed position range, while combining with the Delta auto-hedging function to ensure the overall Delta neutrality of the portfolio.

The electronic eye interface resembles a T-shaped quote divided into the left and right areas, with the white color in the middle being the strike price, call options on the left, and put options on the right. There is a separate Electronic Eye trading algorithm for each option, and a trader can launch hundreds of trading algorithms (the exact number depends on CPU performance) at the same time without interfering with each other.

The configuration parameters for each electronic eye algorithm include:

* Trade Spread Correlation
  * Price spreads
  * Hidden wave spreads
* Position limit correlation
  * Position range
  * Target Position
* Maximum Mandate
  * Maximum number of mandates in a single trade
* Direction
  * Direction of trading allowed by the algorithm
  * Includes long-only, short-only, and two-way trades allowed

The execution process of the electronic eye algorithm is as follows:

1. calculate the **theoretical price** of the option based on the priced volatility
2. Calculate the target bid-ask spread:
   1. hidden wave spread price value = hidden wave spread * option theoretical Vega value
   2. trading spread = max(price spread, price value of hidden wave spread)
3. Calculate the target bid/ask price:
   1. Target Bid = Theoretical Price - Trading Spread / 2
   2. target ask price = theoretical price + trading spread / 2
4. Take a long trade as an example, a buy signal is triggered when the Ask 1 price is lower than the target Bid price
5. Calculate the commission volume for the current round:
   1. Algorithmic Position Limit = Target Position + Position Range
   2. Remaining Long Tradable Volume = Algorithmic Long Position Limit - Net Current Position
   3. current order quantity = min(Remaining Long Tradable Volume, Sell 1 Volume, Maximum Order Quantity)
6. Use the target bid price and the current round of orders to place the corresponding order.

After configuring the algorithm parameters, click the button in the [Pricing] column of the row to start the algorithm's pricing calculation, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/13.png)

The status of the [Pricing] and [Trading] buttons are displayed:

* If N, it means that the algorithm has not started the task.
* If it is Y, it means that the algorithm is already performing the corresponding task.

The four options algorithms that have started pricing will start updating the target bid and ask prices and other relevant values in real time.

At this point, click the button in the [Trade] column to start the algorithm's trade execution, and when the price and position meet the conditions, it will automatically issue a trade order. Detailed algorithmic operation status log information can be monitored through the log area on the right side:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/option_master/14.png)

When you need to make batch modifications to the algorithm configuration, you can use the global modification function in the upper right corner of the electronic eye window, which is more convenient and faster.

