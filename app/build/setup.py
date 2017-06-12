from setuptools import setup, find_packages

setup(
    name='Python Base Template',
    version='17.06',
    description='Base docker template for python projects',
    author='Joseph Niel Tuazon',
    author_email='josephnieltuazon@gmail.com',
    url='',
    license='MIT',
    keywords='python docker template',
    packages=find_packages(),
    install_requires=[
        'flask',
        'marshmallow',
    ]
)
