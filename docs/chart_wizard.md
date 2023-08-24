# ChartWizard - Real-time Bar Charting Module

## Introduction

ChartWizard is a functional module for **real-time bar chart display**, users can view real-time and historical bar quotes through its UI, currently only supports displaying 1-minute level bar data, real-time bar (the latest bar) for Tick level refresh.

## Loading Startup

### Loading VeighNa Station

After launching and logging in to VeighNa Station, click the [Trading] button and check [ChartWizard] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
# Write at the top
from vnpy_chartwizard import ChartWizardApp

# Write after creating the main_engine object
main_engine.add_app(ChartWizardApp)
```


## Start the module

Before starting the module, please connect to the trading interface (see the Connecting to the Interface section of the Basic Usage chapter for details on how to connect). Start the module after you see the "Contract Information Query Successful" output in the [Log] column of the VeighNa Trader main interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not get all contract information automatically when you log in, but only when you subscribe to the market manually. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

Since VeighNa itself does not provide any data service, for the historical data used in the process of bar charting, the domestic futures historical data is provided by the data service, users need to prepare and configure the data service account (for details of the configuration method, please refer to the Global Configuration section of the Basic Usage chapter).

After successfully connecting to the trading interface, click [Function] -> [Bar Chart] in the menu bar, or click the icon on the left side button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/chart_wizard/1.png)

You can enter the UI interface of the real-time bar chart module, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/chart_wizard/2.png)


## New Chart

After opening the chart window, enter the contract code in the [Local Code] edit box (note that the local code consists of two parts: the code prefix and the exchange suffix, such as rb2112.SHFE).

Click the [New Chart] button to create a bar chart of the corresponding contract, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/chart_wizard/3.png)

Users can create new bar charts for multiple contracts, with a toggle window for quick switching: 

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/chart_wizard/4.png)


## View Charts

The chart for each contract is divided into two sub-charts areas, upper and lower:

- The upper sub-chart is the ticker bar;
- The lower sub-chart shows volume data.

The crosshair on the chart can be used to locate and display specific data for a particular point in time, with labels corresponding to the data points on both the X and Y axes, and information such as the OHLCV of the bar is also displayed in the upper left corner.

Other quick operations:

- You can pan the time range of the bar chart display left and right by dragging and dropping with the left mouse button;
- You can zoom in and out the time range of the bar chart by scrolling with the mouse wheel.
