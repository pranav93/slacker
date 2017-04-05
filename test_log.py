log_info = dict(
    version=1,
    formatters={
        'compact': {
            'format': '%(asctime)s [%(levelname)-8.8s] %(name)-10.10s : %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s [%(levelname)-8.8s] %(name)-8.8s [%(filename)-15.15s:%(lineno)-3.3s]: %(message)s'
        },
        'err_report': {
            'format': '%(asctime)s\n%(message)s'
        }
    },
    handlers={
        'slack_jabber': {
            'class': 'slacker.SlackHandler',
            'url': 'https://hooks.slack.com/services/xyz',
            'channel': 'pranavdev',
            'username': 'crash_jabber',
            'icon_emoji': ':ghost:'
        },
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    loggers={
        '': {
            'handlers': ['default'],
            'level': 'DEBUG'
        },
        'crash': {
            'handlers': ['default', 'slack_jabber'],
            'level': 'ERROR',
            'propagate': False
        }
    }
)


import logging
import logging.config

logging.config.dictConfig(log_info)
logger = logging.getLogger('crash')

logger.error('lol')
