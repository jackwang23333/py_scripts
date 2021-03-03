#coding: utf-8

from textnow import textnow_sms
import os
import random
import time
usernames = os.environ["TEXTNOW_USERNAME"].split(',')
passwords = os.environ["TEXTNOW_PASSWORD"].split(',')
cookies = os.environ["TEXTNOW_COOKIES"].split('##,##')


import datetime
utc = time.strftime("%Y-%m-%d %H:%M:%S")
UTC_FORMAT = "%Y-%m-%d %H:%M:%S"
utc_time = datetime.datetime.strptime(utc, UTC_FORMAT)
local_time = utc_time + datetime.timedelta(hours=8)
if len(usernames) != len(passwords) :
  print(u"账号和密码个数不对应")
  quit()
elif len(usernames) != len(cookies) :
  print(u"账号和Cookie个数不对应")
  quit()
else:
  print(u"共有 %s 个账号，即将开始保号处理" % len(usernames))

print(u"共有 %s 个账号，即将开始保号处理" % len(cookies))

numbers = os.environ["TEXTNOW_NUMBER"]
#msg = os.environ["TEXTNOW_MSG"]
msg = local_time
for idx in range(0,len(usernames)):
  username = usernames[idx]
  password = passwords[idx]
  cookie = cookies[idx]
  text = textnow_sms.Textnow(numbers, msg, username, password, cookie)
  text.send_text()
  print("---第%s个账号处理完毕---" % (idx+1))

print("---Good Job! 所有账号处理完毕---")
