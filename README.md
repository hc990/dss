let
===
http://www.csdn123.com/html/20130308/59/996b984961a548854b9b8daf049910e5.htm


1./etc/default/syslogd，把其中的 SYSLOGD="" 改为 SYSLOGD="-r"。

2.在 /var/log 下新建 firewall 目录，用于保存日志文件。目录属性750
3. /etc/syslog.conf
local4.*  -/var/log/firewall/firewall.log
4.在syslog.conf文件中的syslog和messages定义前面加上了 !local4.*


