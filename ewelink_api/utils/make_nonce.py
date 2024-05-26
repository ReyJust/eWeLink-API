import random
import string


def make_nonce():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=7))
