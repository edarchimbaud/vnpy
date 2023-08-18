# Windows Installation Guide

Windows systems to which the installation steps in this document apply include:

- Windows 10/11
- Windows Server 2019

> Other versions of Windows systems may encounter various issues with dependent libraries during installation and are not recommended.

To install VeighNa on Windows systems, the official [VeighNa Studio Python distribution] is recommended, **especially for programming novices who are new to Python**.

As a one-stop Python environment for quantitative investment research trading, VeighNa Studio integrates:

- Python 3.10 64-bit (official Python version)
- VeighNa and other related dependent libraries
- VeighNa Station (graphical management tool for the VeighNa framework)

For users who are already more experienced in programming or need to use a specific Python distribution (e.g. Anaconda), a manual installation solution is also available.


## VeighNa Studio program

### Download and install

The VeighNa Studio installer can be downloaded from the [VeighNa official website](https://www.vnpy.com/).

After the download is complete, double-click the installation package to enter the VeighNa Studio Installation Wizard (we recommend right-clicking and selecting [Run as Administrator] for installation), and using the default settings click the [Quick Install] button to proceed with the VeighNa Studio installation, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/21.png)

> It is recommended to install VeighNa Studio in the default path of C:\veighna_studio, other VeighNa documents and tutorials use this directory as the VeighNa installation directory to explain.

If you want to personalize the installation, you can click [Customize Installation] to enter the Advanced Options page, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/24.png)

After the installation is complete, it will switch to the Installation Success page, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/26.png)

The VeighNa Station icon will appear on your desktop, double click the icon to run VeighNa Station.

### Use

After successful installation, start the command line tool to use VeighNa Studio Python distribution directly.

Type python to enter the interactive python environment as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/29.png)

At this point, typing python code on the command line will execute it immediately. If you want to run the example that comes with pyqtgraph, you can enter the following code in order:

```python 3
from pyqtgraph import examples
examples.run()
```

This brings up the run window for Examples, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/30.png)

Clicking on Basic Plotting on the left will bring up the graphical interface of the examples, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/31.png)

If you want to open jupyter lab for investment research, you can open cmd and type in jupyter lab to start it successfully, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/32.png)

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/38.png)

### Modify

If you want to add or remove a feature after installation, you can double-click the VeighNa Studio installation package to enter the VeighNa Studio installation interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

Click [Modify] to enter the modification page, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/35.png)

After selecting the optional features, click [Next] to enter the Advanced Options page, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/37.png)

After selecting, you can reinstall.

### Repair

If, after installation, the installation is incomplete or otherwise needs to be repaired, you can double-click the VeighNa Studio installation package to enter the VeighNa Studio installation screen, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

Click [Repair] to enter the repair interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/34.png)

After the repair is completed, it will switch to the Repair Success page, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/15.png)

### Uninstallation

If you want to uninstall VeighNa Studio, you can double-click the VeighNa Studio installation package to enter the VeighNa Studio installation interface, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/33.png)

Click [Uninstall] to enter the uninstallation interface, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/27.png)

After the uninstallation is completed, it will switch to the uninstallation success page, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/28.png)


### Manual installation program

### Prepare Python environment

First of all, please prepare the Python 3.10 64-bit environment on your computer (**Note that it must be the 64-bit version**). We recommend using the distribution from the Python official website, but you can also use Anaconda, Miniconda, Canopy and other distributions.

Here we take the distribution of Python official website as an example, first of all, download the installation file in [Python official website](https://www.python.org/downloads/windows/), select [Windows installer (64-bit)], as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/22.png)

After the download is complete, double-click the file into the Python installation wizard, check the [Add Python3.10 to PATH] option, click [Install Now] to install, recommended to use the default settings all the way to click [Next] until the installation is complete:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/install/23.png)


### Downloading and installing VeighNa  

Download VeighNa source code (zip format for Windows):

- [VeighNa Github download address](https://github.com/vnpy/vnpy/releases)
- [VeighNa Gitee download address](https://gitee.com/mirrors/vn-py/releases)

After the download is complete, unzip it, then launch a command line tool (CMD or PowerShell), go to the directory where the source code is located (i.e. where the install.bat file is located), and enter the following commands to run the script to perform a one-click install:

```
install.bat
```

The overall one-click installation process is divided into 3 steps:

1. Download and install the ta-lib library;
2. install the relevant dependency libraries inside the requirements.txt file;
3. install VeighNa itself.

If an error occurs during one of the installation steps, please save the error message on the command line (**prioritize the error message at the bottom**) and go to the VeighNa community forums to post a question for help.

### Starting VeighNa Trader

Start the command line tool, go to the directory where you extracted the VeighNa source code and find the file run.py in the folder examples/veighna_trader.

Enter the following command to start VeighNa Trader:

```
python run.py 
```

Please note that run.py contains a large number of startup add-ons (trading interfaces and application modules), so please modify and adjust them according to your operating system and actual trading needs (if you need to load interfaces, just remove the comment symbols in front of the interfaces).

For more information on connecting interfaces, please refer to the chapter on trading interfaces.

> If some libraries are incompatible at startup, follow the instructions to re-pip install these libraries.
