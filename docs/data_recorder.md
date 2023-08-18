# DataRecorder - Live Tick Recorder Module

DataRecorder is a module for **Live Quotes Recording**, which allows users to record real-time tick data and K-line data, and automatically write and save them to the database.

The recorded data can be viewed through the DataManager module, and can also be used for historical backtesting of CtaBacktester, as well as live initialization of CtaStrategy, PortfolioStrategy and other strategies.

## Load startup

### VeighNa Station Loading

After launching and logging in to VeighNa Station, click the [Trading] button and check [DataRecorder] in the [Application Module] field in the configuration dialog.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_datarecorder import DataRecorderApp

# Write after creating the main_engine object
main_engine.add_app(DataRecorderApp)
```

## Start the module

Before starting the module, please connect to the trading interface (see the section on connecting to the interface in the chapter on basic usage for more details), and start the module after you see the output of "Contract information query succeeded" in the main interface of VeighNa Trader (log bar), as shown in the figure below:

The following is a diagram of the module [](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/cta_strategy/1.png)

Please note that the IB interface does not get all the contract information automatically when you log in, but only when you subscribe to the market manually. Therefore, you need to subscribe to the contract quotes manually on the main interface before launching the module.

After successfully connecting to the trading interface, click [Functions] -> [Quotes] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/1.png)

DataRecorder will be launched and the UI of DataRecorder will pop up, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/4.png)


## Add Records

The DataRecorder module supports the task of adding records of K-line (1-minute) and Tick data on demand:

1. Enter the local code (vt_symbol) of the contract to be recorded in the [Local Code] edit box as shown below:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/5.png)
- Note that the local code consists of two parts: the code prefix and the exchange suffix, e.g. rb2112.SHFE;
- The edit box provides auto-completion function (case sensitive) for contract information received after the interface is connected;

2. In the [Write Interval] edit box, select the timed batch write frequency as shown below:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/6.png)
In this way, you can first take out all the data to be recorded from the queue each time, and then write the existing data in the queue to the database at one time, so as to reduce the database pressure and recording delay;

3. Click the [Add] button corresponding to [K-Line Record] or [Tick Record] on the right side to add a recording task:

- After successfully adding, the local code of the contract will appear in the [K-line Record List] or [Tick Record List] below, and the corresponding log will be output at the bottom of the interface, as shown in the following figure:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/10.png)


## Remove Records

When you no longer need to record the quotes of a certain contract, you can remove its corresponding recording task:

1. Enter the local code (vt_symbol) of the contract you want to remove in the [Local Code] edit box. 2;
2. Click the [Remove] button on the right side of the [K-Line Record] or [Tick Record] to remove the corresponding recording task.

If the removal is successful, the corresponding recording task information under [K-Line Record List] or [Tick Record List] will be removed, and the corresponding log will be output at the bottom of the interface, as shown in the following figure:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/data_recorder/9.png)
