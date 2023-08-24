# VeighNa Station

## Launch the program ##

### Click on the icon to start

After successful installation, double-click the VeighNa Station shortcut on your desktop:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/1.png)

to run VeighNa Station.

### Command line startup

Open the command line tool and type veighna to start VeighNa Station.

### User Login

The first time you use VeighNa Station you will be prompted with the VeighNa Studio disclaimer as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/2.png)

After you read it carefully and click [Confirm], a user login screen with a user name input box, a password input box, a login button, and a registration button will pop up as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/3.png)

Users follow the requirements to enter the user name in the user name input box, enter the password in the password input box, then click the [Login] button to complete the login to enter the VeighNa Station main runtime program.

New users can click the [Register] button to register for an account, and then log in after registration is complete. Please note when registering.

- Please fill in your personal email address truthfully (subsequently used to retrieve your password and other forum functions);
- User name automatically use the registration of WeChat [nickname] (does not support changes). Password please keep in mind, the password is also used in the program;
- Please remember your password, which is also used to log in VeighNa Community Forum.

The **Login screen only pops up when you run VeighNa Station for the first time**, and you will be logged in automatically when you run VeighNa Station afterwards.

## Interface Window

Once you have logged in, the VeighNa Station interface will automatically pop up as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/4.png)

The interface is divided into several parts: Menu Bar, Title Bar, Function Bar, Main Display Area, Learning and Using Area, and Official Channel Area.

### Menu Bar

The menu bar is located at the top and contains two buttons, [System] and [Help].

#### Configuration

Click [System] - [Configuration], it will pop up the system configuration window, you can modify the PyPI index and pip proxy, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/5.png)

PyPI index is used to replace the pypiserver address used by VeighNa Station, when left empty the default used is https://pypi.org的PyPI服务器.

The pip proxy is empty by default, users can set it by themselves. After modification, you can click the [Save] button to save the configuration and exit the window.

#### Logout

Click [System] - [Logout], the logout window will pop up, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/6.png)

Clicking [Yes] will log out the user and close the program immediately. After the user is logged out, you need to log in the user again at the next startup.

#### Close

Clicking [System] - [Close] will bring up the exit window as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/7.png)

Click [Yes] to close the program immediately.


### Main window

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/9.png)

As shown in the picture above, the left area of the picture is the function bar and the right area is the main display area. The function bar includes Community, Trading, Investment Research, Encryption, and Updates. With different selections on the left side of the function bar, the right side of the main display area will show the corresponding related contents.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/10.png)

As shown above, the lower left corner of the VeighNa Station interface is the Learning and Use area.

Clicking [Documentation] will open the browser and jump to the official documentation https://www.vnpy.com/docs/cn/index.html , where users can check the detailed instructions.

Clicking [Community Help] will open the browser and jump to the official forum https://www.vnpy.com/forum/ , where users can check the technical post and post to exchange ideas.

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/11.png)

As shown in the picture above, below the Learning and Use area is the official channel area.

From left to right are the official Github repository, the official WeChat public number and the official Zhihu account. Clicking on them will open your browser and take you directly to the relevant pages.


### Functionality

### Community

Click the [Community] button on the left side of VeighNa Station, and the main display area on the right side will show the official forum, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/4.png)

Users can browse the official forum content in this area.

### Trading

Click the [Transaction] button on the left side of VeighNa Station, the main display area on the right side shows the transaction interface, application module selection area and information output area, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/12.png)

Click the white checkbox after the trading interface or application module that needs to be loaded to select it. Then click the [Start] button in the lower left corner of the main display area to start VeighNa Trader. at this time, the right output area will output the information of the program in operation, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/13.png)

Click the [Modify] button at the bottom right corner of the main display area to modify the running directory.

### Pitch

Click the [Pitch] button on the left side of VeighNa Station, the main display area on the right side will be the jupyterlab application operation directory, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/14.png)

After clicking the [Launch] button at the bottom left corner of the main display area, the jupyterlab application will be run in the operation directory specified at the bottom right corner, and you can conduct investment research operations in the jupyterlab application, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/15.png)

### Encryption

Click the [Encryption] button on the left side of VeighNa Station, and the main display area on the right side will show the encryption related contents, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/16.png)

Users can compile the selected .py file into a .pyd file to perform encryption operation on the strategy in this interface.

Click the [Select] button, select the path of the strategy file to be encrypted in the pop-up window, and click the [Open] button. The input field in the lower left corner of the main display area will be changed to the absolute path of the file to be encrypted, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/17.png)

Click the [Encrypt] button to compile the file. At this time, the center display area will output the information related to the encryption process, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/18.png)

When the output file encryption process is terminated, an encrypted pyd file will be generated at the location of the encrypted file.

Please note that after encryption, you need to **remove the .cp310-win_amd64 part of the pyd file name** before putting it into the self-built strategies folder.

### Update

Click the [Update] button on the left side of VeighNa Station, and the main display area on the right side shows the component update related content, as shown below:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/19.png)

Click the [Check] button on the bottom left corner of the main display area, and the locally installed modules and versions will be displayed, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/20.png)

Click the [Update] button at the bottom right corner of the main display area, the update process will be started in the background and relevant information will be output, as shown in the following figure:

![](https://vnpy-doc.oss-cn-shanghai.aliyuncs.com/veighna_station/21.png)

When the update is completed, a notification window will pop up, click [OK] and restart VeighNa Station.
