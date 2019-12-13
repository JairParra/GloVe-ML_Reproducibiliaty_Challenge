# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:54:43 2019

@author: jairp
"""

### Simple script to creat vocabulary for the vectors 
 

import os
import argparse
from random import seed
from random import randint

seed(42)


def obtain_vectors_vocab(vectors_PATH, encoding = 'utf-8'): 
    """ 
    Obtains the vocabulary for the  input vectors
    """
    vocab = [] 
    
    with open(vectors_PATH,'r', encoding = encoding ) as vectors_file: 
        vocab = [ (line.split(' ')[0] + " " + str(randint(0,71290)) )  for line in vectors_file.readlines()]
        vectors_file.close()
        
    return vocab


def save_vectors_vocab(vocab, saving_path, encoding = 'utf-8'): 
    """
    Saves vectors vocabulary in txt format
    """

    with open(saving_path, 'w', encoding=encoding) as vocab_file: 
        for word in  vocab: 
            vocab_file.write(word + "\n") 
        vocab_file.close()
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--vectors_file', default='vectors.txt', type=str)
    parser.add_argument('--encoding', default = 'utf-8', type = str)    
    parser.add_argument('--saving_path', default = os.path.join(os.getcwd(), "default_vocab.txt"), type = str)
    args_main = parser.parse_args() 
        
    # vocabulary reading 
    vocab = obtain_vectors_vocab(args_main.vectors_file, encoding=args_main.encoding) 

    if args_main.vectors_file == 'vectors.txt' and args_main.saving_path == os.path.join(os.getcwd(), "default_vocab.txt"): 
        save_vectors_vocab(vocab, args_main.saving_path)  # save with default name 
    elif args_main.vectors_file != 'vectors.txt' and args_main.saving_path == os.path.join(os.getcwd(), "default_vocab.txt"): 
        vocab_name = args_main.vectors_file[:-3] + "_vectors.txt" # obtain saving name 
        save_vectors_vocab(vocab_name, args_main.saving_path)
        
        
    