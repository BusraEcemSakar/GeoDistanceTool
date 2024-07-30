from setuptools import setup, find_packages

def read_long_description():
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "A Python library for calculating distances between geographical coordinates."

setup(
    name='GeoDistanceTool',
    version='0.1',
    description='A Python library for calculating distances between geographical coordinates.',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    author='Busra Ecem Sakar',
    author_email='busra.ecem.sakar@gmail.com',
    url='https://github.com/BusraEcemSakar/GeoDistanceTool',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='geographical distance haversine vincenty',
    license='MIT',
)
