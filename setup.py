from distutils.core import setup
from crpapi import __version__,__license__,__doc__

license_text = open('LICENSE').read()
long_description = open('README.md').read()

setup(name="python-crpapi",
      version=__version__,
      py_modules=["crpapi"],
      description="Libraries for interacting with the CRP API",
      author="Ben Pilkerton",
      author_email = "bpilkerton@gmail.org",
      license=license_text,
      url="http://www.opensecrets.org/action/api_doc.php",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )

