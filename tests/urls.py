from django.urls import include, re_path

urlpatterns = [
    re_path(
        r"^otp/",
        include("phone_login.urls", namespace="phone_login"),
    ),
]
