## Version 3.7.0

## New

1. Add Shanghai and Shenzhen stock exchange enumeration values. 2.
2. Added vnpy_tap support for Linux system.
3. add vnpy_rqdata support for the new type of main contract data (switching the previous day's closing price ratio reweighting).

## Adjustment

1. vnpy_ctastrategy/vnpy_ctabacktester filter TargetPosTemplate templates when loading strategy classes.
2. vnpy_ctp connection login process to disable re-initiation of authentication only if the authorization code is wrong
3. vnpy_uft add support for GFEX in Hiroshima.
4. vnpy_tqsdk adds support for output logging.
5. vnpy_dolphindb allows specified users to configure specific database instances.
6. vnpy_rqdata optimizes the query code conversion rules for futures and options contracts on the Zhengzhou Stock Exchange.
7. vnpy_rqdata adds support for GFEX of GFEX.
8. vnpy_portfoliostrategy adds backtest position checking.
9. vnpy_portfoliostrategy adds contract multiplier query function get_size to strategy templates.
10. vnpy_portfoliostrategy backtests do not use segmented loading when loading daily and hourly data.


## Fixes

1. fix vnpy_rpcservice, the RPC interface is wrong about the vt prefix of the pushed data.
2. fix the special handling of INE positions in vnpy_mini. 3. fix the problem of vnpy_data_data.
3. fix the missing output function in vnpy_datamanager when updating batch data
4. fix the problem in vnpy_spreadtrading that when loading data for backtesting, it prioritizes to get historical data from data service, and instead prioritizes to load from local database.


# 3.6.0 Version

## New

1. add Mac system support (M1/M2) for vnpy_ctp.

## Tweaks

1. add output parameter to BaseDatafeed function to output logs.
2. Modify the related data service modules to adapt the output parameter: vnpy_rqdata/vnpy_ifind/vnpy_wind/vnpy_tushare.
3. Modify related strategy application modules to adapt output parameters: vnpy_ctastrategy/vnpy_ctabacktester/vnpy_portfoliostrategy/vnpy_spreadtrading/vnpy_datamanager
3. OffsetConverter adds support for locking mode for SHFE/INE contracts.
4. add global OffsetConverter function in OmsEngine, no longer need to be maintained by each AppEngine.
5. add a parameter to limit the maximum number of processes of the CTA strategy module when performing parameter optimization: vnpy_ctastrategy/vnpy_ctabacktester
6. add tqdm-based progress bar output during the exhaustive optimization algorithm.
7. add iteration count progress output for genetic optimization algorithm.
8. increase the matching function of option products corresponding to underlying contracts in vnpy_optionmaster module, and no longer limit the range of products.
9. upgraded the dll library of vnpy_tts to solve the problem that funds are not displayed due to the upgrade of openctp.
10. modify vnpy_ctastrategy to use the time zone defined in vnpy.trader.database to load data.
11. add vnpy_ctastrategy strategy template contract multiplier query function get_size
12. add vnpy_spreadtrading backtesting to check the performance of the statistics for the case of burst positions.
13. add vnpy_scripttrader function to query position data based on vt_symbol and direction.
14. modify the string content of vt_positionid and add the prefix gateway_name.

## Fixes

1. fix the problem of wrong parameter for the exception catching hook threading_excepthook
2. fix an exception failure when vnpy_ib fetches historical data
3. fix a problem in vnpy_rest/vnpy_websocket where the proxy parameter of aiohttp must be None when passed empty.
4. fix the problem that the number of rows of Greeks monitoring table in vnpy_optionmaster module is not set enough. 5. fix the problem that the number of rows in vnpy_ruby is not set enough.
5. fix the problem that vnpy_rqdata querying stock option data reports an error.
6. fix the problem that RqdataGateway in vnpy_rqdata gets the wrong information of futures index and continuous contract.
7. fix an issue in vnpy_portfoliostrategy where restoring data from a cached file causes defaultdict to become dict


# Version 3.5.0

## New

1. Added RqdataGateway, a new cross-market quotes data interface based on MiBasket RQData. 2.
2. Added Oriental Wealth Securities EMT counter trading interface vnpy_emt.

## Adjustments

1. adjust vnpy_algotrading module design (template, engine) to support only single contract algorithmic execution trading
2. Optimize the algorithmic state control of vnpy_algotrading, increase the state enumeration value, and the algorithm supports suspension and resumption of operation.
3. upgrading the vnpy_hft interface to support the API of the 2.0 version of the HFT Guodian Unified Trading Gateway.
4. optimize the strategy template of vnpy_portfoliostrategy to support position target adjustment trading mode.

## Fixes

1. fix the compatibility problem of the background thread exception catching hook function with Python 3.7 syntax
2. fix the issue of time period duplication when loading historical data in vnpy_mysql. 3.
3. fix vnpy_ib delegate failure issue due to TWS client upgrade.
4. fix vnpy_rest/vnpy_websocket support for asyncio after Python 3.10
5. fix vnpy_sopt to return [Commit In Progress] status when delegate fails due to flow control.


# Version 3.4.0

## New

1. New trading interface vnpy_jees for Jeyes asset management system.

## Adjustments

1. Enable the pyzmq connection keepalive mechanism of vnpy.rpc to avoid disconnection of idle connections in complex network environments.
2. remove the EVENT_TIMER timer event push in vnpy_rpcservice.
3. adjust vnpy_postgresql to write data in batch to improve efficiency.
4. add sub-thread exception catching in VeighNa Trader (requires Python>=3.8)
5. adjust vnpy_ib interface to query historical bar data, for foreign exchange and precious metals are used in the median price (rather than the transaction price)
6. add vnpy_ctastrategy for backtesting in the process of funds burst (less than or equal to 0) check the situation
7. optimize the encryption authentication of vnpy_webtrader module, and support web process shutdown and restart.

## Fixes

1. fix the NOBLOCK compatibility problem of vnpy.rpc module for pyzmq version 23.0 or above. 2. fix the NOBLOCK compatibility problem of vnpy_webtrader module.
2. fix a series of compatibility issues with vnpy_taos due to TDengine version upgrades.
3. fix vnpy_datamanager failed to remove old data points when refreshing the data summary information display.



# Version 3.3.0

## New
1. added the TickOverview object in the database component vnpy.trader.database.
2. New trading interface vnpy_gm in Nuggets simulation environment.
3. BaseData base data type add extra field (dictionary type), used to transfer any relevant data

## Adjustments
1. use Python's built-in zoneinfo library to replace the pytz library of the three parties.
2. adjust the related transaction interface, data service interface, database adapter, and application module to use the new ZoneInfo object to identify time zone information.
3. When writing data to database adapter interface vnpy.trader.database, add stream writing parameter stream to improve the performance of quote recording.


# Version 3.2.0

## New
1. added the enumeration value field GFEX of Guangzhou Futures Exchange.
2. Added vnpy_sopttest interface for CTP options (ETF) penetration testing. 3.
3. Added Currency.
4. Added Exchange.TSE (Toronto Stock Exchange) and Exchange.AMEX (American Stock Exchange) enumerations.
5. Added vnpy_taos, the TDengine timing database adapter.
5. added vnpy_timescaledb, TimescaleDB timeseries database adapter

## Adjustments
1. update vnpy_ctp/vnpy_ctptest to support Guangzhou Futures Exchange
2. update vnpy_tora's spot API interface to the latest version: API_Python3.7_Trading_v4.0.3_20220222
3. Update vnpy_tora's Options API to the latest version: API_Python3.7_v1.3.2_20211201
4. update vnpy_esunny/vnpy_tap to add a call to the API exit function when closing the interface
5. remove reverse contract support for vnpy_ctastrategy/vnpy_ctabacktester/vnpy_optionmaster
6. add vnpy_ib support for Shanghai Stock Connect, Shenzhen Stock Connect, TSX, AMEX.
7. add vnpy_ib support for index ticker data
8. add strategy instance search function in vnpy_ctastrategy strategy trading management interface.

## Fixes

1. fix the problem of counting the amount of bar data in vnpy_mongodb (using the new count_documents function)
2. fix the issue that BaseMonitor derived component could not save interface state automatically due to PySide6 object destruction before __del__ call



## Version 3.1.0

## New
1. New trading interface vnpy_uf for Hang Seng Cloud UF2.0 securities simulation environment is added.
2. New trading interface vnpy_hx is added for FireElephant Investment Education simulation environment.

## Adjustments
1. upgraded the version of tzlocal library to 4.2, eliminating the warnings of get_localzone() function.
2. Improve the function and variable type hints in the code.
3. use QtCore.Signal instead of the old QtCore.pyqtSignal.
4. optimize the delegate transaction related details of vnpy_rohon interface.
5. update vnpy_xtp to version 2.2.32.2.0 of the XTP API to support the new bond system of SSE.
6. optimize the data writing speed of vnpy_mongodb, based on pymongo 4.0 version of the batch write function
7. add vnpy_ctp for delegate function return value is non-zero (failed to send request) state of the processing.
8. change the strategy template drop-down box of vnpy_ctastrategy and vnpy_ctabacktester to sort by first letter.

## Fixes
1. fix a data refresh issue in the Greek value monitoring component of the vnpy_optionmaster module
2. fix a data load range issue in vnpy_mongodb due to time zone information in timestamps being true
3. fix the issue of missing lib files in the sdist source code packaging of vnpy_tts.
4. fix a parsing issue with vnpy_rqdata due to NaN query returns.


# 3.0.0 version

## Adjustments
1. remove api, gateway, app submodule directories
2. remove default dependency of requirements.txt on plugins
3. simplify and refactor the rpc sub-module to target cross-process communication in reliable environments (local, LAN)
4. remove support for authentication in rpc submodule
5. adjust the implementation of the heartbeat mechanism in the rpc submodule. 6.
6. remove the code editor based on QScintilla, and use VSCode to open the code.
7. optimize the loading logic of QAction button icon in MainWindow.
8. Support customized interface name when adding transaction interface in MainEngine.

## Fixes
1. Fix the problem that the [Configuration] button is not displayed under Linux/Mac by using the non-native window menu bar.


## Version 2.9.0

## New
1. New Vertex HTS counter trading interface vnpy_hts is added.

## Adjustments
1. Remove Hang Seng Options hsoption interface
2. vnpy_webtrader add support for custom listening address and port.
3. vnpy_mongodb locks the pymongo dependency to version 3.12.3.
4. vnpy_udata install script adds hs_udata library dependency.
5. vnpy_uft upgrades to use version 3.7.2.4 of the HS API interface

## Strip
2. Strip Guotai Junan Securities Unified Access Gateway trading interface to vnpy_hft project
3. Strip the Vertex Filtronics trading interface to the vnpy_sec project
4. Strip RPC services and interfaces to vnpy_rpcservice project

## Fixes
1. fix the withdrawal failure problem caused by the conflict between the withdrawal number and the order number when vnpy_tora withdraws an order.
2. fix the problem of wrong mapping of [Undelivered] status in vnpy_tora stock order status
3. fix the data caching problem in the edit box of backtest start date in vnpy_ctabacktester.
4. fix the issue that when downloading data by segments in vnpy_udata, it may enter a dead loop
5. fix a bug in vnpy_udata that caused an error when the downloaded data amount was empty.
6. fix the problem that data cannot be read in vnpy_dolphindb when the contract name has a symbol.


# Version 2.8.0

## New
1. Added a new interface vnpy_ost for OST counter trading. 2.
2. Added strategy parameter optimization function in Portfolio Strategy module.

## Fixes
1. Fixed the error caused by the leftover installation scripts after the stripping of some C++ interface modules.
2. fix the flashback problem after vnpy_xtp subscribes to SZSE quotes.
3. fix the data error caused by vnpy_tushare when part of the data field is None.
4. fix vnpy_mini, the date field error of SFE quotes timestamp when changing day of nightly trading.
5. fix the problem of missing ETF option contract information parsing in vnpy_uft
6. fix the N/A parsing problem when vnpy_wind downloads missing data.
7. fix missing html static file in vnpy_webtrader
8. fix vnpy_dolphindb data type problem when storing Tick data.
9. fix a bug in vnpy_dolphindb when reading data is empty.
10. fix the problem that the contract multiplier of gold TD contract is 0 when vnpy_esunny query the contract.
11. fix vnpy_ctastrategy strategy initialization failed to read boolean value false
12. fix a problem with vnpy_rohon that assigns wrong values to option contract fields
13. fix issue with vnpy_leveldb's Linux installation dependency libraries

## Fixed a dependency library issue in vnpy_leveldb for Linux.
1. remove old version of RestClient client based on requests library
2. remove old version of WebsocketClient client based on websocket-client library
3. vnpy_tts add support for SSE and SZSE stock simulation trading.
4. vnpy_ctp remove support for option inquiry orders.
5. vnpy_ctp add the function of avoiding repeated operation after the authorization code verification fails.
6. optimize vnpy_uft's disconnect and reconnect quote subscription logic
7. add vnpy_arctic for user name and password authentication function
8. add vnpy_mini support for stock index options.

## Divest
1. divest the trading interface of Huaxin Singularity into vnpy_tora project and upgrade it to version 4.0.
2. divest the Pegasus trading interface to vnpy_femas project
3. divest the Goldstar Gold interface to vnpy_ksgold project
4. stripped the Portfolio Strategy module to the vnpy_portfoliostrategy project
5. stripped Excel RTD module to vnpy_excelrtd project
6. stripped the local simulation trading module to the vnpy_paperaccount project

# Version 2.7.0

## New
1. added tinysoft data service project vnpy_tinysoft
2. added Flush iFinD data service project vnpy_ifind
3. Added dYdx trading interface vnpy_dddx
4. vnpy_wind is a new data service project.
5. Added PortfolioBarGenerator for PortfolioStrategy.

## Adjustments
1. Remove KasiaGateway
4. Remove MarketRadarApp. 5.
5. Removed Arbitrage and Grid non-executable algorithms from Algorithmic Trading Module
6. vnpy_tushare data service, add position and turnover fields
8. vnpy_datamanager data manager, query bar information is displayed sorted by contract code
13. vnpy_dolphindb optimize data loading and parsing speed
14. vnpy_influxdb uses pandas to parse CSV data to improve the overall speed.

## Fixes
1. fix vnpy_ctp's CtpGateway's date field error in SFE quotes timestamps during nightly day change.
2. fix the error overwrite problem when vnpy_arctic's data is written repeatedly

## Stripping
1. stripped the InteractiveBrokers trading interface to vnpy_ib project
2. Stripped Flying Squirrel trading interface to vnpy_sgit project.
3. stripped Edson FX trading interface to vnpy_tap project
4. stripped the Direct Futures trading interface to the vnpy_da project
5. Stripped algorithmic trading module to vnpy_algotrading project
6. stripped the script trading module to the vnpy_scripttrader project
7. divest the trading portfolio management module into the vnpy_portfoliomanager project


# Version 2.6.0

## New
1. add send and withdraw functions for bilateral quote operations
2. add UI component for bilateral quote monitoring
3. add the abstract interface vnpy.trader.database for interfacing with the database.
4. add a new MongoDB database interface project based on Arctic vnpy_arctic
5. add LevelDB database interface project vnpy_leveldb
6. added DolphinDB database interface project vnpy_dolphindb
7. added abstract interface vnpy.trader.datafeed for interfacing with data services
8. add TuShare data service project vnpy_tushare
8. added Hang Seng UData data service project vnpy_udata
8. added Tian Qin TQSDK data service project vnpy_tqsdk
8. added CoinAPI data service project vnpy_coinapi

## Adjustments
1. Remove functions related to batch entrustment and batch withdrawal. 2.
2. remove TigerGateway, the trading interface of Tiger Securities
3. remove XgjGateway, the trading interface of XinManager
4. Remove the support of AlgoTrading algorithmic trading module for Jinnah Algorithmic Service.
5. RestClient adds support for operating system proxy configuration.
6. The default exception handling logic of RestClient and WebsocketClient is changed from throwing exception to printout.
7. Spread trading module removes support for reverse contracts, linear spreads and open/close fields.
8. Spread trading module optimizes the support for flexible spreads and optimizes the filtering judgment of spread quote push.
9. When the spread trading algorithm stops, it will wait until all commissions are finished and all legs are balanced before ending the algorithm.

## Fixes
1. fix the process startup error when running the multi-process optimization on Linux/Mac systems.
2. fix WebsocketClient's frequent disconnections due to the imperfect heartbeat mechanism.

## Strip
1) Strip the rice basket data interface to vnpy_rqdata project and upgrade it to version 2.9.38. 2) Strip the quote recording module to vnpy_rqdata project.
2. Strip the quote recording module to vnpy_datarecorder project.
3. stripped the bar charting module to vnpy_chartwizard project.
4. stripped SQLite database interface to vnpy_sqlite project
5. stripped MySQL database interface to vnpy_mysql project
6. stripped PostgreSQL database interface to vnpy_postgresql project
7. stripping the MongoDB database interface to the vnpy_mongodb project
8. stripped InfluxDB database interface to vnpy_influxdb project
13. stripped option volatility trading module to vnpy_optionmaster project


# Version 2.5.0
## New
1. added the interface vnpy_tts (6.5.1) for TTS trading system (CTP-compatible simulation trading environment)
2. Added vnpy_esunny (1.0.2.2) interface for eSun Qixing/North Star compatible trading APIs.
3. added turnover turnover field for BarData and TickData

## Adjustments
1. change the loading of bar spread data during strategy initialization in SpreadTrading module to give priority to querying data through RQData.
2. In the AboutDialog of MainWindow, get the version information based on importlib_metadata module.
3. hide the [?] button in the upper right corner of all dialog boxes. button
4. Change the contract information of Easun FX TapGateway from quotes interface to trading interface (to avoid the problem that the size of FX contract is 0).
5. Improve the pop-up dialog box of VeighNa Trader to avoid program crash in case of repeated error reports.

## Fixes
1. fix the auto-compile operation of the stripped XTP API when installing on Linux. 2. fix the PortfolioManager issue.
2. fix the bug that the UI component of PortfolioManager listens to the wrong type of transaction event. 3. fix the bug that the UI component of vnpy_vnpy_customize is not a valid UI component.
3. fix the bug that the Response object under vnpy_rest lacks a text field.
4. fix a bug in RestClient that caused an error in the underlying connection when the proxy port information was passed as empty.
6. fix the bug that the output results of ArrayManager's Aroon metrics are in the wrong order.
7. fix the bug caused by the lack of processing of localtime field when reading and writing TickData in Database Manager.

## Stripping
1. stripped the RH interface to vnpy_rohon project and upgraded it to version 6.5.1. 2. stripped the CTP MINI interface to vnpy_rohon project.
2. stripped CTP MINI interface to vnpy_mini project and upgraded to version 1.5.6
3. stripped CTP Option interface to vnpy_sopt project
4. Strip the Hang Seng UFT counter Extreme API interface to vnpy_uft project


## Version 2.4.0

## New
1. added TickData's local timestamp field local_time (without time zone information).
2. added a new concurrent asynchronous REST API client vnpy_rest project based on asyncio and aiohttp implementation.
3. add a new vnpy_websocket project, which is a concurrent asynchronous websocket API client based on asyncio and aiohttp implementation.
4. New Genetic Algorithm Optimization based on multi-process mode.
5. added support for local NIC address in the XTP API package for the ticker login function.

## Adjustments
2. Strip the exhaustion and genetic optimization algorithms from CTA strategy module to vnpy.trader.optimize module. 3.
3. After the genetic algorithm is optimized, output the results of all backtested parameters (not just the optimal results).
4. when CTA strategy engine loads a strategy file, add a module reloading operation, so that any changes to the strategy file can take effect immediately.
5. When CTA strategy engine scans strategy files in a specific directory, use the glob function (replacing the original os.walk) to avoid incorrect loading of files in subdirectories.
6. Strip the CTA strategy module to the vnpy_ctastrategy project.
7. stripped the CTA backtesting module into the vnpy_ctabacktester project.
8. stripped XTP interface to vnpy_xtp project and upgraded to version 2.2.27.4
9. divest the ex-ante risk control module into vnpy_riskmanager project
10. stripped data management module to vnpy_datamanager project

## Fixes
2. fix the error when deleting bar data in MySQL and PostgreSQL database managers
3. fix RestClient and WebsocketClient based on aiohttp that fails to restart after the event loop is stopped
7. fix the problem that CtaBacktester fails to start optimization when optimizing parameters based on tick level data
8. fix the problem that ToraStockGateway and ToraOptionGateway do not return the delegate number when calling the order function.
9. fix the problem that time field parsing error when importing data in InfluxDB Data Manager.

# 2.3.0 version

## Fixes
1. fix the problem that IbGateway does not automatically subscribe to previously subscribed contracts after disconnection and reconnection. 2. fix the problem that the net price of the CTA module does not return the commission number.
2. fix the problem that in the net position trading mode of CTA module, when partially closing and partially opening a position, the opening part of the order is wrong.
6. fix the problem of CtpGateway's error in handling FAK and FOK orders.
10. fix the problem of query failure due to wrong parameter passing when querying historical data in IbGateway. 11. fix the problem of query failure when querying historical data in IbGateway.
11. fix the problem of IbGateway getting stuck when the historical data of the contract to be queried does not exist.
12. Fix an issue in IbGateway where the contract multiplier (string) returned by a query is not converted to a higher level application.
14. fix the issue of BarGenerator, when synthesizing hourly bar, the closing price of minute bar was missed in some cases.
15. Fix a bug in UftGateway that prevented the subscription of quotes when connecting to the ETF options server.
16. Fix an issue with UftGateway that incorrectly handles milliseconds in the commission timestamp when connecting to the ETF Options Server.

## Adjustments
1. modify the net position trading mode of the CTA module to support the splitting of today's and yesterday's positions of SFE and NEMO. 2. adjust the return mode of the Portfolio Strategy module.
2. adjust the bar playback logic of the backtesting engine of the portfolio strategy module, so that when bar data is missing at a certain point in time, the bar dictionary pushed to the strategy will not make up for it.
3. encapsulate the CTP interface and API and divest it into the vnpy_ctp project.
4. Packaged the CTP passthrough test interface and API into the vnpy_ctptest project.

## New
1. Added DataManager's ability to select timestamp time zone when importing CSV files. 2.
2. Added CtaStrategy module's strategy move assistant function to realize one-click futures month-over-month move support.


# Version 2.2.0

## Fixes
1. Fixed the problem that DataManager queried the range of bar data in the database with opposite start and end dates. 2.
6. fix the problem that save_tick_data function in PostgreSQL database docking layer has saved error due to accessing interval.
7. Fix a bug in DataRecorder module where the contract for saving recording is misconfigured under add_bar_recording.
8. fix a problem in the PostgreSQL database docking layer where the transaction execution fails and subsequent errors are reported, by setting the autorollback mode (autorollback=True) when creating the database object.
9. fix the error of querying data range due to calling old version of function when DataManager updates data automatically.
10. fix the problem of floating point precision of historical data obtained by RQData download. 11. fix the bug of BarGenerator.
11. fix the problem of missing fields of closing price, volume and position when BarGenerator synthesizes N-hour bar.
12. fix the problem of repeating the display of time points on the axes of ChartWidget, the underlying component of bar charts, when fewer data are drawn.
13. fix the problem of missing time zone information in the Spread Market data generated by the SpreadTrading module.
14. fix the problem of missing the latest price and time stamp of the spot precious metal market data in IbGateway.
15. fix the problem of missing volume field when synthesizing hourly bar in BarGenerator
16. fix the problem that vnpy.rpc module cannot exit normally after enabling asymmetric encryption.

## Adjustments
1. modify the ChartItem under vnpy.chart to be drawn on demand, so as to shorten the time consuming when the chart is displayed for the first time. 2. modify the IbGateway to make it more efficient.
2. modify the historical data query function of IbGateway to include all available times (i.e., the evening electronic trading sessions in Europe and the United States).
3. Modify DataRecorder's data entry to batch writing at regular intervals to improve the writing performance when recording a large amount of contract data.

## New
1. Added the function of automatic reconnection after IbGateway disconnection (checking every 10 seconds). 2.
2. Added the underlying data structure and functional functions related to bilateral quote business.
3. Added the net position trading mode of OffsetConverter.
4. Added optional parameters for net position trading in the strategy template of CtaStrategy module.
5. Added an optional parameter for annual trading days in the backtesting engine of the CtaStrategy module.
6. Added support for displaying spread charts in ChartWizard module.
7. Added alerts for radar signal conditions in MarketRadar module.

# 2.1.9.1 version

## Fixes
1. Fix the compatibility problem caused by pyopenssl.extract_from_urllib3 in RestClient. 2.

## Tweaks
1. Adjust the algorithm for searching the par strike price of the option chain data structure in the OptionMaster module, instead of relying on the underlying contract.

## New
1. Added the feature of using synthetic futures as the underlying contract for pricing in the OptionMaster module.


## Version 2.1.9

## Fixes
1. Fixed the problem that the same hourly bar was pushed twice in BarGenerator's hourly line synthesis. 2.
2. fix the problem that the lru_cache cache causes the result of the new round of optimization to remain unchanged when the genetic algorithm is optimized.
3. fix the problem of WinError 10054 WSAECONNRESET caused by the use of OpenSSL in the lower layer of the requests library when RestClient initiates a request.
5. fix the problem that the exception catching dialog box executes repeatedly and causes a crash when the program catches exceptions frequently
7. fix the problem that ActiveOrderMonitor will save all delegate data together when saving CSV.
8. Fix a system crash issue when XtpGateway repeatedly initiates a login operation.
9. Fix the problem of mapping error of stock market order type in XtpGateway.

## Adjustments
1. rounding the price data of XTP interface based on the minimum price jump of the contract, and retaining 2 decimal places for the funds.
2. When BaseMonitor saves a CSV file, the table header is changed to the Chinese language displayed in the graphical interface (before it was the English language for the field names of the data).
3. When initializing the TWAP algorithm, the number of commissions in each round is rounded to the minimum number of contracts to be traded.
4. split the database client in the original vnpy.trader.database into a separate vnpy.database module.
5. Optimize the code refactoring of SQLite/MySQL/PostgreSQL/MongoDB/InfluxDB clients, and add the function of BarOverview query for the overall situation of bar data.

## New
1. added BaseMonitor data monitoring UI component (and its subclasses), with the function of automatically saving column widths
2. add support for FENS server connection and fund account login in Huaxin QIP ToraGateway, which previously only supported front-end machine connection and user code login 
4. add InfluxDB database client vnpy.database.influx for Tick data storage and loading support