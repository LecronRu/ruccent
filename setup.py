from setuptools import setup, find_packages

with open('README.md') as file:
    description = file.read()


with open('requirements.txt') as file:
    requirements = [_.strip() for _ in file]


setup(
    name='ruccent',
    version='1.0.1',

    description='Pure Python, no dependencies, simple word accent setter, based on ngram model.',
    long_description=description,
    long_description_content_type='text/markdown',

    url='https://github.com/lecronru/ruccent',
    author='Lecron',
    author_email='lecronru@gmail.com',
    license='MIT License',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='natural language processing, russian',

#    packages=find_packages(),
    packages=['ruccent'],
    package_data={
        'ruccent': [
            '*.mdl',
        ]
    },
    setup_requires=['wheel'],
    install_requires=requirements,
)
