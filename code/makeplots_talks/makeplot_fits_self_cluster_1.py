#!/usr/bin/python 
import scipy 
import numpy 
import pickle
from numpy import * 
from scipy import ndimage
from scipy import interpolate 
from numpy import loadtxt
import os 
import numpy as np
from numpy import * 
import matplotlib 
from pylab import rcParams
from pylab import * 
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.pyplot import axes
from matplotlib.pyplot import colorbar
#from matplotlib.ticker import NullFormatter
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
s = matplotlib.font_manager.FontProperties()
s.set_family('serif')
s.set_size(14)
from matplotlib import rc
rc('text', usetex=False)
rc('font', family='serif')

def plotfits():
    file_in = "self_tags.pickle"
    file_in2 = open(file_in, 'r') 
    params, icovs_params = pickle.load(file_in2)
    params = array(params)
    file_in2.close()

    filein2 = 'starsin_test2.txt' # this is for self test this is dangerous - need to implement the same logg cut here, this is original data values or otherwise metadata 
    filein2 = 'starsin_new_all_ordered.txt' # this is for self test this is dangerous - need to implement the same logg cut here, this is original data values or otherwise metadata 
    filein2 = 'test4_selfg.txt' # this is for self test this is dangerous - need to implement the same logg cut here, this is original data values or otherwise metadata 
    a = open(filein2) 
    al = a.readlines() 
    names = []
    for each in al:
      names.append(each.split()[1]) 
    unames = unique(names) 
    starind = arange(0,len(names), 1) 
    name_ind = [] 
    names = array(names) 
    for each in unames:
      takeit = each == names 
      name_ind.append(np.int(starind[takeit][-1]+1. ) )
    cluster_ind = [0] + list(sort(name_ind))# + [len(al)]
    plot_markers = ['ko', 'yo', 'ro', 'bo', 'co','k*', 'y*', 'r*', 'b*', 'c*', 'ks', 'rs', 'bs', 'cs', 'rd', 'kd', 'bd', 'cd', 'mo', 'ms' ]
    #plot_markers = ['k', 'y', 'r', 'b', 'c','k', 'y', 'r', 'b', 'c', 'k', 'r', 'b', 'c', 'r', 'k', 'b', 'c', 'm', 'm' ]
    #cv_ind = np.arange(395,469,1)
    #a  = open(filein2)
    #al = a.readlines() 
    #bl = []
    #for each in al:
    #    bl.append(each.strip())
    #bl = np.delete(bl, [cv_ind], axis = 0) 
    #savetxt("starsin_cut.txt", bl, fmt = "%s") 
    #filein3 = 'starsin_cut.txt'
    t,g,feh,t_err,feh_err = loadtxt(filein2, usecols = (4,6,8,16,17), unpack =1) 
    g_err = [0]*len(g) 
    g_err = array(g_err)
    
    params = array(params) 
    covs_params = np.linalg.inv(icovs_params) 
    rcParams['figure.figsize'] = 12.0, 10.0
    fig, temp = pyplot.subplots(3,1, sharex=False, sharey=False)
    ax1 = temp[0]
    ax2 = temp[1]
    ax3 = temp[2]
    params_labels = [params[:,0], params[:,1], params[:,2] , covs_params[:,0,0]**0.5, covs_params[:,1,1]**0.5, covs_params[:,2,2]**0.5 ]  
    cval = ['k', 'b', 'r'] 
    input_ASPCAP = [t, g, feh, t_err, g_err, feh_err] 
    listit_1 = [0,1,2]
    listit_2 = [1,0,0]
    axs = [ax1,ax2,ax3]
    labels = ["ASPCAP log g", "ASPCAP Teff", "ASPCAP Teff"]
    for i in range(0,len(cluster_ind)-1): 
      indc1 = cluster_ind[i]
      indc2 = cluster_ind[i+1]
      for ax, num,num2,label1,x1,y1 in zip(axs, listit_1,listit_2,labels, [4800,3.0,0.3], [3400,1,-1.5]): 
        pick = logical_and(g[indc1:indc2] > 0, logical_and(t_err[indc1:indc2] < 300, feh[indc1:indc2] > -4.0) ) 
        cind = array(input_ASPCAP[1][indc1:indc2][pick]) 
        cind = array(input_ASPCAP[num2][indc1:indc2][pick]).flatten() 
        ax.plot(input_ASPCAP[num][indc1:indc2][pick], params_labels[num][indc1:indc2][pick], plot_markers[i]) 
        #ax.errorbar(input_ASPCAP[num][indc1:indc2][pick], params_labels[num][indc1:indc2][pick],yerr= params_labels[num+3][indc1:indc2][pick],marker='',ls='',zorder=0, fmt = None,elinewidth = 1,capsize = 0)
        #ax.errorbar(input_ASPCAP[num][indc1:indc2][pick], params_labels[num][indc1:indc2][pick],xerr=input_ASPCAP[num+3][indc1:indc2][pick],marker='',ls='',zorder=0, fmt = None,elinewidth = 1,capsize = 0)
        ax.text(x1,y1,"y-axis, $<\sigma>$ = "+str(round(mean(params_labels[num+3][pick]),2)),fontsize = 14) 

    ax1.plot([0,6000], [0,6000], linewidth = 1.5, color = 'k' ) 
    ax2.plot([0,5], [0,5], linewidth = 1.5, color = 'k' ) 
    ax3.plot([-3,2], [-3,2], linewidth = 1.5, color = 'k' ) 
    ax1.set_xlim(3500, 5500) 
    ax2.set_xlim(0, 5) 
    ax3.set_xlim(-3, 2) 
    ax1.set_xlabel("ASPCAP Teff, [K]", fontsize = 14,labelpad = 5) 
    ax1.set_ylabel("NHR+ Teff, [K]", fontsize = 14,labelpad = 5) 
    ax2.set_xlabel("ASPCAP logg, [dex]", fontsize = 14,labelpad = 5) 
    ax2.set_ylabel("NHR+ logg, [dex]", fontsize = 14,labelpad = 5) 
    ax3.set_xlabel("ASPCAP [Fe/H], [dex]", fontsize = 14,labelpad = 5) 
    ax3.set_ylabel("NHR+ [Fe/H], [dex]", fontsize = 14,labelpad = 5) 
    ax1.set_ylim(1000,6000)
    ax1.set_ylim(3000,5500)
    ax2.set_ylim(-3,6)
    ax3.set_ylim(-3,2) 
    # attach lines to plots
    fig.subplots_adjust(hspace=0.22)
    #prefix = "/Users/ness/Downloads/Apogee_Raw/calibration_apogeecontinuum/documents/plots/fits_3_self_cut"
   ## prefix = "/Users/ness/Downloads/Apogee_Raw/calibration_apogeecontinuum/documents/plots/test_self"
    #savefig(fig, prefix, transparent=False, bbox_inches='tight', pad_inches=0.5)
    return 

def savefig(fig, prefix, **kwargs):
    for suffix in (".eps", ".png"):
        print "writing %s" % (prefix + suffix)
        fig.savefig(prefix + suffix, **kwargs)

if __name__ == "__main__": #args in command line 
    wl1,wl2,wl3,wl4,wl5,wl6 = 15392, 15697, 15958.8, 16208.6, 16120.4, 16169.5 
    plotfits() 

