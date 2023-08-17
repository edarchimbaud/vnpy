# VeighNa in English - By Traders, For Traders.

<p align="center">
  <img src = "https://vnpy.oss-cn-shanghai.aliyuncs.com/veighna-logo.png"/>
</p

<p align="center">
    <img src ="https://img.shields.io/badge/version-3.7.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src = "https://img.shields.io/badge/python-3.7|3.8|3.9|3.10-blue.svg" />
    <img src ="https://img.shields.io/github/actions/workflow/status/vnpy/vnpy/pythonapp.yml?branch=master"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

:rocket: :rocket: **This is the first version of VeighNa in English!** :rocket: :rocket:

VeighNa is a Python-based open source quantitative trading system development framework, in the open source community's continuous contribution to grow step by step into a multi-functional quantitative trading platform, since its release has accumulated a large number of users from financial institutions or related fields, including private equity funds, securities firms, futures companies and so on.

If you have any questions in the process of using VeighNa for secondary development (strategies, modules, etc.), please check the [**VeighNa Project Documentation**](https://edarchimbaud.com/trading-platform-veighna), and if you can't solve it, please go to the [**Official Community Forum**](https://www.vnpy.com/forum/) for help, and you are welcome to share your experience in the [Experience Sharing] section!

For VeighNa's financial institution users, a special [VeighNa Institutional User Group] (QQ Group No.: 676499931) has been created to share issues related to institutional applications, such as: interbank market access, asset management O32 system, distributed deployment and other content. Please note that this group is only open to financial institution users, when adding the group, please specify: name - organization - department.

## Features

1. Multi-functional quantitative trading platform (trader), integrated with a variety of trading interfaces, and for the development of specific strategies algorithms and functions to provide a simple and easy to use API for the rapid construction of quantitative trading applications required by traders.

2. Covering the following trading brokers:

    * Domestic market

        * CTP ([ctp](https://www.github.com/vnpy/vnpy_ctp)): domestic futures, options

        * CTP Mini ([mini](https://www.github.com/vnpy/vnpy_mini)): domestic futures, options

        * CTP Securities ([sopt](https://www.github.com/vnpy/vnpy_sopt)): ETF options

        * Pegasus ([femas](https://www.github.com/vnpy/vnpy_femas)): domestic futures

        * Hang Seng UFT ([uft](https://www.github.com/vnpy/vnpy_uft)): domestic futures, ETF options

        * eSun ([esunny](https://www.github.com/vnpy/vnpy_esunny)): domestic futures, gold TD

        * Vertex Feitron ([sec](https://www.github.com/vnpy/vnpy_sec)): ETF options

        * Vertex HTS ([hts](https://www.github.com/vnpy/vnpy_hts)): ETF options

        * Zhongtai XTP ([xtp](https://www.github.com/vnpy/vnpy_xtp)): domestic securities (A shares), ETF options

        * Huaxin Chips ([tora](https://www.github.com/vnpy/vnpy_tora)): domestic securities (A shares), ETF options

        * Guotai Junan ([hft](https://www.github.com/vnpy/vnpy_hft)): domestic securities (A shares, two financing)

        * Dongshi OST ([ost](https://www.github.com/vnpy/vnpy_ost)): domestic securities (A shares)

        * Oriental Wealth EMT ([emt](https://www.github.com/vnpy/vnpy_emt)): domestic securities (A shares)

        * Flying Mouse ([sgit](https://www.github.com/vnpy/vnpy_sgit)): gold TD, domestic futures

        * Jinshida Gold ([ksgold](https://www.github.com/vnpy/vnpy_ksgold)): Gold TD

        * Ronghang ([rohon](https://www.github.com/vnpy/vnpy_rohon)): futures capital management

        * JEES ([jees](https://www.github.com/vnpy/vnpy_jees)): futures capital management

        * Zhonghui Yida ([comstar](https://www.github.com/vnpy/vnpy_comstar)): interbank market

        * Nuggets ([gm](https://www.github.com/vnpy/vnpy_gm)): domestic securities (simulation)

        * Hang Seng Cloud UF ([uf](https://www.github.com/vnpy/vnpy_uf)): domestic securities (simulation)

        * TTS ([tts](https://www.github.com/vnpy/vnpy_tts)): domestic futures (simulation)

        * Fire Elephant ([hx](https://www.github.com/vnpy/vnpy_hx)): domestic futures (simulation)

    * Overseas Markets

        * Interactive Brokers ([ib](https://www.github.com/vnpy/vnpy_ib)): overseas securities, futures, options, precious metals, etc.

        * Edson 9.0 Forex ([tap](https://www.github.com/vnpy/vnpy_tap)): Overseas Futures

        * Direct Futures ([da](https://www.github.com/vnpy/vnpy_da)): Overseas Futures

    * Special Applications

        * RQData Quotes ([rqdata](https://www.github.com/vnpy/vnpy_rqdata)): cross-market (stocks, indices, ETFs, futures) real-time quotes

        * RPC service ([rpc](https://www.github.com/vnpy/vnpy_rpcservice)): cross-process communication interface for distributed architectures

3. Trading applications (apps) covering the following types of quantitative strategies:

    * [cta_strategy](https://www.github.com/vnpy/vnpy_ctastrategy): CTA strategy engine module, while maintaining ease-of-use, allows users to control at a fine-grained level (to reduce slippage, realize high-frequency strategies) the reported withdrawal behavior of delegates during the operation of CTA-type strategies.

    * [cta_backtester](https://www.github.com/vnpy/vnpy_ctabacktester): CTA strategy backtesting module, without the need to use Jupyter Notebook, directly using the graphical interface for strategy backtesting analysis, parameter optimization and other related work.

    * [spread_trading](https://www.github.com/vnpy/vnpy_spreadtrading): spread trading module, support for customized spreads, real-time calculation of spread quotes and positions, support for spread algorithmic trading and automated spread strategy two models

    * [option_master](https://www.github.com/vnpy/vnpy_optionmaster): options trading module, designed for the domestic options market, supports a variety of options pricing models, implied volatility surface calculation, Greek value risk tracking and other functions.

    * [portfolio_strategy](https://www.github.com/vnpy/vnpy_portfoliostrategy): portfolio strategy module, for simultaneous trading of multi-contract quantitative strategies (Alpha, option arbitrage, etc.), to provide historical data backtesting and real-time auto-trading features

    * [algo_trading](https://www.github.com/vnpy/vnpy_algotrading): algorithmic trading module, provides a variety of commonly used smart trading algorithms: TWAP, Sniper, Iceberg, BestLimit, etc.

    * [script_trader](https://www.github.com/vnpy/vnpy_scripttrader): script strategy module, quantitative strategies for the class of multi-subjective and computational task design, but also in the command line to achieve the REPL instruction form of trading, does not support the backtesting feature

    * [paper_account](https://www.github.com/vnpy/vnpy_paperaccount): local simulation module, purely localized implementation of the simulation of simulation trading functions, based on the real-time quotes obtained from the trading interface for commission aggregation, to provide commission transaction push and position records

    * [chart_wizard](https://www.github.com/vnpy/vnpy_chartwizard): K-line chart module, based on RQData data services (futures) or trading interface to obtain historical data, and combined with the Tick push to display real-time market changes.

    * [portfolio_manager](https://www.github.com/vnpy/vnpy_portfoliomanager): portfolio management module, based on independent strategy trading portfolio (sub-accounts), to provide commission transaction record management, automatic tracking of trading positions, and daily profit and loss real-time statistics Functions

    * [rpc_service](https://www.github.com/vnpy/vnpy_rpcservice): RPC service module, allowing a process to be started as a server, as a unified quote and transaction routing channel, allowing multiple clients to connect simultaneously, to achieve multi-process distributed system

    * [data_manager](https://www.github.com/vnpy/vnpy_datamanager): historical data management module, through the tree directory to view the database of existing data overview, select any time period data to view the details of the field, support for CSV file data import and export

    * [data_recorder](https://www.github.com/vnpy/vnpy_datarecorder): quote recording module, based on the graphical interface for configuration, according to the needs of real-time recording Tick or K-line quotes to the database, for strategy backtesting or initialization of the real market

    * [excel_rtd](https://www.github.com/vnpy/vnpy_excelrtd): Excel RTD (Real Time Data) real-time data service, based on the pyxll module to realize in Excel to get all kinds of data (quotes, contracts, positions, etc.) in real-time push updates.

    * [risk_manager](https://www.github.com/vnpy/vnpy_riskmanager): risk management module, providing statistics and restrictions on rules including transaction flow control, number of orders, active commissions, total number of withdrawals, etc., effectively realizing the front-end risk control function.

    * [web_trader](https://www.github.com/vnpy/vnpy_webtrader): Web service module, designed for B-S architecture requirements, the realization of the Web server to provide active function call (REST) and passive data push (Websocket)

4. Python trading API interface encapsulation (api), to provide the above transaction interface for the underlying docking implementation.

    * REST Client ([rest](https://www.github.com/vnpy/vnpy_rest)): High-performance REST API client based on concurrent asynchronous IO , using the event-message loop programming model , support for high-concurrency real-time transaction request sending

    * Websocket Client ([websocket](https://www.github.com/vnpy/vnpy_websocket)): high-performance Websocket API client based on concurrent asynchronous IO , support and REST Client to share the event loop to run concurrently

5. simple and easy to use event-driven engine (event), as the core of the event-driven transaction program.

6. Adapter interface to various types of databases (database):

    * SQL class

        * SQLite ([sqlite](https://www.github.com/vnpy/vnpy_sqlite)): lightweight single-file database, without the need to install and configure the data service program, VeighNa's default option for entry-level novice users.

        * MySQL ([mysql](https://www.github.com/vnpy/vnpy_mysql)): mainstream open-source relational database, extremely well documented and replaceable with other NewSQL-compatible implementations (e.g. TiDB)

        * PostgreSQL ([postgresql](https://www.github.com/vnpy/vnpy_postgresql)): more feature-rich open source relational database, support for new features through extension plug-ins, only recommended for skilled users

    * NoSQL class

        * DolphinDB ([dolphindb](https://www.github.com/vnpy/vnpy_dolphindb)): a high-performance distributed time-series database for low-latency or real-time tasks with high speed requirements

        * Arctic ([arctic](https://www.github.com/vnpy/vnpy_arctic)): a high-performance financial timing database, using chunked storage, LZ4 compression and other performance optimization schemes to achieve efficient reading and writing of timing data

        * TDengine ([taos](https://www.github.com/vnpy/vnpy_taos)): distributed, high-performance, SQL-enabled timescale database with built-in caching, streaming computation, data subscription, and other system functions, which can significantly reduce the complexity of research and development and operation and maintenance

        * TimescaleDB ([timescaledb](https://www.github.com/vnpy/vnpy_timescaledb)): a PostgreSQL-based timescale database, installed as a plug-in extension, supporting automatic partitioning of data by space and time.

        * MongoDB ([mongodb](https://www.github.com/vnpy/vnpy_mongodb)): a document-based database based on distributed file storage (bson format), with built-in hot data in-memory caching to provide faster read and write speeds

        * InfluxDB ([influxdb](https://www.github.com/vnpy/vnpy_influxdb)): time series database specially designed for TimeSeries Data, columnar data storage to provide high read/write efficiency and peripheral analysis applications.

        * LevelDB ([levelldb](https://www.github.com/vnpy/vnpy_leveldb)): a high-performance Key/Value database launched by Google, based on the LSM algorithm to realize the in-process storage engine, supporting billions of levels of massive data.

7. Adapter interface to the following types of data services (datafeed):

    * MiBasket RQData ([rqdata](https://www.github.com/vnpy/vnpy_rqdata)): stocks, futures, options, funds, bonds, gold TDs

    * Hang Seng UData ([udata](https://www.github.com/vnpy/vnpy_udata)): stocks, futures, options

    * TuShare ([tushare](https://www.github.com/vnpy/vnpy_tushare)): stocks, futures, options, funds

    * Vantage Wind ([wind](https://www.github.com/vnpy/vnpy_wind)): stocks, futures, funds, bonds

    * Tinysoft Tinysoft ([tinysoft](https://www.github.com/vnpy/vnpy_tinysoft)): stocks, futures, funds, bonds

    * Flush iFinD ([ifind](https://www.github.com/vnpy/vnpy_ifind)): stocks, futures, funds, bonds

    * Tian Qin TQSDK ([tqsdk](https://www.github.com/vnpy/vnpy_tqsdk)): futures

8. standard component for cross-process communication (rpc) for implementing complex trading systems with distributed deployment.

9. Python high-performance K-line chart (chart), support for large data volume chart display and real-time data update function.

10. [Community Forum](http://www.vnpy.com/forum) and [Zhihu Column](http://zhuanlan.zhihu.com/vn-py), including VeighNa project development tutorials and Python in the field of quantitative trading application research and other content.

11. The official communication group 262656087 (QQ), with strict management (regularly removing members who have been diving for a long time), and the joining fee will be donated to VeighNa community fund.

Note: The above description of the features is based on the description of the document released at the time of listing, there may be subsequent updates or adjustments. If there is any discrepancy between the description of the features and the actual situation, please feel free to contact us via Issue for adjustment.

## Environment Preparation

* We recommend using the Python distribution [VeighNa Studio-3.7.0](https://download.vnpy.com/veighna_studio-3.7.0.exe), which is specially built by VeighNa team for quantitative trading, integrating the built-in VeighNa framework and VeighNa Station quantitative management platform. Station quantization management platform, no need to install manually
* Supported system versions: Windows 10+ / Windows Server 2016+ / Ubuntu 20.04 LTS+.
* Supported Python versions: Python 3.7/ 3.8 / 3.9 / 3.10 64-bit (**Python 3.10 is recommended**)

## Installation steps

Download the Release distribution from [here](https://github.com/vnpy/vnpy/releases), unzip it and run the following command to install it:

**Windows**

```
install.bat
```

**Ubuntu**

```
bash install.sh
```

**MacOS**

```
bash install_osx.sh
```

**Note: setup.cfg lists the dependencies required for VeighNa framework installation, and requirements.txt gives the recommended installation versions of these dependencies. **

## Guidelines for use

1. Register for a CTP simulation account at [SimNow](http://www.simnow.com.cn/) and get the broker code and the address of the trading quotes server at [this page](http://www.simnow.com.cn/product.action).

2. Register at [VeighNa Community Forum](https://www.vnpy.com/forum/) to get VeighNa Station account password (forum account password that is)

3. Launch VeighNa Station (after installing VeighNa Studio, a shortcut will be automatically created on your desktop), enter the account password from the previous step to log in.

4. Click the **VeighNa Trader** button at the bottom to start your trading!

Caution:

* Do not close VeighNa Station while VeighNa Trader is running (it will exit automatically).

## Script Running

In addition to the graphical startup method based on VeighNa Station, you can also create run.py in any directory and write the following sample code:

```python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp


def main().
    """Start VeighNa Trader"""""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__".
    main()
```

Start VeighNa Trader by running the following command after opening CMD (hold Shift -> right mouse click -> open command window/PowerShell here) in that directory:

    python run.py

## Contribute code

VeighNa uses Github to host its source code, if you wish to contribute code please use the github PR (Pull Request) process.

1. [Create Issue](https://github.com/vnpy/vnpy/issues/new) - For larger changes (e.g. new features, major refactoring, etc.) it is recommended to open an issue to discuss them first, and for smaller improvements (e.g. documentation improvements, bugfixes, etc.) just send a PR.

2. Fork [VeighNa](https://github.com/vnpy/vnpy) - Click the **Fork** button in the upper right corner.

3. Clone your own fork: ```git clone https://github.com/$userid/vnpy.git``''
	* If your fork is outdated, you need to sync it manually: [sync method](https://help.github.com/articles/syncing-a-fork/)

4. Create your own feature branch from **dev**: ```git checkout -b $my_feature_branch dev``` * If your fork is out of date, you need to sync it manually: [sync method]()

5. Make changes to $my_feature_branch and push them to your fork.

6. Create a [Pull Request] - [here](https://github.com/vnpy/vnpy/compare?expand=1) from your fork's $my_feature_branch branch to the main project's **dev** branch by clicking **compare across forks**, select the required fork and branch to create PR. 7.

7. Wait for review, need to continue to improve, or be Merge!

When submitting code, please observe the following rules to improve code quality:

  * Check your code with [flake8](https://pypi.org/project/flake8/) to make sure there are no errors and warnings. just run ```flake8`` in the project root directory.

## Other content

* [Getting Help](https://github.com/vnpy/vnpy/blob/dev/.github/SUPPORT.md)
* [Community Code of Conduct](https://github.com/vnpy/vnpy/blob/dev/.github/CODE_OF_CONDUCT.md)
* [Issue template](https://github.com/vnpy/vnpy/blob/dev/.github/ISSUE_TEMPLATE.md)
* [PR Template](https://github.com/vnpy/vnpy/blob/dev/.github/PULL_REQUEST_TEMPLATE.md)

## Copyright

MIT
