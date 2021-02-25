#### Test_Assistant

---

doc/  文档

img/   图片素材

syslog/   运行log

utils/  常用方法

——Ass_util.py  常规用方法

——CP_util.py   Tab CP中常用方法

——AP_util.py   Tab AP中常用方法

ui/

——main_ui.py   主界面ui

——at_settings_ui.py   AT管理界面ui

——default_settings_ui.py   默认设置界面ui

AP.py    Tab AP操作

CP.py    Tab CP操作

_at_settings   AT界面操作

default_settings  默认设置界面操作

start.py   main方法

---


hello


#### Tab1 AT

##### 功能

- [x] 蓝牙状态
- [x] Wifi状态
- [x] Wifi信息
- [x] SIM卡状态
- [x] SD卡状态
- [x] 设备log抓取

##### 测试项

- [x] reboot重启

  

#### Tab2 CP

##### 功能

- [x] 端口检测
- [x] 串口选择
- [x] 波特率
- [x] 串口开关
- [x] 常用命令快捷键（可自定义）

##### 测试项

- [x] 主叫主挂：终端通过串口连接pc，通过ATD;拨打默认号码，对端需要接听后，5s后终端主动挂断

​					完整流程：["拨号"，"对端振铃"，"对端接听"，"通话结束"]

- [x] 主叫被挂：终端通过串口连接pc，通过ATD;拨打默认号码,，对端响铃后， 5s后终端主动挂断

​					完整流程：["拨号"，"对端振铃"，"对端接听"，”通话结束"]

- [x] 主叫拒接：终端通过串口连接pc，通过ATD;拨打默认号码，对端响铃后，对端挂断

​					完整流程：["拨号"，"对端振铃"，"通话结束"]

- [x] 主叫未接：终端通过串口连接pc，通过ATD;拨打默认号码，对端响铃后，等待响铃结束，不接听

​					完整流程：["拨号"，"对端振铃"，“对端无应答，通话结束”]




 ***Q:***

 - wifi信息如果未联系，显示已搜到的wifi列表；如果已连接，显示已连接wifi的详细信息
 - 蓝牙详细信息显示已匹配过的设备名称
 - AT添加新指令，因格式或其他错误添加失败后无提示

问题：

​	1.选择测试项执行时会先打电话，而不是先提示开始测试，再进行测试内容的执行；多通电话下判断上一通电话是否结束，等待5s再进行下一通的电话

​	2.测试主叫接听时，拨号，对端响铃正常再接收区正常显示，对端接听无法捕获到，通话结束可以

添加一个流程列表，比如测试主叫接听，将每次运行的过程记录进去

['正在拨号', '对端响铃', '对端已接听', '通话结束']

拨打电话后如果用time，这个期间list不会添加步骤，尝试用thread，一边进行判断，一边进行process的收集

异常过程还未添加

20/11/17

- [ ] 入网检测确认入网状态后，再进行测试项的进行

  --- 现在在点击开始测试后，根据是否能够拨号成功判断能否开始测试

- [x] 增加修改配置的ui，包括默认被接号码，短信内容，默认测试次数



20/11/18

- [x] 测试项开始后，无法发送at指令

- [x] 测试结束后，在下方发送区可以发送成功AT指令，左侧选择AT指令无法显示返回结果

- [ ] tab CP 在下方发送区输入多行AT指令不会依次执行，卡死



20/12/25
JFP1301，1304等功能机使用atd;拨号，终端不会显示拨号界面，TT中会显示AT+CLCC返回，py串口未抓到，如果定时手动AT+DSCI?查询
时间间隔设置





#### Something

##### 2021年2月22日

进展：

1.之前功能机的AT通话流程无法送定时接收获取，需要设置AT^DSCI=1![image-20210222180949677](C:\Users\wangyanlin\AppData\Roaming\Typora\typora-user-images\image-20210222180949677.png)

，可以获取获取并判断通话状态

2.四项测试流程可以正常进行



Q:

1.完成一项测试后，选择下一项测试点击开始无法进行    √

2.ATD主动拨号功能机不显示界面，对端可以接收到

3.每回合测试完成后打印log（未添加） √

4.添加设置通话测试时间间隔  √

5.添加一个使用at+creg判断是否入网的method  √

6.AP 左侧界面宽度需要增加

7.默认设置修改后，Tab CP中测试项——测试次数未变化

8.将各个类分为多个文件，start.py调用



