import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('test_resize/20201107122805838.png')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((165.53086419753012 ,  282.66666384), 316.8395061728382, 356.44444087999995, linewidth=1, edgecolor='r', facecolor='none')
   
# Add the patch to the Axes
ax.add_patch(rect)

plt.show()
