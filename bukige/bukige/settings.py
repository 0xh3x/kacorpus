# Scrapy settings for bukige project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bukige'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['bukige.spiders']
NEWSPIDER_MODULE = 'bukige.spiders'
DEFAULT_ITEM_CLASS = 'bukige.items.BukigeItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

