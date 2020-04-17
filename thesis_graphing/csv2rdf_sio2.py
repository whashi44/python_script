import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FormatStrFormatter

# Read the csv and store them in the data frame
df = pd.read_csv("sio2.csv")
df2 = pd.read_csv("sio2_herzbach.csv")

# Graph box line width
plt.rcParams['axes.linewidth'] = 1
# Attempt to change the font to bold or normal
#plt.rcParams['font.weight'] = 'normal'

# did not set up the latex yet
# plt.rcParams['text.usetex'] = True

# Change the font to something else
# plt.rcParams['font.family'] = "sans"
# plt.rcParams['font.sans-serif']="Comi Sans MS"

# Attempt to change the font to bold for the tick label but somehow not reflective
# plt.rcParams['axes.titleweight'] = 'bold'
# plt.rcParams['axes.labelweight'] = 'bold'

# Subplot,
fig,ax = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(6,4), dpi=100)

# Plot the each r vs. g(r) for
col = 'Si-O'
col_ni = ['r',]
ax.plot(df['r'],df[col],'k-',label='This Work')
ax.plot(df2[col_ni],df2[col],'k--',label='Herzbach 2005')

# for item, col, col_ni in zip(ax, col_list, col_list_ni_r):
#     item.plot(df['r'],df[col],'k-',label='This Work')
#     item.plot(df2[col_ni],df2[col],'k--',label='Herzbach 2005')


# ax[0].tick_params(axis='both',direction='out')
ax.tick_params(axis='both', which='major', length=6)
ax.tick_params(axis='both', which='minor', length=2)
ax.tick_params(axis='x', which='both', direction='in')
ax.legend(title=col,)
# ax.legend(prop={'weight':'normal'}, title= fr'{title}').get_frame().set_edgecolor('k')
ax.legend(prop={'weight':'normal'}, title= fr'{col}' ,frameon=False)

# for item, val,val2 in zip(ax,major_tick,minor_tick):
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    # item.yaxis.set_major_formatter(FormatStrFormatter('%d'))


ax.set_xlim([3, 6])
ax.set_ylim([0,3])
# ax[1].set_ylim([0,3.5])
# ax[2].set_ylim([0,1.5])
# ax[2].set_xlabel(r'$\bf{r(}$Å$\bf{)}$',fontweight='normal')
ax.set_xlabel(r'r(Å)',fontweight='normal')
ax.set_ylabel(r'g$_{ij}$(r)',fontweight='normal')
# ax[1].set_ylabel('g(r)',fontweight='bold')

# For common y axis title
# fig.add_subplot(111, frameon=False)
# plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
# plt.ylabel(r'g$_{ij}$(r)',fontweight='normal')

# ax[0].xticks(fontweight = 'bold')

# fig.tight_layout(pad=0.1)




plt.show()


# fig.set_size_inches(4,4)
fig.savefig('sio2.png')
# plt.rcParams.keys()
# plt.subplots.keys()
