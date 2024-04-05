"""
Django settings for AppProject project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-g)!_1dm#4ql7slum^&252+nwokmpw19flu2i%4t_)@%wq@uh%1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

"""
错误信息 AttributeError: 'User' object has no attribute 'follow' 表明在测试环境中，尽管您定义了 CustomUser 模型并且在其中实现了 follow 方法，但是在测试时创建的用户实例并没有这个方法。这通常是因为Django没有使用您的自定义用户模型 CustomUser，而是使用了默认的用户模型。
要解决这个问题，请确保您已经在项目的 settings.py 文件中正确设置了 AUTH_USER_MODEL 指向您的自定义用户模型。例如，如果您的应用名为 authAPP，并且您的自定义用户模型类名为 CustomUser，则应该这样设置：
"""
AUTH_USER_MODEL = "authAPP.CustomUser"
""" """

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_extensions',
    "authAPP",
    "dynamic",
    "message",
    "reserve",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "AppProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "AppProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_api',
        'USER': 'root',
        'PASSWORD': '156156',
        'HOST': 'localhost',  # 本地数据库通常是'localhost'
        'PORT': '3306',  # MySQL默认端口是3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.authAPP.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.authAPP.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.authAPP.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.authAPP.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
