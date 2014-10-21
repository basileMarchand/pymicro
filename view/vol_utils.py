import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.colors import colorConverter
import matplotlib as mpl

def show_and_save(image, name, dpi=100, colormap=cm.gray, verbose=False):
  '''Save a 2D image with pyplot.
  
  This function displays a 2D numpy array (or a slice of a 3D array)
  using pyplot and save it to the disk as a png image. The interpolation 
  is disabled and the vertical origin is set to the bottom of the image.

  *Parameters*
  
  **image**: the 2d data array to show and save.
  
  **name**: a string to use as the file name (without the extension)
  
  **dpi**: image resolution (default 100).
  
  **colormap**: the colormap tp use in matplotlib format (default gray).
  
  **verbose**: boolean to enable verbose mode (default False).
  '''
  (im_size_y, im_size_x) = image.shape
  plt.figure(figsize=(im_size_x/float(dpi), im_size_y/float(dpi)))
  if verbose:
    print('image size is', image.shape)
    print('figure size is:', np.array(image.shape)/float(dpi))
  plt.axis('off')
  plt.hold('off')
  plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
  plt.imshow(image, cmap=colormap, interpolation='nearest', origin='lower')
  plt.savefig(name + '.png', format='png')
  plt.close()

def hist(data, nb_bins=256, show=True, save=False, prefix='data', density=False):
  '''Histogram of a data array.
  
  Compute and plot the gray level histogram of the provided data array.

  .. warning::

     Works only with 8 bit data (ie numpy uint8 data type).

  *Parameters*
  
  **data**: the data array to analyse.
  
  **nb_bins**: the number of bins in the histogram.
  
  **show**: boolean to display the figure using pyplot (defalut True).

  **save**: boolean to save the figure using pyplot (defalut False).
  
  **prefix**: a string to use in the file name when saving the histogram 
  as an image (defaut 'data').
  
  **density**: a boolean to control wether the histogram is plotted 
  using the probability density function, see numpy histogram function 
  for more details (default False).
  
  .. figure:: _static/HDPE_0001-2_512x512x512_uint8_hist.png
      :width: 600 px
      :height: 400 px
      :alt: HDPE_0001-2_512x512x512_uint8_hist.png
      :align: center

      Gray level histogram computed on a 512x512x512 8 bits image.
  '''
  print 'computing gray level histogram'
  hist, bin_edges = np.histogram(data, bins=nb_bins, range=(0,255), density=density)
  bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])
  plt.figure(1, figsize=(6,4))
  if density:
    plt.bar(bin_centers, 100*hist, width=1, fill=True, color='g', edgecolor='g')
    plt.ylabel('Probability (%)')
  else:
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.bar(bin_centers, hist, width=1, fill=True, color='g', edgecolor='g')
    plt.ylabel('Counts')
  plt.xlim(0,256)
  plt.xlabel('8 bit gray level value')
  if save: plt.savefig(prefix + '_hist.png', format='png')
  if show: plt.show()

def alpha_cmap(color='red'):
  '''Creating a particular colormap with transparency.
  
  Only values equal to 255 will have a non zero alpha channel.
  This is typically used to overlay a binary result on initial data.
  '''
  color1 = colorConverter.to_rgba('white')
  color2 = colorConverter.to_rgba(color)
  mycmap = mpl.colors.LinearSegmentedColormap.from_list('my_cmap', [color1, color2], 256)
  mycmap._init()
  alphas = np.zeros(mycmap.N+3)
  alphas[255:] = 1.0 # show only values at 255
  mycmap._lut[:,-1] = alphas
  return mycmap

def format_coord(x, y):
  '''
  Modify the coordinate formatter of pyplot to display the image
  value of the nearest pixel given x and y.
  '''
  n_rows, n_cols = array.shape
  col = int(x + 0.5)
  row = int(y + 0.5)
  if col >= 0 and col < numcols and row >= 0 and row < numrows:
    z = 10#array[row, col]
    return 'x=%1.1f, y=%1.1f, z=%1.1f' % (x, y, z)
  else:
    return 'x=%1.1f, y=%1.1f' % (x, y)
