#!/usr/bin/env python3.9
import logging
import shutil
import os

logging.basicConfig(level=logging.INFO)


def run_analysis():
    logging.info("start of processing")
    src = os.environ['INPUT_DIR']
    dest = os.environ['OUTPUT_DIR']
    print('copying', src, 'to', dest)

    shutil.copytree(src, dest, dirs_exist_ok=True)
    print('copied', src, 'to', dest)
    raise Exception('unexpected error!')
    logging.info("end of processing")


run_analysis()
