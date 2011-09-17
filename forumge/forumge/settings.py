# Scrapy settings for forumge project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'forumge'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['forumge.spiders']
NEWSPIDER_MODULE = 'forumge.spiders'
DEFAULT_ITEM_CLASS = 'forumge.items.ForumgeItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

DOWNLOADER_MIDDLEWARES = {
    'forumge.middlewares.Ignoreduplicates': 543,
}
