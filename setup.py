#  MexPyro - Custom fork of Pyrogram (Telegram MTProto API Client Library)
#  Copyright (C) 2025 Fajar Ikhsan
#
#  This file is part of MexPyro.
#
#  MexPyro is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MexPyro is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with MexPyro.  If not, see <http://www.gnu.org/licenses/>.

import re
from sys import argv
from setuptools import setup, find_packages

from compiler.api import compiler as api_compiler
from compiler.errors import compiler as errors_compiler

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("pyrogram/__init__.py", encoding="utf-8") as f:
    version = re.findall(r'__version__ = "(.+)"', f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

if len(argv) > 1 and argv[1] in ["bdist_wheel", "install", "develop"]:
    api_compiler.start()
    errors_compiler.start()

setup(
    name="mexpyro",  # <--- ganti supaya beda dari PyPI resmi
    version=version,
    description="MexPyro: Custom fork of Pyrogram with extra features & patches",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/memex2711/mexpyro",
    download_url="https://github.com/memex2711/mexpyro/releases/latest",
    author="Fajar Ikhsan",
    author_email="",
    license="LGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords="telegram chat messenger mtproto api client library python mexpyro fork",
    project_urls={
        "Tracker": "https://github.com/memex2711/mexpyro/issues",
        "Community": "https://t.me/pyrogram",
        "Source": "https://github.com/memex2711/mexpyro",
        "Documentation": "https://docs.pyrogram.org",
    },
    python_requires="~=3.7",
    package_data={
        "pyrogram": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
    install_requires=requires
)
