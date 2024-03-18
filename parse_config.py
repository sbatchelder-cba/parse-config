"""
parse_config.py
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
    parser = argparse.ArgumentParser(description="Parse config file")
    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument("-f", "--config_file", help="Relative path of config file", required=True)
    return parser

devops_keys = ["context", "mvn-compile-args", "mvn-test-args", "dockerfile", "py-test-args" ]
output_keys = ["name", "tech",  "context", "mvn-compile-args", "mvn-test-args", "py-test-args", "py-requirements", "dockerfile", "sq-project-key", "artifact-destination", "kaniko-build-args", "kaniko-labels" ]

def set_config(key, value):
    """set_config"""
    file_path = "$CLOUDBEES_OUTPUTS/" + key
    try:
        expanded_file_path = os.path.expandvars(file_path)
        with open(expanded_file_path, 'a') as file:
            # Write content to the file
            file.write(value)
        print(f"Content written to {expanded_file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

def parse_config(config_file):
    """parse_config"""
    # Step 1: Open Config file
    if not os.path.exists(config_file):
        sys.exit("File does not exist")

    with open(config_file, "r", encoding="utf8") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    # print("DEBUG: Config: " + str(config['cb-platform']['component'][0]))
    # iterate through all Components (today, assume 1 component)
    for i in range(len(config['cb-platform']['component'])):
        # print("DEBUG: " + str(config['cb-platform']['component'][i]))

        # Separate
        devops_set = set(devops_keys)
        overridable_keys = set(config['cb-platform']['component'][i].keys()) & devops_set
        dev_keys = set(config['cb-platform']['component'][i].keys()) - devops_set
        remaining_keys = set(output_keys) - dev_keys -overridable_keys

        print("Dev Keys")
        # Set the dev keys
        for key in dev_keys:
            set_config(key, config['cb-platform']['component'][i][key])

        print("Overridable Keys")
        # Set overridable keys
        for key in overridable_keys:
            set_config(key, config['cb-platform']['component'][i][key])

        # Set remaining keys to null

        print("Remaining Keys")
        for key in remaining_keys:
            set_config(key, "null")

def main() -> None:
    """main"""
    parser = init_argparse()
    args = parser.parse_args()
    # print(f'Arguments: {args}')
    if args.config_file:
        parse_config(args.config_file)
        print("Completed successfully")
    else:
        print("Error: config_file field not configured correctly")

main()