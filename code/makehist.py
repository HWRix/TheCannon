pick = logical_and(input_ASPCAP[1] > 0, logical_and(input_ASPCAP[3] < 300, input_ASPCAP[2] > -4.0) ) 
x = input_ASPCAP[2][pick]
y = params_labels[2][pick]

starsin = open('starsin_new_all_ordered.txt','r') 
al = starsin.readlines()
names = []
for each in al:
  names.append(each.split()[1]) 
unames = unique(names) 
starind = arange(0,len(names), 1) 
name_ind = [] 
name_ind2 = [] 
names = array(names) 
for each in unames:
  takeit = each == names 
  name_ind.append(starind[takeit][-1]+1. ) 
  name_ind2.append(starind[takeit][0] ) 
names = array(names) 
for each in unames:
  takeit = each == names 
  name_ind.append(starind[takeit][-1]+1. ) 
  name_ind2.append(starind[takeit][0]+1. ) 
name_ind_sort = sort(name_ind)
name_ind2_sort = sort(name_ind2)

#zip(sort(name_ind), unames[argsort(name_ind)]) 

T_est,g_est,feh_est = np.loadtxt("starsin_new_all_ordered.txt", usecols = (4,6,8), unpack =1) 
feh_clusters = [] 
g_clusters = [] 
t_clusters = [] 
name_ind2_sort1 = list(name_ind2_sort) + list([len(al)] ) 
name_ind2_sort1 = array(name_ind2_sort1) 
for i in range(len(name_ind2_sort1)-1):
  ind1 = name_ind2_sort1[i]
  ind2 = name_ind2_sort1[i+1]
  feh_clusters.append(feh_est[ind1:ind2]) 
  g_clusters.append(g_est[ind1:ind2]) 
  t_clusters.append(T_est[ind1:ind2]) 

nullfmt   = NullFormatter()         # no labels

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left+width+0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(11,11))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx,alpha = 0.4)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y, c = input_ASPCAP[0][pick], s = 30)

# now determine nice limits by hand:
binwidth = 0.25
xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
lim = ( int(xymax/binwidth) + 1) * binwidth

axScatter.set_xlim( (-lim, lim) )
axScatter.set_ylim( (-lim, lim) )
axHisty.set_ylim( (-lim, lim) )
axScatter.plot([-3,2], [-3,2],'k',linewidth = 2) 

bins = np.arange(-lim, lim + binwidth, binwidth)
bins = np.arange(-3,2,0.25) 
for each in feh_clusters:
  #axHistx.hist(each, bins=bins,alpha  = 0.5,range = (-3,1) )
  axHistx.hist(each, bins=15,alpha  = 0.5,range = (-3,1) )

axHisty.hist(y, bins=bins, orientation='horizontal')

axScatter.set_xlim(-3,2) 
axScatter.set_ylim(-3,2) 
axHisty.set_ylim(-3,2) 
axHistx.set_xlim(-3,2) 
axScatter.set_xlabel("ASPCAP [Fe/H]", fontsize = 20)
axScatter.set_ylabel("NHR+ [Fe/H]", fontsize = 20) 
axHistx.set_title("calibrators: [Fe/H]", fontsize = 20 ) 
#axHisty.set_ylabel("[Fe/H] hisogram of NHR+ [Fe/H]", fontsize = 20) 
axHisty.yaxis.set_label_position("right")
draw()
show()
savefig('/Users/ness/Downloads/Apogee_Raw/calibration_apogeecontinuum/documents/plots/cal_feh.eps', transparent=True, bbox_inches='tight', pad_inches=0)