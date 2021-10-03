from setuptools import setup

from src import animal_avatar

setup(
    name='animal_avatar',
    version=animal_avatar.__version__,
    description='SVG avatar generator.',
    long_description=animal_avatar.__doc__,
    author_email='johnherbertdillinger@ukr.net',
    license='MIT',
    platforms='any',
    url='https://github.com/Nacht1gall/animal-avatar-generator',
    download_url='https://github.com/Nacht1gall/animal-avatar-generator/archive/refs/heads/master.zip',
    keywords=['AVATAR', 'SVG'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
