from django.urls import re_path

from .views import GenerateOTP, ValidateOTP

app_name = "phone_login"

urlpatterns = [
    re_path(r"^generate/$", GenerateOTP.as_view(), name="generate"),
    re_path(r"^validate/$", ValidateOTP.as_view(), name="validate"),
]
