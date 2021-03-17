# Assignment 3 - MSR
# Generator is a python script used to prepare and generate parts of the assignment 2

import glob
import csv
import os
import sys
import re
import shutil
import subprocess
from pathlib import Path

# base paths - ⚠️ warning: Do not move any files the whole thing breaks apart
dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = 'data'
input_path = data_path + '/input'
temp_path = data_path + '/temp'
output_path = data_path + '/output'
assignment2_path = temp_path + '/assignment2'
original_repo_path = input_path + '/original_repo/msr4flakiness'
test_folder = temp_path + "/test_files"
test_cases_folder = temp_path + "/test_cases"
test_tokens_folder = temp_path + "/samples_flaky/test_tokens"
process_path = './process'


def main():
    # Step 0 - copy assignment 2 process files
    print('Step 0 : Copying base files to the input directory -- Please wait..')

    #shutil.copy(assignment2_path + '/process/actuall.py',
    #            process_path + '/actuall.py')
    shutil.copy(assignment2_path + '/process/initialization.sh',
                process_path + '/initialization.sh')

    # step 1 - Delegate the work to actuall.py
    print('We are now running actuall.py in Simulation mode')
    os.system('python ' + process_path + '/actuall.py ' + 'SIMULATE')

    # step 2 - prepare raw CSV files


if __name__ == '__main__':
    main()
