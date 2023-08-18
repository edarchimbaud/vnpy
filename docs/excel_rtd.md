# ExcelRtd - EXCEL RTD Module

## Functional Description

ExcelRtd is a functional module for **accessing any data information** within the VeighNa program in Excel.
RTD full name is RealTimeData, is Microsoft provided mainly for the financial industry in real-time data needs designed for Excel data docking program. ExcelRtd relies on the PyXLLC module (www.pyxll.com), which is a commercial software that needs to be purchased to be able to use it (provides 30 days of free use).

## Install PyXLL
In order to use the ExcelRtd module, the PyXLL plug-in needs to be installed. The steps are as follows:

First go to the [PyXLL official website](https://www.pyxll.com/) and click DownloadPyXLL as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_0.png)

Then jump to the download interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/13.png)

At this time you need to fill in the appropriate fields, of which **Python Version** choose Python3.10, and **Excel Version** according to their own installed version of Excel to choose, generally 64bit (x64).

After filling in the form, click [Download PyXLL] and you will be redirected to the download page. After downloading the file, go to the folder where the file is placed, hold down the shift key and click the right mouse button, select [Open PowerShell window here] and run the following command:

```bash
pip install pyxll
pyxll install
```

Then follow the software requirements and it will be successfully installed.

Please note that when you get to the step shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_9.png)

If you don't specify a path, it will be installed to the default location in the picture (please remember this path as you will need to access this folder later).

Then go to the examples directory under that directory and put vnpy_rtd.py under the path ~/veighna_studio/Lib/site-packages/vnpy_excelrtd/ into that directory as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_5.png)

The installation is now complete.

## Load startup

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Transaction] button, and check [ExcelRtd] in the [Application Module] field of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_excelrtd import ExcelRtdApp

# Write after creating the main_engine object
main_engine.add_app(ExcelRtdApp)
```

## Start the module

Before starting the module, please connect the trading interface (see the Connecting the Interface section of the Basic Usage chapter for details on how to connect). Start the module after you see "Contract Information Query Successful" in the [Log] column of VeighNa Trader main interface, as shown in the figure below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not get all contract information automatically when you log in, but only when you subscribe to the market manually. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

After successfully connecting to the trading interface, click [Functions] -> [Excel RTD] in the menu bar, or click Charts in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_6.png)

You can enter the UI interface of Excel RTD module, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/15.png)


## Functionality and Configuration

### Basic Application

After starting the Excel RTD module, you can call the functions provided by the module in an Excel table through PyXll (mainly to get real-time data through the rtd_tick_data function).

First open an excel table, and in each cell call rtd_tick_data function and pass the corresponding parameters can get the corresponding data, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/14.png)

The above figure is an example of obtaining real-time data for four fields of soybean oil 2205 (bid_price_1, high_price, low_price and last_price respectively).

From the figure, we can see that the rtd_tick_data function takes two parameters: one is vt_symbol, and the other is the attribute of TickData defined in VeighNa (for specific attributes, please refer to the source code vnpy.trader.object.TickData). These two parameters are strings, the first parameter can be specified by the specific location of the cell, such as "A1" that the first row of column A data.

At the same time, in the graphical interface of the Excel RTD module can also be seen in the corresponding output, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/16.png)

### Advanced Applications
Of course, the above is just a simple demonstration of the functionality of the ExcelRtd module. As for the specific data to get, in what way to display on excel, it is written by the user according to their actual needs. Here we provide several advanced cases, including futures market quote tracking, market depth quote tracking and spread monitoring:

#### Futures market quote tracking
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_10.png)

#### Market Depth Tracking

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_11.png)
#### Spread Monitoring

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/excel_rtd/excel_rtd_12.png)