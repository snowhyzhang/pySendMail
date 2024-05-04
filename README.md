# Python发送邮件

一个使用Python来发送邮件的案列

## 使用方法

### 邮箱设置

在`src.mail.mail_settings.py`中，可以设置邮箱服务的参数，例如邮箱服务器地址、端口等信息。这些参数可以查看你所使用的邮箱服务说明。

### 收件人列表

默认的收件人列表可以写在`mail_config/receiver_list`中，每行为一个收件人邮箱。你也可以修改`src.mail.mail_settings.py`中`load_receivers`方法来定义自己的获取收件人列表方法。

### 邮件内容

默认邮件内容你可以在`mail_config/mail_content`中，可以写纯文本、HTML等，在发送邮件方法中指定内容类型即可。

### 发送邮件

调用`src.mail.mail.py`中的`send_mail`方法发送邮件即可。
