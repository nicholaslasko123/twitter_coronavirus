#!/usr/bin/env python3

import argparse
import json
import os
import operator
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

# Parse command-line arguments
cli_parser = argparse.ArgumentParser()
cli_parser.add_argument("--input_path", required=True, help="Path to the JSON file")
cli_parser.add_argument("--key", required=True, help="Key to process within the JSON data")
cli_parser.add_argument("--percent", action="store_true", help="Normalize counts to percentages")
opts = cli_parser.parse_args()

# Load JSON data from the specified file
with open(opts.input_path, "r") as file_handle:
    data = json.load(file_handle)

# If percent flag is set, normalize counts using the totals in '_all'
if opts.percent:
    for item in data[opts.key]:
        data[opts.key][item] /= data['_all'][item]

# Sort the items by count (and then by key) and get the top 10 entries
sorted_items = sorted(data[opts.key].items(), key=operator.itemgetter(1, 0))
top_entries = sorted_items[-10:]
names = []
counts = []
for label, count in top_entries:
    names.append(label)
    counts.append(count)

# Determine the x-axis label based on the input file's name
if "country" in opts.input_path:
    x_axis_label = "countries"
else:
    x_axis_label = "languages"

# Set up and generate the bar chart
plt.figure(figsize=(10, 6))
plt.bar(names, counts, color="skyblue")
plt.xlabel(x_axis_label)
plt.ylabel("{} occurances".format(opts.key))
plt.title("Top 10 {} by {}".format(x_axis_label, opts.key))
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a PNG file
output_filename = opts.input_path + opts.key + ".png"
plt.savefig(output_filename)

