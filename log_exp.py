import logging

# DEBUG from calculator: "something happend" on 21-9-2001 at 10:30:30

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%d-%m-%y at  %I:%M:%S%p',
                    filename='calculator.log',
                    level=logging.DEBUG)

logging.debug('Debugging')
logging.info('Util information')
