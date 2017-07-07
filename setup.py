from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'Programming Language :: Python2',
    ]

# calling the setup function 
setup(name='mygmap',
      version='1.0.0',
      description='send facebook msg',
      long_description=long_description,
      url='https://github.com/himanshu2454/facebook_msg_script',
      author='Himanshu Chouahan',
      author_email='hchouahan3654@gmail.com',
      packages=['msg'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='facebook chat messages'
)
