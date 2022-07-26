import os.path
import logger

def read():
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            logger.debug('High_score reading')
            return int(file.read())
    else:
         return 0


def save(score):
    logger.debug('High_score saved')
    with open('high_score.txt', 'w') as file:
        file.write(str(score))
