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
import pandas as pd

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

    shutil.copy(assignment2_path + '/process/actuall.py',
                process_path + '/actuall.py')
    shutil.copy(assignment2_path + '/process/initialization.sh',
                process_path + '/initialization.sh')

    # step 1 - Delegate the work to actuall.py
    print('We are now running actuall.py in Simulation mode')
    os.system('python ' + process_path + '/actuall.py ' + 'SIMULATE')
    print('Simulation is done we have the main rerun file created out of logs ✅✅✅')

    # step 2 - create a 1% sample set from the original
    all_reruns = pd.read_csv(input_path + '/' + 'all_reruns.csv', header=None)
    sample_count = all_reruns.count()[0] * 0.01
    randomized_sample = all_reruns.sample(round(sample_count))
    randomized_sample['sample_run'] = ''
    randomized_sample.to_csv(temp_path + '/sample_runs.csv', index=False,
                             header=['dir', 'test', 'first_result', 'frequency', 'flaky', 'sample_run'])

    # step 3 - refer to jupyter
    print('We have now all the files necessary -- Please refer to the iPython notebook: comparison.ipynb')

if __name__ == '__main__':
    main()
