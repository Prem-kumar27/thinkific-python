from setuptools import setup, find_packages

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='thinkific',
    version='0.1.1',
    description='Python Client wrapper for Thinkific API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Premkumar',
    author_email='sprem1997@gmail.com',
    url='https://github.com/Prem-kumar27/thinkific-python',
    download_url='https://github.com/Prem-kumar27/thinkific-python/archive/refs/tags/v0.1.1.tar.gz',
    keywords=['thinkific','thinkific-api','thinkific-lms'],
    packages=find_packages(),
    install_requires=['requests'],
    license='MIT',
    
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
    ]
)