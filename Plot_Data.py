# -*- coding: utf-8 -*-

"""
Created on 2020-02-28
by Jibin Joseph -joseph57

Assignment 06 - Graphing Data with Python

Revision 03-2020-04-14
Modified to add comments
"""

## Import the required packages
import numpy as np
import matplotlib.pyplot as plt
import sys

## Check the command lines options before accepting
## Check for python script file name, input file and output file name
if len(sys.argv)!=3:
    print("Requires the format python <py_program.py> <input_file> <output_file>")


## Read the arguments from the command line and use them as i/o filename
input_filename=sys.argv[1]
output_filename=sys.argv[2]

## Open the file (using genfromtxt()) and use header to define the array names
data_graph=np.genfromtxt(input_filename,
                         dtype=['int','float','float','float','float','float','float'],
                         names=True,delimiter='\t')

plt.figure(1) ## Create an empty figure numbered 1
## Create the first subplot LINE PLOT
plt.subplot(311) #or (3,1,1)
plt.plot(data_graph['Year'],data_graph['Mean'],'k',label="Mean Streamflow")
plt.plot(data_graph['Year'],data_graph['Max'],'r',label="Max Streamflow")
plt.plot(data_graph['Year'],data_graph['Min'],'b',label="Min Streamflow")
plt.xlabel('Year',fontsize=7)
plt.ylabel("Streamflow ("+r"$ft^3/s$"+" or cfs)",fontsize=7)#my first trial to use latex expression in python
plt.title("Line Plot showing Mean, Maximum, Minimum Streamflow",fontsize=7)
plt.legend(loc='upper left',frameon=True,fontsize=5)
##As y values are high, it offsets the y label towards left, so work-around
plt.ticklabel_format(style='sci',axis='y',scilimits=(1,4))
plt.ylim(data_graph['Min'].min(),1.1*data_graph['Max'].max())

## Create the second subplot SCATTER PLOT
plt.subplot(312) #or (3,1,2)
plt.scatter(data_graph['Year'],data_graph['Tqmean']*100,color='m',marker='*',label="Tqmean")
plt.xlabel('Year',fontsize=7)
plt.ylabel("Tqmean (%)",fontsize=7)
plt.title("Scatter Plot showing Annual Values of Tqmean",fontsize=7)
plt.legend(loc='upper left',frameon=True,fontsize=5)


## Create the third subplot BAR PLOT
plt.subplot(313) #or (3,1,3)
plt.bar(data_graph['Year'],data_graph['RBindex'],facecolor='g',label="RBindex")
plt.xlabel('Year',fontsize=7)
plt.ylabel("RBindex (ratio)",fontsize=7)
plt.title("Bar Plot showing RBindex",fontsize=7)
plt.legend(loc='upper left',frameon=True,fontsize=5)

## Title for the centered title to the figure
plt.suptitle("PLOTS FOR INPUT FILE: "+sys.argv[1],fontsize=10)

## Tweak the spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=1)

## Save the plot as pdf
plt.savefig(output_filename+".pdf")
plt.close()
