"""
@author: snowhyzhang
@file: mail.py
@time: 2024/5/4 16:48
@desc: 发送邮件方法
"""
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

import src.mail.mail_settings as ms


def send_mail(content_type: str = 'plain', attachment_path: str = None):
    """
    发送邮件
    :param content_type: 邮件类型，例如：plain(纯文本)、html(html格式)
    :param attachment_path: 附件路径，默认为None
    :return:
    """
    msg_obj = MIMEMultipart("alternative")
    # 读取邮件内容
    content = MIMEText(ms.load_content(), content_type, 'utf-8')
    msg_obj.attach(content)
    # 设置附件
    if attachment_path:
        with open(attachment_path, 'rb') as file:
            # 将内容类型（Content-Type）设置为application/octet-stream，表示附件是一个二进制文件。这里的octet-stream
            # 指的是“八位字节流”，即一个原始的、未解释的二进制数据流。
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            # 增加header
            attachment.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(attachment_path)}",
            )
            msg_obj.attach(attachment)
    # 设置邮件标题
    msg_obj['From'] = formataddr((ms.FROM_NAME, ms.MAIL_SENDER))
    msg_obj['subject'] = ms.SUBJECT
    # 设置收件人
    # 读取收件人列表
    receiver_list = ms.load_receivers()
    msg_obj['TO'] = ','.join(receiver_list)
    # 设置抄送人
    # msg_obj['CC'] = ','.join(receiver_list)
    # 设置密送人
    # msg_obj['BCC'] = ','.join(receiver_list)
    try:
        smtp_server = smtplib.SMTP_SSL(host=ms.MAIL_HOST, port=ms.MAIL_PORT)
        smtp_server.login(ms.MAIL_SENDER, ms.MAIL_SECRET)
        smtp_server.sendmail(ms.MAIL_SENDER, receiver_list, msg_obj.as_string())
        smtp_server.quit()
    except smtplib.SMTPException as e:
        print("邮件发送失败：", e)
