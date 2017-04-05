from setuptools import setup

setup(name='slacker',
      version='0.1',
      description='Slack log handler',
      url='https://github.com/pranav93/slacker',
      author='Pranav Ambhore',
      author_email='ambhore.pranav@gmail.com',
      license='MIT',
      packages=['slacker'],
      install_requires=[
          'slackweb',
      ],
      zip_safe=False)
