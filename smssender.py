from deamon import Daemon
from smsengine import SmsEngine
from senderdatacontext import SenderDataContext


class SmsSender(Daemon):
    def run(self):
        self.smsEngine = SmsEngine(self.logger)
        self.senderdatabasecontext = SenderDataContext(self.logger, self.config.database)
        self.logger.info("test")
