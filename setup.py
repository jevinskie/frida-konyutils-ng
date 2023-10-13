#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.build import build
from setuptools_npm import npm_not_skipped


class custom_build(build):
    sub_commands = [
        ("npm_install", npm_not_skipped),
        ("npm_run", npm_not_skipped),
    ] + build.sub_commands


setup(cmdclass={"build": custom_build})
