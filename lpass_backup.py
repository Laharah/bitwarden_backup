import os
from subprocess import Popen
import pynentry
import re


class LP_Session:
    def __init__(self, user):
        self.user = user
        self.passwd = ''

    def __enter__(self):
        p = pynentry.PynEntry()
        p.description = 'Enter your LastPass Password'
        p.prompt = '>'
        passwd = p.get_pin()
        passwd = passwd + '\n'
        self.passwd = passwd
        env = os.environ.copy()
        env['LPASS_DISABLE_PINENTRY'] = '1'
        self.env = env
        print('Logging in...')
        lp = Popen(
            f'lpass login {self.user}'.split(), stdin=-1, stdout=-1, stderr=-3, env=env)
        outs, err = lp.communicate(passwd.encode('utf8'), timeout=20)
        try:
            assert b'Success' in outs
        except AssertionError:
            raise ValueError('Incorrect Password')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self.passwd
        print('Closing LastPass session...')
        with Popen(['lpass', 'logout', '-f'], stdout=-1, stderr=-1) as lp:
            ans = lp.communicate(timeout=5)



def export(session):
    p = Popen(['lpass', 'export'], stdin=-1, stdout=-1, stderr=-1, env=session.env)
    p.stdin.write(session.passwd.encode('utf8'))
    p.stdin.flush()
    p.stdin.close()
    print('Reading Vault Stream from LastPass...')
    return p.stdout


def encrypt(data_stream, filename, lp):
    with open(filename, 'wb') as output:
        in_fd, out_fd = os.pipe()
        args = f'gpg -c --cipher-algo AES256 --batch --armor --passphrase-fd {in_fd}'.split()
        with Popen(
                args, stdin=data_stream, stdout=output, stderr=-3,
                pass_fds=[in_fd]) as gpg:
            os.close(in_fd)
            print('Encrypting with AES256...')
            with open(out_fd, 'w') as of:
                of.write(lp.passwd)
            print(f'Writing data to {filename}...')
        print('Encryption finished...')


if __name__ == '__main__':
    filename = 'temp'
    try:
        with LP_Session('laharah22@gmail.com') as lp:
            csv = export(lp)
            encrypt(csv, filename, lp)

    except ValueError:
        print('Incorrect Password!')
    else:
        print('Success!')
