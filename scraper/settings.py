from django.conf import settings


setting_prefix = 'SCRAPER'

FETCH_URL_DOWNLOAD_TIMEOUT = getattr(settings, '{}_FETCH_URL_DOWNLOAD_TIMEOUT'.format(setting_prefix), 20)
USE_YOUTUBE_THUMBNAIL_TEMPLATE = getattr(settings, '{}_USE_YOUTUBE_THUMBNAIL_TEMPLATE'.format(setting_prefix), True)
