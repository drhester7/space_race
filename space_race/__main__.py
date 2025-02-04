from .classmodule import tech_class
from .funcmodule import *


def main():
    # load config
    config_file_path = os.path.join(
        os.path.expanduser("~"), ".space_race/config.json")
    config = load_json(config_file_path)

    tech = tech_class(config)

    args = parse_args()
    if args.command == "init":
        tech.init_tech(args.name, args.description)
    elif args.command == "start":
        tech.start_research(args.name)
    elif args.command == "stop":
        tech.halt_research(args.name)
    else:
        print("Invalid command. Use --help for usage instructions.")


if __name__ == '__main__':
    main()
