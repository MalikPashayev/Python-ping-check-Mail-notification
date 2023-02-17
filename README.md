# Python-ping-check-Mail-notification
Python ping test code. Email sending function in case of interruption

In this code, the ping_ips function is the same as your previous code, but now the send_email function is called when the ping fails. This function sets the sending e-mail address, sending e-mail account password, receiving e-mail address and SMTP server settings. Next, an email message is created using the email.mime.text module and sent using the smtplib module. If this operation fails, you will receive an error message.

Note: This sample code is designed for Gmail accounts and may require some different settings for other email service providers.
