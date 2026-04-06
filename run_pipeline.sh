#!/bin/bash
cd "$(dirname "$0")"
python3 blog_pipeline.py >> logs/pipeline.log 2>&1
