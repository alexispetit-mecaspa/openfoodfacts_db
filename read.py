#!/usr/bin/python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*-coding:Utf-8 -*

"""
  read.py
  Author : Alexis Petit
  Date : 2018 02 17

  This scrip read the database of OpenFoodFacts
"""

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime

def read_db(name_db):
  
  df = pd.read_csv(name_db,sep='\t')#,nrows=100)
  header = df.columns
  header = [item.strip() for item in header]
  df.columns = header

  print 'Number of products : ',len(df)

  #print df.head(5)
  origin = df["origins"].values
  list_origin = []
  for item in origin:
    if item not in list_origin:
      list_origin.append(item)

  print list_origin
  print 'Number of country : ',len(list_origin)
  
if __name__ == "__main__":

  name_db = "en.openfoodfacts.org.products.csv"  
  read_db(name_db)
