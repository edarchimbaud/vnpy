# Ubuntu Installation Guide

## Check Python

Check the local Python version, you need to need version 3.7 or higher, you can run the python command at the command line to see.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/40.png)


### Install VeighNa

### Download source code

Download VeighNa source code (for Ubuntu system, please choose tar.gz format):

- [VeighNa Github download address](https://github.com/vnpy/vnpy/releases)
- [VeighNa Gitee download address](https://gitee.com/mirrors/vn-py/releases)

Unzip the file with the tar command after the download is complete, as shown below.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/41.png)

### Perform a one-click installation

Before installing VeighNa, you need to install the gcc compiler for compiling C++ class interface files. Run the following command in the terminal:

```
sudo apt-get update
sudo apt-get install build-essential
```

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/39.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/43.png)

Then go to the VeighNa source code directory (containing the install.sh file) that you extracted earlier

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/42.png)

Open a terminal and run the following command to perform a one-click installation:

```
sudo bash install.sh
```

Note that if the python softlink name is not python, such as python3 or python3.10, run the following command:

```
sudo bash install.sh your python softconnect
```

The overall one-click installation process is divided into 3 steps:

1. download and install the ta-lib library and numpy;
2. install the relevant dependencies in the requirements.txt file;
3. install VeighNa itself.

> If you are running on a virtual machine, please set the RAM to 4G or more, otherwise it will report insufficient memory.


## Launch VeighNa Trader

Go to the directory where you extracted the VeighNa source code and find the file run.py in the folder examples/veighna_trader.

Click the right mouse button to open the terminal and enter the following command to start VeighNa Trader:

```
python run.py 
```

Please note that run.py contains a lot of startup add-ons (trading interfaces and application modules), please modify and adjust them according to your operating system and actual trading needs (if you need to load interfaces, just cancel the comment symbols before the interfaces).

Please note that some interfaces do not support Ubuntu system, please do not load. Please refer to the chapter on trading interfaces for details on connecting interfaces (you can check the operating systems supported by the interfaces).

> If some libraries are incompatible at startup, follow the instructions to re-pip install these libraries.


## Frequently Asked Questions

### Problems with the Python development environment

If you get the error "command 'gcc' failed with exit status 1" when installing Python, you may not have installed the Python development environment correctly. You can try to fix it by running the following command in the terminal:

```
sudo apt-get install your python softlink-dev
```

### Graphical driver troubleshooting

If you boot on an Ubuntu system with a graphical interface and get the error qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found, you can run the following command in the terminal to install libxcb-xinerama0 to try to resolve the problem: `` sudo apt-get install your python softwire-dev `` ### Graphical driver problem handling xinerama0 in the terminal to try to resolve the graphics driver dependency:

```
sudo apt-get install libxcb-xinerama0
```

### Chinese encoding issues

If the Ubuntu system language is English, the following error may occur when connecting to a CTP interface that uses the Chinese language:

terminate called after throwing an instance of 'std::runtime_error'
what(): locale::facet::_S_create_c_locale name not valid

You can use local-gen to install Chinese encoding to try to solve the problem:

```
sudo locale-gen zh_CN.GB18030
```
