import string
import random

def generate_biz_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))