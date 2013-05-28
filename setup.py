#!/usr/bin/env python
from distutils.core import setup

DISTNAME = 'tract_querier'
DESCRIPTION = \
        'Complex queries for full '\
        'brain tractographies with '\
        'a registered template on top of them'
LONG_DESCRIPTION = ''  # open('README.rst').read()
MAINTAINER = 'Demian Wassermann'
MAINTAINER_EMAIL = 'demian@bwh.harvard.edu'
URL = ''
LICENSE = ''
DOWNLOAD_URL = ''
VERSION = '0.1'


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(quiet=True)
    config.add_subpackage('tract_querier')
    return config


if __name__ == "__main__":
    setup(
          name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'
             ],
            scripts=[
                'scripts/tract_querier',
                'scripts/tract_outlier_rejection',
                'scripts/tq_map_image_to_tracts',
                'scripts/tract_to_mask',
                'scripts/kappa',
                'scripts/tract_math'
              ],
            **(configuration().todict())
    )