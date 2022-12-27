#!/usr/bin/env bash

pip3 install -r requirements.txt

OUTPUT_DIR="./out"
HYDRA_OUTPUT="./outputs"
if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Creating output directory..." ${OUTPUT_DIR}
  mkdir "$OUTPUT_DIR"
fi

if [ -d "$HYDRA_OUTPUT" ]; then
  echo "Removing hydra outputs directory..." ${HYDRA_OUTPUT}
  rm -r "$HYDRA_OUTPUT"
fi

python3 src/main.py