# RiskManager - Ex-ante Risk Management Module

## Introduction

The RiskManager module is a functional module for **pre-existing risk management**, which allows users to easily accomplish tasks such as starting, modifying and stopping risk management through its UI.

## Load and start

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check [RiskManager] in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:

```python 3
### Write it at the top
from vnpy_riskmanager import RiskManagerApp

# Write after creating the main_engine object
main_engine.add_app(RiskManagerApp)
```

## Start the module

Click [Functions] -> [Trading Risk Control] in the menu bar, or click the icon in the left button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-1.png)

You can enter the UI interface of the Ex-ante Risk Control module, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-2.png)


## Starting Risk Control

Prior risk control module is responsible for checking whether the status of the order complies with various risk control rules before it is sent out through the trading API interface. Risk control rules include transaction flow control, number of orders placed, active commissions, total number of withdrawn orders, etc., as follows:

 - Delegation flow control related:
   - Delegation flow control limit: the maximum number of delegations allowed to be issued within a given time window.
   - Mandate flow control clearing: every how many seconds to clear the above count of mandates.
 - Mandate flow control limit: the maximum number of mandates allowed in a given time window Mandate flow control clearing: the number of mandates cleared every how many seconds.
 - Total transaction limit: the maximum number of transactions (not the number of commissions) allowed during the day.
 - Maximum number of active commissions: the maximum number of active commissions (active, unfilled, partially filled) allowed.
 - Contract Withdrawal Limit: the maximum number of withdrawals allowed for a single contract in a single day (each contract is counted independently).

It is recommended to activate pre-testing before running the automated trading every day to check whether every order issued meets the risk control requirements:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-3.png)

1. Select [Activate] from the drop-down box in the column of [Risk Control Operation Status];
2. After setting the parameters of various wind control rules, click the [Save] button below to start running the wind control. 3;
3. At this time, each commission in the system needs to meet all the requirements of wind control (not exceeding the limit) before it can be issued through the underlying interface.


## Parameter Modification

The Ex-ante Risk Control module allows users to customize risk control parameters:

* Users can click the up and down arrows on the right side of the input box to modify the parameters, or directly enter numbers to modify them, as shown below.
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-4.png)
* After modification, please click [Save] button to take effect.

## Stop Wind Control

When there is no need to run the wind control, user can stop the wind control:

* Select [Stop] in the drop-down box of [Wind Control Running Status] as shown below:
![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/risk_manager/1-5.png)
* Click the [Save] button at the bottom to stop the wind control check for the delegate.
