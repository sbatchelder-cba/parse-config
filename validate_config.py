"""
validate_config.py
    Return a map of the yaml config to be consumed by future steps in platform

Inputs
    config_file
Outputs
    config
"""

import os
import sys
import argparse
import yaml
def init_argparse() -> argparse.ArgumentParser:
    """init_argparse"""
    parser = argparse.ArgumentParser(description="Validate config file")
    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument("-f", "--config_file", help="Relative path of config file", required=True)
    return parser

def validate_config(config_file):
    """validate_config"""
    # Step 1: Open Config file
    if not os.path.exists(config_file):
        sys.exit("File does not exist")

    # with open(config_file, "r", encoding="utf8") as file:
    #     config = yaml.load(file, Loader=yaml.FullLoader)

    # Step 2: Validate Config file
    # stubbed
    print("INFO: Config File Validated!")

def main() -> None:
    """main"""
    parser = init_argparse()
    args = parser.parse_args()
    # print(f'Arguments: {args}')
    if args.config_file:
        validate_config(args.config_file)
    else:
        print("Error: config_file field not configured correctly")

main()