#! /usr/bin/env python3

import os, sys, yaml
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

def has_yaml_frontmatter(filepath):
    with open(filepath, "r") as f:
        first_line = f.readline()
        return first_line.strip() == "---"

def get_formatted_ctime(file):
    ctime = os.path.getctime(file)
    return datetime.fromtimestamp(ctime).strftime('%Y%m%dT%H%M%S')

def get_file_yaml_data(file):
    with open(file) as f:
        lines = f.readlines()
        start, end = [i for i, l in enumerate(lines) if l.strip() == "---"][:2]
        return yaml.safe_load("".join(lines[start+1:end]))

def get_tag_string_for_filename(string):
    joined_tag = "_".join(string)
    return joined_tag

def get_file_title_from_yaml_title(string):
    return string.lower().replace(" ", "-")

def get_file_filename_combined(identifier, title, tags):
    return identifier + "--" + title + "__" + tags + ".md"


def main():

    filetimeidentifier = (get_formatted_ctime(filename))
    file_yaml_data = (get_file_yaml_data(filename))
    
    file_yaml_identifier = (file_yaml_data['identifier'])
    file_yaml_title = (file_yaml_data['title'])
    file_yaml_tags = (file_yaml_data['tags'])
    file_filename_tags = (get_tag_string_for_filename(file_yaml_tags))
    file_filename_title = (get_file_title_from_yaml_title(file_yaml_title))
    file_filename_combined = (get_file_filename_combined(filetimeidentifier, file_filename_title,
                                                     file_filename_tags))

    print(filetimeidentifier)
    print(file_yaml_identifier)
    print(file_yaml_title)
    print(file_filename_title)
    print(file_yaml_tags)
    print(file_filename_tags)
    print(file_filename_combined)
    print("original: " + filename)

if not has_yaml_frontmatter(filename):
    print("File does not have YAML frontmatter.")

    sys.exit(1)

if __name__ == '__main__':
    main()
