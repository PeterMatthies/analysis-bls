import numpy as np
from os import listdir
import re
from os.path import isfile, join
import matplotlib.pyplot as plt


path_to_data = './m_data/25052017_nrcl/'
data_files = [f for f in listdir(path_to_data) if isfile(join(path_to_data, f))]
print(data_files)

# to replace a comma in float to a point
# for data_file in data_files:
#     with open(path_to_data + data_file, 'r+') as f:
#         newf = re.sub(r'(\s+[+-]?[0-9]+),([0-9]+\s+)',r'\1.\2', f.read())
#         f.seek(0)
#         f.write(newf)


fig = plt.figure()
ax1 = fig.add_subplot(111)
# # ax2 = fig.add_subplot(212)
ax1.set_xlabel('Frequency(GHz)')
ax1.set_ylabel('Intensity')
# # ax2.set_ylabel('Intensity')
#
selected_field = 'p10mT'
fig.suptitle('Freq Spectra for '+selected_field[1:])

for data_file in data_files:
    data = np.loadtxt(path_to_data + data_file, comments='#')
    print(data.shape)
    x1, y1, x2, y2 = 0, 0, 0, 0
    if selected_field in data_file:
        x_pos1 = data[:, 0]
        y_pos1 = data[:, 1]
        x_pos2 = data[:, 2]
        y_pos2 = data[:, 3]
        ax1.plot(x_pos1, y_pos1, color='blue', label = 'above antenna')
        ax1.plot(x_pos2, y_pos2, color='red', label = 'below antenna')
plt.grid()
plt.legend()
plt.show()




