# from datetime import datetime
import time


def get_epoch() -> int:
    # return int(datetime.timestamp(datetime.now()))

    return int(time.time())
