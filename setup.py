from setuptools import find_packages, setup

with open('README.MD', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    authod='Pawan Rampal'
    author_email='pawanrampal@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_desciption=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pawanrampal/pgbackup',
    packages=find_packages('src')
)
