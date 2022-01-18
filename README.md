<h1 align="center">Django Phone Login</h1>

<p align="center">
<a href="https://github.com/engineervix/django-phone-login/actions/workflows/main.yml" target="_blank">
  <img src="https://github.com/engineervix/django-phone-login/actions/workflows/main.yml/badge.svg" alt="Build Status">
</a>
<a href="https://codecov.io/gh/engineervix/django-phone-login" target="_blank">
  <img src="https://codecov.io/gh/engineervix/django-phone-login/branch/master/graph/badge.svg" alt="codecov">
</a>
<a href="https://github.com/engineervix/django-phone-login/commits/master" target="_blank">
  <img alt="GitHub commits since latest release (by SemVer)" src="https://img.shields.io/github/commits-since/engineervix/django-phone-login/latest/master">
</a>
</p>

This is a fork of <https://github.com/wejhink/django-phone-login> – an excellent package that allows for login via phone number with no additional passwords for the user to remember.

Django-phone-login uses [django-sendsms](https://github.com/stefanfoulis/django-sendsms) to send sms.

It's an easy way to grow your customer base without any hassle.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Installing Django Phone Login](#installing-django-phone-login)
- [Instructions](#instructions)
- [Adding to URLs](#adding-to-urls)
- [Customizable Fields in Settings.](#customizable-fields-in-settings)
- [Flow](#flow)
- [Why use django-phone-login?](#why-use-django-phone-login)
- [TODO](#todo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

> **Why this fork?**
>
> - because the [original project](https://github.com/wejhink/django-phone-login) seems not to be actively maintained anymore (last commit is in 2019).
> - the [original project](https://github.com/wejhink/django-phone-login) doesn't work well on recent versions of Django and Python (only supports Django < 2.0 and Python 2.7, <3.4)
> - I needed to add my own customisations

## Installing Django Phone Login

Django Phone Login was built for django.

PyPi, install using PIP:

```bash
pip install django-phone-login
```

If you want to install manually:

```bash
git clone git@github.com:wejhink/django-phone-login.git
cd django-phone-login/
pip install -r requirements.txt
python setup.py install
```

## Instructions

```python
INSTALLED_APPS += [
    ...  # Make sure to include the default installed apps here.

    'phone_login',
    'rest_framework',
    'rest_framework.authtoken',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}



AUTHENTICATION_BACKENDS = [
    'phone_login.backends.phone_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend'
]

# Make sure you also have backend Django Templates and APP_DIRS True, if you want to use default OTP Template.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        ...
    },
]


# Configure the SENDSMS_BACKEND (for django-sendsms integration)

SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend' #(defaults to 'sendsms.backends.console.SmsBackend')
SENDSMS_FROM_NUMBER = "+XXxxxxxxxxxx" 
SENDSMS_ACCOUNT_SID = 'ACXXXXXXXXXXXXXX'
SENDSMS_AUTH_TOKEN = 'xxxxxxxx' 

```

## Adding to URLs

Add the Below `urls.py`

```python
urlpatterns = [
    re_path(r'^phone_login/', include('phone_login.urls', namespace='phone_login'),),
]
```

## Customizable Fields in Settings.

```python
PHONE_LOGIN_ATTEMPTS = 10
PHONE_LOGIN_OTP_LENGTH = 6
PHONE_LOGIN_OTP_HASH_ALGORITHM = 'sha256'
PHONE_LOGIN_DEBUG = True  # will include otp in generate response, default is False.
```

## Flow

1. User enter the `phone_number` and sends request to generate `secret code`.
2. `django-phone-login` sends a `secret_code` as SMS to the phone number.
3. User sends `secret_code` to the server to verify.
4. `django-phone-login` verifies and send `token` as response using `DRF3`.

## Why use django-phone-login?

- Phone number login, no password required.
- Registration through phone number.
- Mobile based user authentication.

## TODO

- [ ] Update test matrix to have different Django versions (2.x to 4.x ?)

---
