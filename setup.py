from setuptools import setup

setup(
    name='lpass-backup',
    version='1.0.0',
    url='',
    license='MIT',
    author='laharah',
    author_email='laharah22+ca@gmail.com',
    description='Script to download an encrypted backup of a LastPass vault.',
    install_requires=[
        'docopt >= 0.5.0',
    ],
    scripts=['lpass-backup'],

)