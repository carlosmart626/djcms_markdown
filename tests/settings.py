from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'test-secret-key-not-for-production'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'easymde',
    'djcms_markdown',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SITE_ID = 1

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

CMS_CONFIRM_VERSION4 = True

CMS_TEMPLATES = [
    ('base.html', 'Base'),
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': 'English',
            'public': True,
        },
    ],
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
}

LANGUAGES = [('en', 'English')]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
