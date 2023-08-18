# Features

As a Python-based quantitative trading program development framework, VeighNa is dedicated to providing quantitative solutions from trading API docking to strategy automated trading.

## Target Users

If you have the following needs, you may want to try VeighNa:

* Develop your own quantitative trading program based on Python language, and take full advantage of the powerful data research and machine learning ecosystem of Python community.
* Use a standardized trading platform to connect to many different types of financial markets at home and abroad: securities, futures, options, and foreign markets.
* Using a well-tested quantitative strategy engine to complete the entire business process from data maintenance, strategy development, backtesting research to real-time automated trading.
* Customize and extend the platform to meet individual trading needs: add trading interfaces, modify the GUI, and develop complex strategy applications based on event-driven engines.
* Control the source code details of the trading program, eliminating all kinds of program backdoors, avoiding the risk of strategy theft, interception of trading signals, theft of account passwords and so on.
* Save the cost of capital for quantitative trading platforms, do not have to spend tens of thousands of annual software license fees or additional points for each transaction


## Application Scenarios

From professional individual investors, entrepreneurial private equity, to brokerage management departments, all can find VeighNa application scenarios.

* Professional individual investors: use VeighNa Trader to directly connect to the CTP futures counters of futures companies, realizing the CTA business process from strategy development to real trading automation.
* Entrepreneurial private equity: Based on RpcService to build a unified server-side reporting channel, allowing traders to develop all kinds of trading strategy applications on their own local computers.
* Securities firms' asset management departments: docking with the O32 asset management system deployed by securities firms, and customizing the development of multi-strategy complex systems based on the event-driven engine.


## Supported interfaces

**vnpy.gateway**, covering trading interfaces for all trading varieties at home and abroad:

* Domestic market

  * CTP (ctp): futures, futures options

  * CTP Test (ctptest): futures, futures options

  * CTP Mini (mini): futures, futures options

  * Pegasus (femas): futures

  * CTP Options (sopt): options on ETFs

  * Vertex Filtron (sec): ETF options

  * Vertex HTS (hts): ETF options

  * Hang Seng UFT (uft): futures, ETF options

  * esunny (esunny): futures, gold td

  * Zhongtai XTP (xtp): A-shares, two financing, ETF options

  * Guotai Junan unified trading gateway (hft): A shares, two financing

  * Huaxin singularity stock (torastock): A shares

  * Huaxin Qidian Options (toraoption): ETF options

  * Zhongyi Huida Comstar (comstar): interbank market

  * Orient Securities OST (ost): A shares

  * Ronghang (rohon): futures custody

  * TTS (tts): futures

  * Flying Mouse (sgit): Gold TD

  * Jinshida Gold (ksgold): Gold TD

* Overseas Markets

  * Reuters Securities (ib): overseas multi-species

  * eSun 9.0 foreign exchange (tap): foreign exchange futures

  * Directly to the futures (da): foreign exchange futures

* Specialty Applications

  * RPC service (rpc): cross-process communication interface for distributed architecture


## Supported applications

**vnpy.app**, out-of-the-box trading application for various quantitative strategies:

* cta_strategy: CTA strategy engine module, while maintaining ease of use, allowing users to CTA type strategy running process entrusted to the report withdrawal behavior for fine-grained control (reduce trading slippage, realize high-frequency strategy)

* cta_backtester: CTA strategy backtesting module, without the need to use Jupyter Notebook, direct use of the graphical interface to directly analyze the strategy backtesting, parameter optimization and other related work.

* spread_trading: multi-contract spread arbitrage module, in addition to allowing users to manually start the algorithm to buy and sell spreads, but also supports the use of strategy templates SpreadStrategyTemplate to develop a variety of quantitative trading strategy spreads.

* algo_trading: algorithmic trading module, provides a variety of commonly used smart trading algorithms: TWAP, Sniper, Iceberg, BestLimit and so on. Support commonly used algorithms to save the configuration

* option_master: option volatility trading module, provides volatility curve charts, allowing users to make the appropriate judgment and analysis, and then use the volatility management component to set the pricing reference volatility, and then you can automatically scan the market through the option electronic eye algorithms trading opportunities and instantaneous completion of the transaction

* portfolio_strategy: multi-contract portfolio strategy module, designed specifically for quantitative strategies that require simultaneous trading of multiple contracts to meet the needs of their historical data backtesting and real-time automated trading.

* script_trader: script strategy module, designed for multi-subjective portfolio trading strategy design, but also can be realized directly on the command line in the form of REPL instruction trading, does not support the backtesting function

* chart_wizard: real-time K-line chart module, you can realize simple real-time K-line market display, directly in the local contract code edit box, enter vt_symbol, click on the [New Chart] button will open the corresponding contract's chart.

* rpc_service: RPC service module, allowing a VeighNa Trader process to be started as a server, as a unified quote and trade routing channel, allowing multiple clients to connect simultaneously, to achieve multi-process distributed system.

* excel_rtd: EXCEL RTD module, RTD full name is RealTimeData, is Microsoft's main for the financial industry's real-time data needs designed for Excel data docking program. This module is used to realize the function of accessing any data information within the VeighNa program in Excel.

* data_manager: Historical data management module, is a multi-functional management tool for historical data within VeighNa Trader. Can support data import, data view and data export and other functions, support for customizing the data table header format.

* data_recorder: Quotes recording module, based on the graphical interface for configuration, according to the needs of real-time recording Tick or K-line quotes into the database, for strategy backtesting or initialization of the real market.

* risk_manager: risk management module, providing statistics and restrictions on trading flow control, number of orders placed, active commissions, total number of withdrawn orders and other rules, effectively realizing the front-end risk control function.

* web_trader: Web service module, designed for B-S architecture requirements, realizes a Web server that provides active function calls (REST) and passive data push (Websocket).

* portfolio_manager: portfolio management module, the module is mainly oriented to a variety of investors using fundamental strategies, for each investment strategy, to create an independent portfolio strategy objects

* paper_account: simulation trading account module, in order to solve the current need to rely on various types of server-side functions of the simulation trading account, directly within the trading client to provide a set of localized simulation of the trading environment, at the same time, based on the real market quotations of the stock market data for the commissioning of the aggregator


## Generic components

**vnpy.event**, a simple and easy-to-use event-driven engine that serves as the core of an event-driven trading program.

**vnpy.chart**, Python high-performance K-line charts, support for large-data-volume chart display and real-time data update function.

**vnpy.trader.database**, integrates several database management side modules to support database read/write performance and future new database extensions.

**vnpy.trader.datafeed**, provides a standardized interface BaseDataFeed, bringing more flexible data service support.
