import os
from subprocess import Popen
import pynentry
import re


class LP_Session:
    def __init__(self, user):
        self.user = user

    def __enter__(self):
        p = pynentry.PynEntry()
        p.description = 'Enter your LastPass Password'
        p.prompt = '>'
        passwd = p.get_pin()
        passwd = passwd + '\n'
        env = os.environ.copy()
        env['LPASS_DISABLE_PINENTRY'] = '1'
        lp = Popen(
            f'lpass login {self.user}'.split(), stdin=-1, stdout=-1, stderr=-3, env=env)
        outs, err = lp.communicate(passwd.encode('utf8'), timeout=20)
        print((outs, err))
        assert b'Success' in outs

    def __exit__(self, exc_type, exc_value, traceback):
        with Popen(['lpass', 'logout', '-f'], stdout=-1, stderr=-1) as lp:
            ans = lp.communicate(timeout=5)
            print(ans)


def list():
    lp = Popen(['lpass', 'ls'], stdout=-1)
    print(lp.communicate(timeout=5))


if __name__ == '__main__':
    with LP_Session('laharah22@gmail.com'):
        list()
