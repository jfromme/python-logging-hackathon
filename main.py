#!/usr/bin/env python3.9
import contextlib
import shutil
import os
from pathlib import Path
from functools import wraps


def debug_logging(func):
    @wraps(func)
    def wrapper():
        log_dir = os.environ['OUTPUT_DIR']
        log_file = Path(log_dir, "analysis_log.txt")
        log_file.parent.mkdir(exist_ok=True, parents=True)

        f = open(log_file, 'w')
        import sys
        import logging
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler(stream=f)
        logger.addHandler(handler)

        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return

            logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

        sys.excepthook = handle_exception

        with contextlib.redirect_stderr(f), contextlib.redirect_stdout(f):
            func()

    return wrapper


@debug_logging
def run_analysis():
    print("start of processing")
    src = os.environ['INPUT_DIR']
    dest = os.environ['OUTPUT_DIR']
    print('copying', src, 'to', dest)

    shutil.copytree(src, dest, dirs_exist_ok=True)
    print('copied', src, 'to', dest)
    raise Exception('unexpected error!')
    print("end of processing")


run_analysis()
