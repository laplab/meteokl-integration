import tornado.ioloop
import tornado.web
from models import Entry
import signal
import logging as log
import json
import config

log.basicConfig(
    format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=log.ERROR,
    filename='server.log'
)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            last_saved = Entry.select().get()
        except Entry.DoesNotExist:
            self.clear()
            self.set_status(204)
            self.finish('No data in weather database')
            return

        serializable = [
            last_saved.inner_temperature,
            last_saved.outer_temperature,
            last_saved.pressure,
            last_saved.humidity,
            last_saved.wind_speed,
            last_saved.wind_direction
        ]
        
        self.write(json.dumps(serializable))
        

app = tornado.web.Application([
    (r'/api/weather', MainHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static', 'default_filename': 'index.html'}),
], debug=config.serverIsDebug)

def start_tornado():
    log.info('Starting tornado...')
    app.listen(config.serverPort)
    tornado.ioloop.IOLoop.current().start()

def stop_tornado(signum, stackframe):
    log.info('Stopping tornado...')
    tornado.ioloop.IOLoop.current().stop()

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, stop_tornado)
    signal.signal(signal.SIGINT, stop_tornado)

    start_tornado()
