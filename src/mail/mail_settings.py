"""
@author: snowhyzhang
@file: mail_settings.py
@time: 2024/5/4 16:35
@desc: 读取发送EMail的设置信息，如邮箱服务设置、收件人列表，收件信息等。
"""

# 设置邮箱服务，例如QQ邮箱、网易邮箱等，参看具体的邮箱服务说明
MAIL_HOST = 'smtp.qq.com'  # 例如QQ邮箱地址
MAIL_PORT = 465  # 例如QQ邮箱发送端口
# 设置发送者邮箱
MAIL_SENDER = 'example@qq.com'
# 邮箱服务Secret，参看具体邮箱服务获取方法
MAIL_SECRET = 'mail-secret'

# 设置邮件标题
SUBJECT = '测试标题'
# 设置发送者名称
FROM_NAME = 'pySendMail'


def load_receivers(file_name: str = 'mail_config/receiver_list') -> []:
    """
    读取邮箱列表
    默认配置在文件mail_config/receiver_list，格式为每行一个收件人地址
    :param file_name:
    :return:
    """
    receivers = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line:
                receivers.append(line.strip())

    return receivers


def load_content(file_name: str = 'mail_config/mail_content') -> str:
    """
    读取邮件内容，可以扩展成任何自己需要的内容
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        return f.read()
