# Data services


For data services, VeighNa provides a standardized interface BaseDatafeed (located in vnpy.trader.datafeed) that enables more flexible data service support. In the global configuration, fields related to data services are prefixed with datafeed.

The specific field meanings are as follows:
- datafeed.name: The name of the data service interface, which must be a full lowercase English letter;
- datafeed.username: the username of the data service;
- datafeed.password: password of the data service.

The above fields are required for all data services, if the authorization is by token please fill in the datafeed.password field. Currently VeighNa Trader supports the following seven data services, **specific details of each data service can be found in the corresponding project address**.

## RQData

Rice Basket RQData has been VeighNa official team of long-term recommended data services, for most individual investors should be cost-effective choice:
- Project address: [vnpy_rqdata](https://github.com/vnpy/vnpy_rqdata)
- Data classification: stocks, futures, options, funds and gold TD
- Data Period: Daily, Hourly, Minute, TICK (real-time update)
- Registration application: [RICEQUANT](https://www.ricequant.com/welcome/purchase?utm_source=vnpy)

**Please note that the username and password in the configuration information are not the account number and password used to log in to the official MiBasket website. **


## UData

HengYouData UData is a cloud-based data service launched by HengYouData, providing unlimited and unlimited access to a wide range of financial data:
- Project address: [vnpy_udata](https://github.com/vnpy/vnpy_udata)
- Data Classification: Stocks, Futures
- Data Cycle: Minute Line (after-hours update)
- Registration application: [constant_number_udata](https://udata.hs.net/home)


## TuShare

TuShare is a well-known domestic open source Python financial data interface project, developed and maintained by the god Jimmy team for a long time, in addition to market data also provides many alternative data:
- Project address: [vnpy_tushare](https://www.github.com/vnpy/vnpy_tushare)
- Data classification: stocks, futures
- Data Period: Daily, Minute (after-hours update)
- Registration application: [Tushare Big Data Community](https://tushare.pro/)


## TQSDK
Tian Qin TQSDK is a Python programmed trading solution launched by Shinex Technologies, providing access to historical data since the listing of current tradable contracts:
- Project address: [vnpy_tqsdk](https://github.com/vnpy/vnpy_tqsdk)
- Data Category: Futures
- Data Period: Minute Line (real-time update)
- Registration application: [Tian Qin Quantitative - Xin Yi Technology (shinnytech.com)](https://www.shinnytech.com/tianqin)


## Wind
Vantage Wind has been a standard configuration in the work for practitioners working in domestic financial institutions. Whether it is stock, bond or commodity market data, Wind can be said to have everything:
- Project address: [vnpy_wind](https://github.com/vnpy/vnpy_wind)
- Data Category: Futures
- Data Period: Minute Line (real-time update)
- Registration application: [Wind Financial Terminal](https://www.wind.com.cn/newsite/wft.html)

## iFinD
Flush iFinD is a financial data terminal for professional institutional users launched by Flush Corporation, and its market share has increased rapidly in the past few years:
- Project address: [vnpy_ifind](https://github.com/vnpy/vnpy_ifind)
- Data Category: Futures
- Data Period: Minute-by-minute (real-time update)
- Registration Application: [iFinD Financial Data Terminal](http://www.51ifind.com/)

## Tinysoft
As a domestic veteran financial data company Tinysoft, its core product [TinySoft .NET Financial Analysis Platform] (TinySoft for short) has accumulated a large number of users in the field of brokerage firms' research institutes and self-employment. When you look at the financial engineering research reports of the brokerage firms, you will often find that there is a data source statement "The above data is from TinySoft" written in the notes of the charts:
- Project address: [vnpy_tinysoft](https://github.com/vnpy/vnpy_tinysoft)
- Data Category: Futures
- Data Period: Minute Line (real-time update)
- Registration Application: [Tinysoft .NET Financial Analysis Platform](http://www.tinysoft.com.cn/TSDN/HomePage.tsl)

Please note that VeighNa Studio 3.0.0 does not provide Tinysoft support because Tinysoft does not currently support Python 3.10.

## Scripting
Before using the script, please configure the data service according to the above, and call the corresponding function interface when using it (please refer to the supported data cycles above for the specific interface support).

### Script loading

#### loads the required packages and data structures in the script.

```python 3
from datetime import datetime
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.object import HistoryRequest

# Get the data service instance
datafeed = get_datafeed()
```

#### Get historical data at the k-line level

```python 3
req = HistoryRequest(
    # contract code (example cu888 is a continuous contract code for rice baskets, only for demonstration purposes, please check the data service provider for specific contract code according to your needs)
    symbol="cu888",
    symbol="cu888", # contract exchange
    exchange=Exchange.
    SHFE, # Historical data start time
    start=datetime(2019, 1, 1), # Historical data start time.
    # Historical data end time
    end=datetime(2021, 1, 20), # Historical data end time.
    # Data time granularity, the default options are minute, hour and day, the specific choice needs to be combined with the authority of the data service and the needs of their own choice
    interval=Interval.
)

# Get k-line historical data
data = datafeed.query_bar_history(req)
```

#### Get tick level history data

Due to the large amount of tick data, please refer to the above to check if the data service provides tick data download service before downloading.

```python 3
req = HistoryRequest(
    # contract code (example cu888 is the continuous contract code of the meter basket, only for demonstration purposes, please check with the data service provider for the specific contract code according to your needs)
    symbol="cu888",
    symbol="cu888", # exchange=Exchange.
    exchange=Exchange.
    SHFE, # Historical data start time
    start=datetime(2019, 1, 1), # Historical data start time.
    # Historical data end time
    end=datetime(2021, 1, 20), # Historical data end time.
    # Data time granularity at tick level
    interval=Interval.TICK
)

# Get tick history data
data = datafeed.query_tick_history(req)
```
