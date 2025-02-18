#!/bin/sh
# Define the directory containing the dataset
DATASET_DIR="/data/Twitter dataset"

# Loop over each matching file in the dataset directory
for file in "$DATASET_DIR"/geoTwitter20-*-*.zip; do
  echo "Launching process for $file"
  nohup python3 src/map.py --input_path="$file" > "${file}_nohup.log" 2>&1 &
done

echo "All map.py processes have been started."

