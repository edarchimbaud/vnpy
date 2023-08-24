# RpcService - RPC Server Module

## Function Introduction

RpcService is a functional module used to **transform VeighNa Trader process into an RPC server**, which externally provides functions such as trade routing, quotes data push, and position and fund inquiry.

For specific application scenarios of RPC, please refer to the [Application Scenarios of RPC] section at the end of this document.

## Load startup

### Loading VeighNa Station

After logging in to VeighNa Station, click the [Trading] button and check the [RpcService] box in the [Application Module] column of the configuration dialog box.

### Script Loading

Add the following code to the startup script:
'
```python 3
### Write it at the top
from vnpy_rpcservice import RpcServiceApp

# Write after creating the main_engine object
main_engine.add_app(RpcServiceApp)
```

### Start the module

Before starting the module, please connect to the login trading interface (see the Connecting to the Interface section of the Basic Usage chapter for details on how to connect). Start the module after you see "Contract Information Query Successful" in the [Log] column of VeighNa Trader main interface, as shown in the following figure:  

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/market_radar/1.png) 

After successfully connecting to the trading interface, click [Functions] -> [RPC Service] in the menu bar, or click the icon on the left side of the button bar:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/rpc_service/1.png) 

You can enter the UI interface of RPC service module, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/rpc_service/2.png) 

### Configuration and usage

### Configuring the RPC service
The RPC service is developed based on ZeroMQ, and the external communication addresses include:

* **Request Response Address**
    * Used to passively receive requests sent by the client and return results after performing the corresponding tasks;
    * Examples of functions:
        * quote subscription;
        * Delegate order placement;
        * Delegated withdrawal;
        * Initialization information query (contracts, positions, funds, etc.);
* **Event broadcast address**
    * Used to actively push event data received by the server to all connected clients;
    * Examples of functions:
        * Quote push;
        * Mandate push;
        * transaction push.

All of the above addresses use ZeroMQ's address format, which consists of two parts: ** communication protocol** (e.g. tcp://) and ** communication address** (e.g. 127.0.0.1:2014).

The communication protocols supported by the RPC service include:

* **TCP protocol**
    * Protocol prefix: tcp://
    * Available for both Windows and Linux systems
    * Can be used for local communication (127.0.0.1) or network communication (network IP address)
* **IPC protocol**
    * Protocol prefix: ipc://
    * Can only be used on Linux systems (POSIX local port communication)
    * Can only be used for local communication, suffixed with any string content

It is generally recommended to use TCP protocol directly (and the default address), for the use of Ubuntu system and want to pursue a lower communication delay users can use IPC protocol.

### Run RPC service

After completing the configuration of the communication address, click the [Start] button to start the RPC service, the log area will output "RPC service started successfully", as shown in the following figure:

The log area will output "RPC service started successfully", as shown in the following figure: ![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/rpc_service/3.png) 

After successful startup, you can use RpcGateway in another VeighNa Trader process (client) to connect.

If you want to stop the RPC service, you can click the [Stop] button, and the log output will be "RPC service stopped".


### Connecting to the client

VeighNa provides RpcGateway, which is used in conjunction with RpcService, as a standard interface for the client to connect to the server and conduct transactions, which is transparent to the upper layer applications.

From the client's perspective, RpcGateway is a CTP-like interface. Because the configuration of the external trading account connection has been completed uniformly on the server side, the client only needs to communicate with the server side, without the need to re-enter the account password and other information.

After loading the RpcGateway interface on the client side, enter the main interface of VeighNa Trader, click [System] -> [Connect RPC] in the menu bar, and then click [Connect] in the pop-up window to connect, as shown in the figure below.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/rpc_service/5.png)

The [Active Request Address] and [Push Subscription Address] correspond to the [Request Response Address] and [Event Broadcast Address] previously configured on the server side, so be careful not to write them backwards.


## RPC Introduction

Due to the existence of the global interpreter lock GIL, resulting in a single Python process can only utilize the computing power of a single CPU core. Remote Procedure Call Protocol (RPC) service can be used to **cross-process or cross-network service function calls**, effectively solving the above problem.

A specific process connects to the transaction interface to act as a **server** and actively pushes events to other independent **client** processes within the local physical machine or local area network and handles client-related requests, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/rpc_service/7.png)

## RpcService application scenarios

- For users running a large number of strategies, only one local market and trading channel can support multiple client processes to trade at the same time, and each client trading strategies run independently, without affecting each other;
- For small and medium-sized investment institution users, you can load various trading interfaces and RiskManagerApp on the server side to realize a lightweight treasury trading system, where multiple traders share a unified trading channel and realize risk management at the fund product level.
