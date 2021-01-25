BOT_NAME = 'transforma'

SPIDER_MODULES = ['transforma.spiders']
NEWSPIDER_MODULE = 'transforma.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'transforma.pipelines.TransformaPipeline': 100,

}