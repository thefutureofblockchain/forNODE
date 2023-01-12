
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
def chartize(bp=0, pf=0, wsd=0, mun=0):
    cars = ['bp', 'pf', 'wsd','mun']
    data = [bp,pf,wsd,mun]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = cars)
    plt.savefig('debate_analysis.png')