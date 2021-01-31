# -*- coding: utf-8 -*-

from resources.lib.scrobbler import scrobblerService
from phate89lib import kodiutils  # pylint: disable=import-error

#from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, utils  # pylint: disable=import-error

kodiutils.log('Addon {} starting {} scrobbling service (version {})'.format(kodiutils.ID, kodiutils.NAME, kodiutils.VERSION))
try:
    scrobblerService().run()
except Exception as exc:
    kodiutils.log('scrobblerService Exception: {}'.format(str(exc)))

kodiutils.log('Addon {} shutting down {} scrobbling service (version {})'.format(kodiutils.ID, kodiutils.NAME, kodiutils.VERSION))
