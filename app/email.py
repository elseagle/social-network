from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
import os


def send_async_email(app, to, subject, template, **kwargs):
    with app.app_context():
        mail.send_email(
            from_email=app.config["MAIL_USERNAME"],
            to_email=to,
            subject=subject,
            html=template)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()

    thr = Thread(target=send_async_email, args=[app,to, subject, template])
    thr.start()
    return thr
