#!/usr/bin/python
import numpy
from numpy import savetxt
import matplotlib
from matplotlib import pyplot
import scipy
from scipy import interpolate
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
s = matplotlib.font_manager.FontProperties()
s.set_family('serif')
s.set_size(14)
from matplotlib import rc
rc('text', usetex=False)
rc('font', family='serif')
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib
from matplotlib import pyplot
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
s = matplotlib.font_manager.FontProperties()
s.set_family('serif')
rcParams["xtick.labelsize"] = 14
rcParams["ytick.labelsize"] = 14
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
s = matplotlib.font_manager.FontProperties()
majorLocator   = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
minorLocator   = MultipleLocator(5)
yminorLocator   = MultipleLocator(10)
yminorLocator2   = MultipleLocator(25)
xminorLocator   = MultipleLocator(5)
yminorLocator   = MultipleLocator(5)
ymajorLocator   = MultipleLocator(50)
xmajorLocator   = MultipleLocator(10)
rcParams['figure.figsize'] = 15.0, 10.0
#wl0 = 15392, 15695, 15958, 16205, 16118, 16170 
def plotdata(wl0, bw): 
  fig, temp = pyplot.subplots(3,1, sharex=True, sharey=False)
  ax1 = temp[0]
  ax2 = temp[1]
  ax3 = temp[2]
  #covs_mean = 1/invcovs[:,:,0]
  #covs_mean1 = covs_mean[:,0]**0.5
  #covs_t = 1/invcovs[:,:,1]
  #covs_t1 = covs_t[:,1]**0.5
  #covs_g = 1/invcovs[:,:,2]
  #covs_g1 = covs_g[:,2]**0.5
  #covs_feh = 1/invcovs[:,:,3]
  #covs_feh1 = covs_feh[:,0]**0.5
  axlist = [ax1,ax2,ax3]
  ax1.plot(dataall[:, 0, 0], 1. * chisqs,color = 'black' ,linewidth = 2) # feh  
  ax2.plot(dataall[:, 0, 0], 1. * coeffs[:, 0],color = 'k' ,linewidth = 2) # median
  ax3.plot(dataall[:, 0, 0], 1. * coeffs[:, 3], color = 'red',linewidth = 2,label  = '[Fe/H] ' ) # feh  
  ax3.fill_between(dataall[:,0,0], coeffs[:,3] +covs_feh1, coeffs[:,3]  - covs_feh1, alpha = 0.2, color = 'grey')
  ax3.plot(dataall[:, 0, 0], 1. * coeffs[:, 2], color = 'blue',linewidth = 2, label = 'logg') #  g 
  ax3.plot(dataall[:, 0, 0], 1000. * coeffs[:, 1], color = 'green',linewidth = 2,label = 'Teff') # teff 
  legend()
  ax1.vlines(wl0, -11,20000000, linestyle = 'dashed', linewidth = 2) 
  ax2.vlines(wl0, -1,2, linestyle = 'dashed', linewidth = 2) 
  ax3.vlines(wl0, -1,2, linestyle = 'dashed', linewidth = 2) 
  for each in axlist:
    each.set_xlim(wl0 - bw/2, wl0 + bw/2 ) 
  ax1.set_ylim(np.array([0.01, 10.]) * 5. * median(chisqs)) 
  ax2.set_ylim(0.7,1.2) 
  ax3.set_ylim(np.array([0.01, 1.]) * 5. * median(coeffs[:,2])) 
  
  ax1.text(wl0-bw/2.+2, median(chisqs)*2.0, "chi2  coeff" , fontsize = 12) 
  ax2.text(wl0-bw/2.+2, median(coeffs[:,0])*2.0, "median spectra" , fontsize = 12) 
  ax3.text(wl0-bw/2+2., median(coeffs[:,2])*2.0, "[Fe/H]  coeff, log g coeff, Teff coeff*1000" , fontsize = 12) 
  ax1.set_title("REGION 1 USED FOR [Fe/H] INDEX") 
  for each in axlist:
    each.plot([wl0-bw/2.,wl0-bw/2.], [0,0],'k--') 
    each.axvspan(wl0-2.5, wl0-2.5, facecolor='c', alpha=0.1)
  ax2.plot([wl0-bw/2., wl0+bw/2.],[1,1], 'k--') 
  line_kwargs = {"color": "k", "alpha": 0.25}
  for each in axlist:
    each.axvline(15391.9, **line_kwargs)
    each.axhline(0., **line_kwargs)
    each.axvspan(l1a, l2a, facecolor='c', alpha=0.1)
  ax2.axhline(1., **line_kwargs)
  ax3.axhline(shape(dataall)[1], **line_kwargs)

  ax3.set_xlabel("Wavelength $\AA$", fontsize = 20) 
  ax1.set_ylabel("chi2", fontsize = 20) 
  ax2.set_ylabel("coeff a0", fontsize = 20) 
  ax3.set_ylabel("coeff a1,a2,a3", fontsize = 20) 
  #ax1.semilogy()

  fig.subplots_adjust(hspace=0)
  fig.subplots_adjust(wspace=0)
  return 
