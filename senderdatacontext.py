import psycopg2
from config import DatabaseConfig


class SenderDataContext():
    def __init__(self, logger, config: DatabaseConfig):
        self.logger = logger
        self.config = config

    def get_sms_to_send(self):
        smsToSend = []
        try:
            connection = psycopg2.connect(user=self.config.user,
                                          password=self.config.password,
                                          host=self.config.host,
                                          port=self.config.port,
                                          database=self.config.database)
            cursor = connection.cursor()
            query = "select * outbox"

            cursor.execute(query)
            sms_records = cursor.fetchall()

            self.logger.debug("Sms retrieved in database")
            for sms in sms_records:
                smsToSend.append(sms)

        except (Exception, psycopg2.Error) as error:
            self.logger.error(
                "Error while fetching data from PostgreSQL ".join(error))

        finally:
            # closing database connection.
            if connection:
                cursor.close()
                connection.close()
                self.logger.debug("PostgreSQL connection is closed")
        return smsToSend
