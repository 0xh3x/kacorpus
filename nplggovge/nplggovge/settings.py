# Scrapy settings for nplggovge project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'nplggovge'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['nplggovge.spiders']
NEWSPIDER_MODULE = 'nplggovge.spiders'
DEFAULT_ITEM_CLASS = 'nplggovge.items.NplggovgeItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

