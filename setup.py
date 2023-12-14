import setuptools

VERSION = '1.1.0'

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='fincalc',
    version=VERSION,
    license='MIT',
    author='Mahyar Amiri',
    author_email='mmaahhyyaarr@gmail.com',
    description='A Financial Calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mahyar-amiri/fincalc',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
