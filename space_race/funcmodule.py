import json
import os
import argparse


def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)

    return {}


def parse_args():
    parser = argparse.ArgumentParser(
        prog='space_race',
        description='The space race was all about research and development. In the same way, learning happens constantly to increase value. This is a relativley simple utility to track time while learning.'
    )
    sub_parsers = parser.add_subparsers(dest='command')

    # Init command
    parser_init = sub_parsers.add_parser(
        "init",
        help="Initialize a new research task"
    )
    parser_init.add_argument(
        "name",
        help="Research Topic. AKA the tech you're researching."
    )
    parser_init.add_argument(
        "description",
        help="Tech description"
    )
    

    # Start command
    parser_start = sub_parsers.add_parser(
        "start",
        help="This command starts the clock on your tech research task."
    )
    parser_start.add_argument(
        "-n", "--name",
        default=None,
        help="Research Topic. AKA the tech you're researching."
    )

    # Stop command
    parser_stop = sub_parsers.add_parser(
        "stop",
        help="This command stops the clock on your tech research task."
    )
    parser_stop.add_argument(
        "name",
        help="Research Topic. AKA the tech you're researching."
    )

    sub_parsers.add_parser(
        "list",
        help="List all tasks"
    )

    # Delete comand
    parser_delete = sub_parsers.add_parser(
        "delete",
        help="Delete a task"
    )
    parser_delete.add_argument(
        "name",
        help="Research Topic. AKA the tech you're researching."
    )
    
    # Set command
    parser_set = sub_parsers.add_parser(
        "set",
        help="Set a default task"
    )
    parser_set.add_argument(
        "name",
        help="Research Topic. AKA the tech you're researching."
    )

    return parser.parse_args()
