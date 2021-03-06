# -*- coding: utf-8 -*-

# Copyright 2014,  Digital Reasoning
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

from setuptools import setup, find_packages


def test_python_version():
    major = sys.version_info[0]
    minor = sys.version_info[1]
    micro = sys.version_info[2]
    if float('%d.%d' % (major, minor)) < 2.6:
        err_msg = ('Your Python version {0}.{1}.{2} is not supported.\n'
                   'stackdio-server requires Python 2.6 or newer.\n'.format(major, minor, micro))
        sys.stderr.write(err_msg)
        sys.exit(1)

# Set version
__version__ = '0.0.0'  # Explicit default
with open('stackdio/client/version.py') as f:
    exec(f.read())


SHORT_DESCRIPTION = ('A cloud deployment, automation, and orchestration '
                     'platform for everyone.')

# Use the README.md as the long description
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

CFG_DIR = os.path.expanduser("~/.stackdio-cli")

requirements = [
    'Jinja2==2.7.3',
    'PyYAML==3.11',
    'cmd2==0.6.7',
    'keyring==3.7',
    'requests>=2.4.0,<2.6.0',
    'simplejson==3.4.0',
]

testing_requirements = [
    'coveralls',
    'pep8',
    'pylint<=1.2.0',
]

if __name__ == "__main__":
    test_python_version()

    # Call the setup method from setuptools that does all the heavy lifting
    # of packaging stackdio-client
    setup(
        name='stackdio',
        version=__version__,
        url='http://stackd.io',
        author='Digital Reasoning Systems, Inc.',
        author_email='info@stackd.io',
        description=SHORT_DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license='Apache 2.0',
        include_package_data=True,
        packages=find_packages(),
        data_files=[
            (CFG_DIR,
                [
                    'bootstrap.yaml',
                ]),
            (os.path.join(CFG_DIR, "blueprints"),
                ["blueprints/%s" % f for f in os.listdir("blueprints")]),
        ],
        zip_safe=False,
        install_requires=requirements,
        dependency_links=[],
        extras_require={
            'testing': testing_requirements,
        },
        entry_points={
            'console_scripts': [
                'stackdio-cli=stackdio.cli:main',
                'blueprint-generator=stackdio.cli.blueprints:main',
            ],
        },
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: System :: Clustering',
            'Topic :: System :: Distributed Computing',
        ]
    )
