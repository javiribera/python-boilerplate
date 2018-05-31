#!/usr/bin/env python3
"""
Module Description.
"""

__author__ = "Javier Ribera"
__version__ = "0.1.0"

import argparse
from logzero import logger


def main(args):
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag",
                        action="store_true",
                        default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name",
                        action="store",
                        dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument("-v", "--verbose",
                        action="count",
                        default=0,
                        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s (v.{__version__})")

    args = parser.parse_args()
    main(args)
