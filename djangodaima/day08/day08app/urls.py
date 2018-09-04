from django.conf.urls import url
from  .views import *

urlpatterns = [
    url(r"^send_mail$", send_my_email),
    url(r"send_mail_mail_v1$",send_email_v1),
    url(r"^verify$", verify),
    url(r"^active/(.+)", active)
]