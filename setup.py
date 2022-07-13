from setuptools import setup
setup(
  name='ytmp',
  #packages=['someprogram'],
  version='0.1.0',
  #author='...',
  #description='...',
  entry_points={
        "console_scripts": [
            "ytmp = __main__:main",
        ],
  },
)
