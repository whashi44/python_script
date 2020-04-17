import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FormatStrFormatter

# Read the csv and store them in the data frame
df = pd.read_csv("nano3.csv")
df2 = pd.read_csv("nano3_ni2019.csv")

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
fig,ax = plt.subplots(nrows=3, ncols=1, sharex=True, figsize=(4,6), dpi=100)

# Plot the each r vs. g(r) for
col_list = ['Na-Na','Na-N','N-N']
col_list_ni_r = ['r','r.1','r.2']
for item, col, col_ni in zip(ax, col_list, col_list_ni_r):
    item.plot(df['r'],df[col],'k-',label='This Work')
    item.plot(df2[col_ni],df2[col],'k--',label='Ni 2019')


# ax[0].tick_params(axis='both',direction='out')
legend_titles = ['Na-Na','Na-N','N-N']
for item,title in zip(ax, legend_titles):
    item.tick_params(axis='both', which='major', length=6)
    item.tick_params(axis='both', which='minor', length=2)
    item.tick_params(axis='x', which='both', direction='in')
    item.legend(title=title,)
    # item.legend(prop={'weight':'normal'}, title= fr'{title}').get_frame().set_edgecolor('k')
    item.legend(prop={'weight':'normal'}, title= fr'{title}' ,frameon=False)

major_tick = [0.5,1.0,0.5]
minor_tick = [0.25, 0.5, 0.25]
for item, val,val2 in zip(ax,major_tick,minor_tick):
    item.xaxis.set_major_locator(MultipleLocator(2))
    item.yaxis.set_major_locator(MultipleLocator(val))
    item.xaxis.set_minor_locator(MultipleLocator(1))
    item.yaxis.set_minor_locator(MultipleLocator(val2))
    # item.yaxis.set_major_formatter(FormatStrFormatter('%d'))


ax[0].set_xlim([0,16])
ax[0].set_ylim([0,1.6])
ax[1].set_ylim([0,3.5])
ax[2].set_ylim([0,1.5])
# ax[2].set_xlabel(r'$\bf{r(}$Å$\bf{)}$',fontweight='normal')
ax[2].set_xlabel(r'r(Å)',fontweight='normal')
# ax[1].set_ylabel('g(r)',fontweight='bold')

# For common y axis title
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.ylabel(r'g$_{ij}$(r)',fontweight='normal')

# ax[0].xticks(fontweight = 'bold')

fig.tight_layout(pad=0.1)




plt.show()


# fig.set_size_inches(4,4)
fig.savefig('nano3.png')
# plt.rcParams.keys()
# plt.subplots.keys()
