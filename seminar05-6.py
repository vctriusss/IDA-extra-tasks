import requests
from functools import lru_cache
import time


def clock(func):
    def clocked(*args):
        t_start = time.time()
        res = func(*args)
        total_time = time.time() - t_start

        print(f'Function executed in {total_time:.3f}s')

        return res

    return clocked


def history(active=True, size=128):
    def decorate(func: callable):
        history = [None for _ in range(size)] if active else []
        def decorated_function(arg):
            res = func(arg)
            if active:
                history.pop(0)
                history.append(arg)

                print(f'Last {size} calls:')
                for i in range(size - 1, -1, -1):
                    print(f'{size - i}) {"-" if (history[i] is None) else history[i]}')
            return res
        return decorated_function
    return decorate



def cache_decorator(cache_type, N=None, K=None):
    def decorate(func: callable):
        if N is None:
            return func

        last_calls = dict()
        max_size = None if N == -1 else N
        @history(active=K is not None, size=K)
        @lru_cache(maxsize=max_size if cache_type == 1 else 0)
        def decorated_function(arg):
            if cache_type == 1:
                return func(arg)

            r = last_calls[arg] if (arg in last_calls) else func(arg)
            if len(last_calls) == N and arg not in last_calls:
                k = next(iter(last_calls))
                last_calls.pop(k)
            last_calls[arg] = r
            return r

        return decorated_function
    return decorate

@clock
@cache_decorator(cache_type=2, N=3, K=3)
def get_miem_teacher_full_name(email):
    time.sleep(1)
    name, domain = email.split('@')
    r = requests.get(
        f'https://devcabinet.miem.vmnet.top/public-api/user/email/{name}%40{domain}')
    if r.json()['data'] is None:
        return 'Not found'
    else:
        return r.json()['data']['fullName']

from random import choice
emails = ['vbashun@miem.hse.ru', 'vminchenkov@hse.ru', 'uq3dtr3rxuq3@hse.ru', 'oevsyutin@hse.ru', 'kzhanashia@hse.ru', 'sartamonov@miem.hse.ru']
for i in range(10):
    print(get_miem_teacher_full_name(choice(emails)))
    print()
