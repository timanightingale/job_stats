# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:32:48 2020

@author: ТОМА
"""

import argparse
from main import *

path_from="data/test.tsv"
path_to="data/test_proc.tsv"

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='path to files')
    parser.add_argument('in_file',  type=str, nargs='+')
    parser.add_argument('out_file',  type=str, nargs='+')
    args = parser.parse_args()
    
    path_from=args.in_file[0]
    path_to=args.out_file[0]
    
    run_proc(path_from,path_to)    
