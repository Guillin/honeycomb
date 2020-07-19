# make_dataset.py
#!/usr/bin/env python
# coding: utf-8
# Import libraries
import logging
import pandas as pd
from pathlib import Path
import argparse
import config

# LOAD DATASET
def load_data(input_file):
    data  = pd.read_csv(f"{config.INPUT_PATH}{input_file}.csv", sep=config.CSV_SEP)

    return data

# SAVE DATASET
def save_data(output_file, data):
    
    data.to_pickle(config.OUTPUT_PATH + f'{output_file}.pkl')
    
    return 0

# PROCESS DATA
def process_data(data):
    """ You must define here how to process the dataframe before be saved
    """
    # drop duplicates
    data.drop_duplicates(inplace=True)
    
    # ****************************************************** # 
    # put here what you think is needed to process your data
    data["target"] = data["y"].map({"no":0, "yes":1})
    data.drop('y', axis=1, inplace=True)
    # ****************************************************** #

    return data
    pass

def main(input_file, output_file):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('INIT: making final data set from raw data')

    logger.info('RUN: Loading data')
    df = load_data(input_file)
   
    logger.info(f'RUN: Data size before be processed: {df.shape}')
    
    logger.info(f'RUN: Processing data')

    df = process_data(df)

    logger.info(f'RUN: Data size after be processed: {df.shape}')

    logger.info(f'RUN: Saving data')
    save_data(output_file, df)

    logger.info('END: raw data processed.')

if __name__ == "__main__":
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    print("project_dir: ", project_dir) # quitar


    parser = argparse.ArgumentParser()
    parser.add_argument( "--input_file",   required=True, 
        help="Specify file name without extension from raw folder to be processed.", type=str)
    parser.add_argument( "--output_file",   required=True, 
        help="Specify output file name which will be saved into folder processed.", type=str)

    args = vars(parser.parse_args())
    
    main(input_file=args['input_file'], output_file=args['output_file'])