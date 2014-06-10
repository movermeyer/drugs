""" Logger configuration tips."""
import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s\tPID:%(process)d ' +
            '[%(module)s: %(name)s THREAD:%(thread)d] %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s\tPID:%(process)d ' +
            '[%(name)s] %(message)s'
        },
    },
    'filters': {
    },
    # https://docs.python.org/2/howto/logging.html#useful-handlers
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': '/tmp/app.log',
            'mode': 'a',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'default': {
            'handlers': ['null', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

logging.config.dictConfig(LOGGING)
getLogger = logging.getLogger
