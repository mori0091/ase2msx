from setuptools import setup, find_packages
from ase2msx.cli import VERSION

setup(
    name="ase2msx",
    version=VERSION,
    description='Generate MSX2 sprite data from Aseprite, for libmsx',
    author='Daishi Mori',
    author_email='mori-d@qc4.so-net.ne.jp',
    license='MIT',
    license_file='LICENSE',
    url='https://github.com/mori0091/libmsx',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      ase2msx = ase2msx.cli:main
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)
