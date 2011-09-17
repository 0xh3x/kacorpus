# Scrapy settings for libge project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'libge'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['libge.spiders']
NEWSPIDER_MODULE = 'libge.spiders'
DEFAULT_ITEM_CLASS = 'libge.items.LibgeItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

