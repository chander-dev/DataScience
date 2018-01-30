#http://www.astroml.org/book_figures/chapter3/fig_conditional_probability.html
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, NullLocator, MultipleLocator
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)
plt.ion()


x = np.linspace(-0.5,1.5,200)
y=x
H=[]
for i in y:
    t=[]
    for j in x:
        if(i>=0 and i<=1 and j>=0 and j<=1):
            t.append(i+j)
        else:
            t.append(0)
    H.append(t)
H=np.asarray(H)



fig = plt.figure(figsize=(5, 2.5))

# define axes
ax_Pxy = plt.axes((0.2, 0.34, 0.27, 0.52))
ax_Px = plt.axes((0.2, 0.14, 0.27, 0.2))
ax_Py = plt.axes((0.1, 0.34, 0.1, 0.52))
ax_cb = plt.axes((0.48, 0.34, 0.01, 0.52))
ax_Px_y = [plt.axes((0.65, 0.62, 0.32, 0.23)),plt.axes((0.65, 0.38, 0.32, 0.23))]

# draw the joint probability

# ax_Px_y[0].xaxis.set_major_formatter(NullFormatter())
# ax_Px_y[1].xaxis.set_major_formatter(NullFormatter())

ax_Pxy.xaxis.set_major_formatter(NullFormatter())
ax_Pxy.yaxis.set_major_formatter(NullFormatter())

# ax_Px.yaxis.set_major_formatter(NullFormatter())
# ax_Py.xaxis.set_major_formatter(NullFormatter())
plt.axes(ax_Pxy)
plt.imshow(H*255.0, interpolation='nearest', origin='lower', aspect='auto',
           cmap=plt.cm.binary)

cb = plt.colorbar(cax=ax_cb)
cb.set_label('p(x, y)')
plt.text(0, 1.02, '10e-3', transform=ax_cb.transAxes)

# draw p(x) distribution
ax_Px.plot(x, H.sum(0), '-r', drawstyle='steps')

# draw p(y) distribution
ax_Py.plot(H.sum(1), y, '-k', drawstyle='steps')

# label axes
ax_Pxy.set_xlabel('x')
ax_Pxy.set_ylabel('y')
ax_Px.set_xlabel('x')
ax_Px.set_ylabel('p(x)')
ax_Px.yaxis.set_label_position('right')
ax_Py.set_ylabel('y')
ax_Py.set_xlabel('p(y)')
ax_Py.xaxis.set_label_position('top')


# draw marginal probabilities
iy = [0.2, 0.4]
colors = 'rgc'
axis = ax_Pxy.axis()
for i in range(len(iy)):
    # overplot range on joint probability
    ax_Pxy.plot([0, 2, 2, 0],
                [iy[i], iy[i],
                 iy[i], iy[i]], c=colors[i], lw=1)
    Px_y = H[int((iy[i] + 0.5)*1e2)] / H[int((iy[i]+0.5)*1e2)].sum()
    ax_Px_y[i].plot(x, Px_y, drawstyle='steps', c=colors[i])
    ax_Px_y[i].yaxis.set_major_formatter(NullFormatter())
    ax_Px_y[i].set_ylabel('p(x | %.1f)' % iy[i])
ax_Pxy.axis(axis)

ax_Px_y[1].set_xlabel('x')

ax_Pxy.set_title('Joint Probability')
ax_Px_y[0].set_title('Conditional Probability')

plt.show()