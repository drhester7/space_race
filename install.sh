#!/bin/bash

uv pip install -e .

GREEN='\033[0;32m'
BLUE='\033[0;34m'

config_dir="$HOME/.space_race"
config_file="$config_dir/config.json"
tasks_file="$config_dir/tasks.json"

if [ ! -d "$config_dir" ]; then
    mkdir "$config_dir"
    printf "${GREEN}Created %s directory.\n" "$config_dir"
else
    printf "${BLUE}Existing config directory found.\n"
fi

if [ ! -f "$config_file" ]; then
    config=$(printf '{
    "space_race": {
        "tasks_file": "%s"
    }
}' "$tasks_file")

    echo "$config" >"$config_file"
    printf "${GREEN}Created %s.\n" "$config_file"
else
    printf "${BLUE}Existing config file found.\n"
fi
