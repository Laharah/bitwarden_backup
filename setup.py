from setuptools import setup

setup(
    name='bw-backup',
    version='1.0.0',
    url='',
    license='MIT',
    author='laharah',
    author_email='laharah22+ca@gmail.com',
    description='Script to download an encrypted backup of a BitWarden vault with Attachments.',
    install_requires=[
        'docopt >= 0.5.0',
        'pynentry >= 0.1.0',
    ],
    scripts=['bw-backup'],

)
