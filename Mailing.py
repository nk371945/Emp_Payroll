from pywin.scintilla.bindings import SendCommandHandler

from utilities import SendMail, PropertyFile


   #vskm.banupriya@gmail.com
SendMail.send_mail(PropertyFile.getValues('sender_mail'),
                   PropertyFile.getValues('receiver_mail'),
                   PropertyFile.getValues('subject'),
                   PropertyFile.getValues('text'),
                   PropertyFile.getValues('pre_file'),
                   PropertyFile.getValues('post_file'),
                   PropertyFile.getValues('report_url'),
                   PropertyFile.getValues('server'),
                   PropertyFile.getValues('port'),
                   PropertyFile.getValues('username'),
                   PropertyFile.getValues('password'))


