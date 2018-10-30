# -*- coding:utf-8 -*-
#

import smtplib


#定义发送邮件函数
def Sendmail(to_addr_list = [],subject_header = 'Test',body = 'This is just for test'):
    #邮件主题
    subject_header = 'Subject: ' + subject_header + '\r'
    #发送服务器smtp地址
    mail_server = 'smtp.163.com'
    #发送服务器smtp端口
    mail_server_port = 25
    #发件人邮件地址
    from_addr = 'sendmail151@163.com'
    #邮件的头信息
    from_header = 'From: %s\r' % from_addr
    #引用smtplib模块
    smtp = smtplib.SMTP()
    #连接发送邮件服务器
    smtp.connect(mail_server,mail_server_port)
    #登陆smtp服务器
    smtp.login('sendmail151@163.com','Earl1211')
    #如果body为列表转换为文本
    infos=''
    if isinstance(body,list):
        for info in body:
           infos = infos + '\n' +  info
        #print infos
    else:
        infos=body
    #多个邮件地址的批量发送
    for to_addr in to_addr_list:
        to_header = 'To: %s\r' % to_addr
        #邮件文本信息
        email_message = '%s\n%s\n%s\n\r\n%s' %(from_header,to_header,subject_header,infos)
        #发送邮件
        # print('send to %s \n%s' %(to_addr, email_message))
        smtp.sendmail(from_addr, to_addr, email_message)
    #退出smtp服务器
    smtp.quit()


#主函数
if __name__ == '__main__':
    body = '''
  text line1
  text line2
  text line3'''
    Body = ['This is new email','Username:guom@mutantbox.com','Password:test']
    to_addr_list = ['meng.guo@neocraftstudio.com']

    try:
        Sendmail(to_addr_list = to_addr_list,subject_header='New email header', body=Body)
        print('Send mail success ...')
    except Exception as e:
        print(e)