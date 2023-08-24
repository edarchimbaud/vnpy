# DataManager - Historical Data Management Module

## Introduction

DataManager is a functional module for **historical data management**, which allows users to conveniently accomplish tasks such as data download, data viewing, data import and data export through its UI interface.

## Loading and Starting

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Transaction] button and check [DataManager] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_datamanager import DataManagerApp

# Write after creating the main_engine object
main_engine.add_app(DataManagerApp)
``


## Start the module

After starting VeighNa Trader, click [Functions] -> [DataManager] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/00.png)

You can enter the historical data management UI interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/1.png)


## Download Data

DataManager module provides the function of downloading historical data with one click, click the [Download Data] button in the upper right corner, the window of downloading historical data will pop up, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/2.png)

You need to fill in the four fields of code, exchange, period and start date information:

<span id="jump">

- Code
  - Code format for contract type
  - Such as IF888, rb2105
- Exchange
  - Exchange on which the contract is traded (click the arrow button on the right side of the window to select the list of exchanges supported by VeighNa)
- PERIOD
  - MINUTE (1 minute bar)
  - HOUR (1 hour bar)
  - DAILY
  - WEEKLY
  - TICK（一个Tick）
- Start date
  - Format yyyy/mm/dd
  - e.g. 2018/2/25

</span>

Fill in the completion, click the following [Download] button to start the download process, download successfully as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/3.png)

Note that the historical data will be saved in the local database after the download is completed, and can be used directly in subsequent backtests or real trading, without having to repeat the download each time.

### Data source: data services (futures, stocks, options)

Take RQData as an example, [RQData](https://www.ricequant.com/welcome/purchase?utm_source=vnpy) provides historical data of domestic futures, stocks and options. Before using it, you need to ensure that the data service has been configured correctly (see the Global Configuration section of the Basic Usage chapter for details on how to configure it).

### Data source: IB (foreign futures, stocks, spot, etc.)

Interactive Brokers (IB) provides a wealth of foreign market historical data download (including stocks, futures, options, spot, etc.), note that you need to start the IB TWS trading software, and in the VeighNa Trader main interface to connect to the IB interface, and subscribe to the required contract quotes.


## Importing Data

If you have already obtained the data file in CSV format from other sources, you can quickly import it into the VeighNa database by using the Data Import function of DataManager. Click the [Import Data] button in the upper right corner, a dialog box will pop up from the one shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/21.png)

Click the [Select File] button at the top, a pop-up window will appear to select the path of the CSV file to be imported, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/5.png)

Then configure the relevant details of data import:

- Contract Information
  - The format is described in the [Download Data](#jump) section of this chapter;
  - Please note that the imported contract code (symbol) and exchange (exchange) fields are combined to form the local code (vt_symbol) used in modules such as CTA backtesting;
  - If the contract code is **IF2003** and the exchange is **CFFEX** (CFFEX), the local code to be used for backtesting in CtaBacktester should be **IF2003.CFFEX**;
  - The timestamp time zone can be selected;
- Table header information
  - You can view the header information of the CSV file and enter the corresponding header string in the header information;
  - For fields that do not exist in the CSV file (e.g., there is no [Position] field for stock data), please just leave them blank;
- Formatting Information
  - The time format definition of Python built-in library datetime module is used to parse the timestamp string;
  - The default time format is "%Y-%m-%d %H:%M:%S", which corresponds to "2017-1-3 0:00:00";
  - If the timestamp is "2017-1-3 0:00", then the time format should be "%Y-%m-%d %H:%M".

When you have finished filling in the form, it is shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/22.png)

Click the [OK] button to start importing data from the CSV file to the database. The interface will be half stuck during the import process, the larger the CSV file (the more data), the longer the stuck time will be. After successful loading, a pop-up window will appear to show that the loading was successful, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/20.png)


## Viewing Data

Currently there are three ways to get data in VeighNa Trader:

- Downloading data through the data service or trading interface

- Import from CSV file

- Recording with the DataRecorder module

Regardless of the method used to obtain data, click the [Refresh] button in the upper left corner to see the statistics of the data currently in the database (except Tick data). During the refresh process, the interface may have occasional lag, usually for the more data, the longer the lag time will be. After the refresh is successful, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/7.png)

Click the [View] button, a dialog box will pop up to select the data interval to view, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/10.png)

After selecting the data range to be displayed, click the [OK] button to see the specific data fields at each point in time in the table on the right:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/11.png)

Provided that the database already has data, click on the small arrow in front of the data frequency under the [Data] column on the leftmost side of the table to expand or collapse the display of contract information under that data frequency.

If the display on the right side of the table is incomplete, you can adjust it by dragging the horizontal scroll bar at the bottom of the interface.


## Export Data

If you want to export the data in the database to a local CSV file, you can select the contract you want to export and click the [Export] button on the right side of the row where the contract is located to bring up the Select Data Interval dialog box, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/8.png)

Select the range of the data interval to be exported and click [OK], a dialog box will pop up again to select the location of the output file, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/9.png)

Select the directory where you want to place the exported file, and after filling in the CSV file name, click the [Save] button to finish exporting the CSV file.


## Delete Data

If you want to delete specific contract data, you can select the contract to be deleted and click the [Delete] button on the right side of the contract row data, a dialog box will pop up, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/12.png)

Click the [OK] button to delete the contract data, and the Delete Success window will pop up, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/13.png)

At this time, click the [Refresh] button again, there is no more information about the contract on the graphical interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/14.png)


## Update Data

If the user **configured data service** or **trading interface (connected) provides sufficient historical data**, click on the upper right corner of the [Update Data] button, you can perform a one-click automatic download and update based on all the contract data displayed on the graphical interface.

The graphical interface before updating is shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/17.png)

Clicking the [Update Data] button brings up an information alert dialog box on the progress of the update, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/19.png)

At this time, DataManager will automatically** download the data up to the current latest date** from the end date of the existing data in the database and update it to the database.

If the data to be updated is small, the update task may be completed instantly, and it is normal not to observe the update dialog box at this time.

After the update is complete, click the [Refresh] button in the upper left corner to see that the contract data has been updated to the current latest date.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_manager/18.png)

## Data Range

Please note that although the interface shows the start and end time of the data already in the database, ** it does not mean that all the data between the start time and the end time is stored in the database**.

If you rely on the historical data provided by the trading interface, as soon as the time span between the start time and the end time exceeds the range of data that the interface can provide, it may lead to a situation where there are missing data between them. Therefore, it is recommended that after updating the data, click the [View] button to check whether the data for the contract is continuous.