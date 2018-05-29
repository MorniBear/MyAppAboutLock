import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'MyAppAboutLock.settings'

if __name__ == '__main__':

    send_mail(
        '老哥垃圾邮件',
        '老哥垃圾邮件',
        'mornibear@sina.com',
        ['saoguang@vip.qq.com'],
    )
