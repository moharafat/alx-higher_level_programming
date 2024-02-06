#!/usr/bin/python3
"""Defining a file-writing function."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file 
load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file

obj = load_from_json_file("add_item.json")
save_to_json_file(obj, "add_item.json")