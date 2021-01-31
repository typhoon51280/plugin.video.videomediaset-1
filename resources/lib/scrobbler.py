import xbmc # pylint: disable=import-error
from phate89lib import kodiutils  # pylint: disable=import-error

class scrobblerService:

    def __init__(self):
        kodiutils.log('[scrobblerService] scrobblerService init', 4)

    def run(self):
        # startup_delay = kodiutils.getSettingAsNum('startup_delay')
        # if startup_delay:
        #     kodiutils.log("Delaying startup by {} seconds.".format(startup_delay), 4)
        #     xbmc.sleep(startup_delay * 1000)

        kodiutils.log("[scrobblerService] scrobblerService thread starting.", 4)

        # setup event driven classes
        self.Player = player()
        self.Monitor = monitor()

        # start loop for events
        while not self.Monitor.abortRequested():

            if self.Monitor.waitForAbort(10):
                # Abort was requested while waiting. We should exit
                break

        # we are shutting down
        kodiutils.log("[scrobblerService] scrobblerService shut down.", 4)

        # delete player/monitor
        del self.Player
        del self.Monitor


class monitor(xbmc.Monitor):
    def __init__(self, *args, **kwargs):
        kodiutils.log("[scrobblerService] monitor initialiazed", 4)

class player(xbmc.Player):
    def __init__(self, *args, **kwargs):
        kodiutils.log("[scrobblerService] monitor initialiazed", 4)
    
    def onAVStarted(self):
        kodiutils.log("[scrobblerService] onAVStarted", 4)
        if self.isPlayingVideo():
            kodiutils.log("[scrobblerService] isPlayingVideo", 4)
            self.seekTime(300)
        else:
            kodiutils.log("[scrobblerService] NOT isPlayingVideo", 4)