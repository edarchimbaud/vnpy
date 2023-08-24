# Databases

VeighNa Trader currently supports the following eight databases:

## Introduction to SQL-like databases

### SQLite (default)

SQLite is a lightweight embedded database without the need to install and configure a data service program, and is VeighNa's **default database**. It is suitable for introductory novice users and has the following features:
 - Stored on a single cross-platform disk file;
 - Does not need to be configured, installed and managed on the system;
 - Does not require a separate server process.

#### SQLite Configuration Fields

SQLite is configured in VeighNa Trader with the following field information:

| Field Name | Value | Required or Not Required |
|--------- |---- | --- |
|database.name | sqlite | optional (not required defaults to sqlite)
|database.database | database file (relative to the trader directory) | Required |

A sample SQLite configuration is shown below:

|field name |value |
|--------- |---- |
|database.name | sqlite |
|database.database | database.db |

### MySQL

MySQL is currently the dominant open source relational database with the following features:
 - Rich documentation material, active community and users;
 - Supports multiple operating systems and multiple development languages;
 - Replaceable with other high-performance NewSQL database compatible implementations (e.g. TiDB).

#### MySQL Configuration Fields

MySQL requires the following field information when configuring in VeighNa Trader:

| Field Name | Value | Required or not |
|--------- |---- | ---- |
|database.name | "mysql" | Required |
|database.host | Address | Required |database.port | "mysql" | Required |database.host | Address | Required
|database.port | Port | Required |database.port | Port | Required |database.
|database.database |Database Name | Required |database.user |Database Name | Required |database.user |Database Name | Required
|database.user |User name | Optional |database.password |Optional
|database.password | Password | Optional

A sample MySQL configuration is shown below:

|field.name |value |
|--------- |---- |
|database.name | mysql |
|database.host |localhost |
|database.port | 3306 |
|database.database | vnpy | |database.user | vnpy | |database.user | vnpy
|database.user |root |database.
|database.password | |database.port | 3306

### PostgreSQL

PostgreSQL is a feature-rich open source relational database that is only recommended for beginners. Compared to MySQL, it is characterized by the following features:
 - Uses a multi-process structure;
 - Support for adding new features through extension plug-ins.

#### PostgreSQL Configuration Fields

When PostgreSQL is configured in VeighNa Trader, you need to fill in the following field information:

| Field Name | Value | Required or Not Required |
|--------- |---- | ---- |
|database.name | "postgresql" | Required |
|database.host | address | Required |database.port | "postgresql" | required |
|database.port | Port | Required |database.
|database.database |Database Name | Required |database.user |Database Name | Required |database.user |Database Name | Required
|database.user |User name | Required |database.password |Database.password |User name | Required
|database.user |User name | Required |database.password |Password | Required

A sample PostgreSQL configuration is shown below:

|field.name |value |
|--------- |---- |
|database.name | postgresql |
|database.host | localhost |
|database.port | 5432 ||database.
|database.database | vnpy |database.user | postgresql
|database.user |postgres |database.password |postgresql
|database.password | 123456 |

Please note that VeighNa does not actively create databases for relational databases, so please make sure that the database corresponding to the filled database.database field has been created. If the database has not been created, connect to it manually and run this command:
```sql
    create database <filled database.database>;
```


## Introduction to non-SQL databases

### MongoDB

MongoDB is a non-relational database based on distributed document storage (bson format) with the following characteristics:
 - Document-oriented storage, operation is relatively simple;
 - Supports rich storage types and data operations;
 - Built-in hot data memory cache to achieve faster read and write speeds.

#### MongoDB Configuration Fields

When MongoDB is configured in VeighNa Trader, you need to fill in the following field information:

| Field Name | Value | Required or not |
|--------- |---- | ---|
|database.name | "mongodb" | Required |
|database.host | address | required |
|database.port | Port | Required |database.
|database.database | Database Name | Required |database.user | Database Name | Required |database.user | Database Name | Required
|database.user |User name|Optional |database.password |Optional
|database.password | Password | Optional |database.
|database.authentication_source | [Database used to create the user][AuthSource]|| Optional |

A sample MongoDB configuration with authentication is shown below:

| field name | value |
|--------- |---- |
|database.name | mongodb |
|database.host | localhost |
|database.port | 27017 |
|database.database | vnpy |
|database.user | root |
|database.password | |
|database.authentication_source | vnpy |

[AuthSource]: https://docs.mongodb.com/manual/core/security-users/#user-authentication-database

### InfluxDB

InfluxDB is a non-relational database designed specifically for storing time-series data with the following features:
- Columnar data storage provides extremely high read and write efficiency;
- Running in the mode of independent service process, it can also support the concurrent access requirements of multiple processes.

You need to select version 2.0 of InfluxDB during installation.

Please note that the cmd running influxd.exe needs to be kept running, if it is closed, it will cause InfluxDB to exit, or you can use some auxiliary tools to register it as a Windows service running in the background.

#### InfluxDB configuration fields
When InfluxDB is configured in VeighNa Trader, the following fields need to be filled in:

| Field Name | Value | Required or not |
|--------- |---- | ---- |
|database.name | "influxdb" | Required |
|database.host | Address | Required |
|database.port | "influxdb" | Required |
|database.host | Address | Required
|database.port | Port | Required |
|database.database | Database name | Required |
|database.user | Database name | Required |
|database.user | Database name | Required
|database.user |User name | Required |
|database.password |User name |Required
|database.user |User name | Required |
|database.password |Password | Required |

A sample InfluxDB configuration is shown below:

|field name |value |
|--------- |---- |
|database.name | influxdb |
|database.host | localhost |
|database.port | 8086 |
|database.database |vnpy |
|database.user |root |
|database.password | 12345678 |

### DolphinDB

DolphinDB is a high-performance distributed time-series database developed by Zhejiang Zhi Yu Technology Co., Ltd. It is especially suitable for low-latency or real-time tasks that require high speed, and is characterized by the following features:
- Columnar analytical (OLAP) database with a hybrid engine (based on memory and hard disk), taking full advantage of the cache to accelerate;
- Native partitioned table storage , reasonable partitioning scheme allows the CPU multi-threaded parallel loading of data within each partition ;
- Support for efficient data compression , significantly reducing hard disk storage space at the same time , but also significantly reduce the overhead of IO communication .

Although DolphinDB is commercial software, a free community edition is also available. You need to select the [2.0 Beta](https://github.com/dolphindb/release/blob/master/2.00/README.md) version during installation.

Please note:
 - The cmd that runs dolphindb.exe needs to be kept running, if it is closed it will cause DolphinDB to exit, or you can also use some auxiliary tools to register it as a Windows service running in the background;
 - Because DolphinDB does not currently support Python 3.10, VeighNa Studio 3.0.0 does not provide DolphinDB support.

#### DolphinDB Configuration Fields

The following fields need to be filled in:

| Field Name | Value | Required or not |
|--------- |---- | ---- |
|database.name | "dolphindb" | Required |
|database.host |Address | Required |
|database.port | Port | Required |
|database.database | Database Name | Required |
|database.user |User name | Required |
|database.password |Password | Required

A sample DolphinDB configuration is shown below:

|field.name |value |
|--------- |---- |
|database.name | dolphindb |
|database.host | localhost |
|database.port | 8848 |
|database.database | vnpy |
|database.user | admin |
|database.password |123456|

### Arctic

Arctic is a high-performance financial time-series database developed by Man AHL, a UK quantitative hedge fund, based on MongoDB with the following features:
- Supports direct storage of DataFrame in pandas and ndaaray objects in numpy;
- Allows versioning of data (similar to git in a database), facilitating the iterative management of data in the factor mining process;
- Based on chunked storage and LZ4 compression, it saves a lot of resources in terms of network and disk IO, and achieves ultra-high performance data query.

Please note that VeighNa Studio 3.0.0 does not provide Arctic support because Arctic does not currently support Python 3.10.

#### Artic Configuration Fields

| field name | value | required or not |
|--------- |---- | ---- |
|database.name | "arctic" | Required |
|database.host |Address | Required |
|database.port | Port | Required |

A sample Arctic configuration is shown below:

|field.name |value |
|--------- |---- |
|database.name | arctic |
|database.host | localhost |
|database.database | vnpy |

### Level DB
LevelDB is a high-performance Key/Value database introduced by Google with the following features:
- Positioned as a general-purpose data storage solution;
- Based on the LSM algorithm to achieve in-process storage engine;
- Support for billions of levels of massive data.

Please note that VeighNa Studio 3.0.0 does not provide LevelDB support because LevelDB does not support Python 3.10 at this time.

#### LevelDB Configuration Fields
| field name | value | required or not |
|--------- |---- | ---- |
|database.name | "leveldb" | Required |
|database.database | "leveldb" | Required |
|database.port | Port | Required |

A sample LevelDB configuration is shown below:

|field.name |value |
|--------- | ---- |
|database.name | leveldb |
|database.database | vnpy_data |


## Database Configuration (Using MySQL as an Example)

This document describes the database configuration process using MySQL as an example.

First download the Windows version of the installation package [MySQL Installer for Windows] from the [MySQL official website](https://dev.mysql.com/downloads/) as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/1.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/2.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/3.png)

After the download is completed, you will get the installation package in msi format, double-click it to open it and select [Full] mode to install MySQL, and click the [Next] button all the way to complete the installation.

Click on the [Next] button to complete the installation. [](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/4.png)

The installation process will automatically download related components from the website, first click [Execute] button to complete, and then click [Next] button.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/5.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/6.png)

The installation process will ask for a password 3 times, here for the convenience of demonstration, we will set the password to 1001, please use a more complex and secure password in your own installation process.  
After the installation is complete, MySQL WorkBench, the graphical management tool for MySQL, will be opened automatically. Click [Database] -> [Connect to Database] in the menu bar, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/7.png)

In the pop-up dialog box, directly select the default database Local Instance MySQL, and then click [OK] button to connect to the MySQL database server.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/8.png)

In the database management interface that opens automatically, click the button in the red box in the menu bar in the figure below to create a new database. Enter "vnpy" in [Name], and then click the [Apply] button below to confirm.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/9.png)

In the Database Script Execution Confirmation dialog box that pops up, click [Apply] as well, and you have completed all operations in MySQL WorkBench.

After that, start VeighNa Trader, click [Configuration] in the menu bar, and set the database related fields:

- name should be changed to mysql (please note the case);
- database should be changed to vnpy;
- host is the local IP, i.e. localhost or 127.0.0.1;
- port is MySQL's default port 3306;
- The port is MySQL's default port 3306. The user username is root.
- The password is the same as 1001.

```json
    database.name: mysql
    database.database: vnpy
    database.host: localhost
    database.port: 3306
    database.user: root
    database.user: root database.password: 1001
```

After filling in the fields, the following image is shown:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/database/22.png)

After saving the configuration changes, restart VeighNa Trader to enable the new database configuration. After restarting, if there are no errors when opening VeighNa Trader, the MySQL database configuration is successful. 


## Scripting

Before using the script, please configure the database according to the above, and call the corresponding function interface when using the script.

### Script loading

#### loads the required packages and data structures into the script.

```python 3
from datetime import datetime
from typing import List
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.database import get_database
from vnpy.trader.object import BarData, TickData

# Get the database instance
database = get_database()
```

#### Configure the specific parameter data for the desired contract

```python 3
# Contract code, 888 is a continuous contract for rice baskets, only for demonstration purposes, please change the contract code according to your needs.
symbol = "cu888"

# Exchange, the exchange of the target contract
exchange = Exchange.SHFE

# Historical data start time, accurate to day
start = datetime(2019, 1, 1)

# Historical data end time, to the nearest day
end = datetime(2021, 1, 20)

# Time granularity of the data, here the example uses day level
interval = Interval.DAILY
```

#### Database read operation

Returns an empty list if there is no data in the database for the specified period of time.

```python 3
# Read k-line data from the database
bar1 = database.load_bar_data(
    symbol=symbol,
    exchange=exchange,
    interval=interval,
    start=start, end=end
    end=end
)

# Read the tick data from the database
tick1 = database.load_tick_data(
    symbol=symbol,
    symbol=symbol, exchange=exchange.
    start=start, end=end
    end=end
)
```

#### Database write operations

Please note that **bar_data** and **tick_data** are not shown in the example. If you need to write them as script, please refer to the source code or other ways to convert them to the data structure in the example.

```python 3
# The k-line data to be deposited, please get it and convert it to the required form.
bar_data: List[BarData] = None

database.save_bar_data(bar_data)

# k-line data to be saved, please get it yourself and convert it to the required form.
tick_data: List[TickData] = None

# Save the tick data to the database
database.save_tick_data(tick_data)
```

#### Database deletion operation

Cannot be recovered, please proceed with caution

```python 3
# Delete k-line data from database
database.delete_bar_data(
    symbol=symbol,
    exchange=exchange,
    interval=interval
)

# Delete tick data from the database
database.delete_tick_data(
    symbol=symbol,
    exchange=exchange
)
```
