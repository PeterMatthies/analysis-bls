# Oersted-field calculation
# origin of coordinate system middle bottom in the cross section of the Au wire

import sys, os, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtGui, QtCore, QtWidgets


class AppForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setWindowTitle('Oersted Field of a Rectangular Wire')

        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        self.textbox1.setText('0.15')  # current value (A)
        self.textbox2.setText('90e-9') # z point for which the field will be calculated
        self.textbox3.setText('3e-6')  # width of the Au wire (m)
        self.textbox4.setText('25e-9') # thickness of the Au wire (m)
        self.on_draw()
        self.current=0.15
        self.z_pos=90e-9
        self.width=3e-6
        self.thickness=25e-9

    def save_plot(self):
        file_choices = 'PNG (*.png)|*.png'

        path = str(QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', '', file_choices))

        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)

    def on_about(self):
        msg = """ A demo of using PyQt with matplotlib:
        
        * Use the matplotlib navigation bar
        * Add valuesto the text box and press Enter (or click "Draw"
        * Show or hide the grid
        * Drag the slider to modify the width of the bars
        * Save the plot to a file using the File menu
        * Click on a bar to receive an information message
        """

        QtWidgets.QMessageBox.about(self, "About the demo", msg.strip())

    def on_pick(self, event):
        # the event here is of the type
        # matplotlib.backend_bases.PickEvent
        #
        # It carries lots of information, of which we're using
        # only a small amount here.
        #
        box_points = event.artist.get_bbox().get_points()
        msg = "You've clicked on a bar with coords:\n %s" %box_points

        QtWidgets.QMessageBox.information(self, "Click!", msg)

    def on_draw(self):
        """Redraws the figure
        """
        self.current = float(self.textbox1.text())
        self.z_pos = float(self.textbox2.text())
        self.width = float(self.textbox3.text())
        self.thickness = float(self.textbox4.text())

        x = np.linspace(-0.5*self.width, 0.5*self.width, 1000)
        y = 1000*calc_field(x, self.z_pos, self.width, self.thickness, self.current)
        # clear the axes and redraw the plot anew
        #
        self.axes.clear()
        self.axes.grid(self.grid_cb.isChecked())

        self.axes.plot(x, y, 'rx')
        # self.axes.bar(
        #     left=x,
        #     height=self.data,
        #     width=self.slider.value() / 100.0,
        #     align='center',
        #     alpha=0.44,
        #     picker=5)
        self.axes.set_xlim(-0.5*self.width, 0.5*self.width)
        self.axes.set_xlabel('Position across wire (m)')
        self.axes.set_ylabel(r"$B_{in\hspace{0.2} plane}$ (mT)")
        self.axes.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
        self.axes.xaxis.major.formatter._useMathText = True
        self.canvas.draw()
        self.fig.tight_layout()

    def create_main_frame(self):
        self.main_frame = QtWidgets.QWidget()

        # Create the mpl Figure and FigCanvas objects.
        # 5x4 inches, 100 dots per inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)

        self.axes = self.fig.add_subplot(111)


        # Bind the 'pick' event for clicking on one of the bars
        #
        self.canvas.mpl_connect('pick_event', self.on_pick)

        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        # Other GUI controls
        #
        self.textbox1 = QtWidgets.QLineEdit()
        self.textbox1.setMinimumWidth(100)
        self.textbox1.editingFinished.connect(self.on_draw)

        self.textbox2 = QtWidgets.QLineEdit()
        self.textbox2.setMinimumWidth(100)
        self.textbox2.editingFinished.connect(self.on_draw)

        self.textbox3 = QtWidgets.QLineEdit()
        self.textbox3.setMinimumWidth(100)
        self.textbox3.editingFinished.connect(self.on_draw)

        self.textbox4 = QtWidgets.QLineEdit()
        self.textbox4.setMinimumWidth(100)
        self.textbox4.editingFinished.connect(self.on_draw)

        self.draw_button = QtWidgets.QPushButton("&Draw")
        # self.connect(self.draw_button, QtWidgets.PYQT_SIGNAL('clicked()'), self.on_draw)
        self.draw_button.clicked.connect(self.on_draw)

        self.grid_cb = QtWidgets.QCheckBox("Show &Grid")
        self.grid_cb.setChecked(False)
        # self.connect(self.grid_cb, QtWidgets.PYQT_SIGNAL('stateChanged(int)'), self.on_draw)
        self.grid_cb.stateChanged.connect(self.on_draw)

        # slider_label = QtWidgets.QLabel('Bar width (%):')
        # self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        # self.slider.setRange(1, 100)
        # self.slider.setValue(20)
        # self.slider.setTracking(True)
        # self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        # self.connect(self.slider, QtWidgets.PYQT_SIGNAL('valueChanged(int)'), self.on_draw)
        # self.slider.valueChanged.connect(self.on_draw)

        #
        # Layout with box sizers
        #
        hbox = QtWidgets.QHBoxLayout()

        for w in [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.draw_button, self.grid_cb]:
            hbox.addWidget(w)
            hbox.setAlignment(w, QtCore.Qt.AlignVCenter)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        vbox.addLayout(hbox)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

    def create_status_bar(self):
        self.status_text = QtWidgets.QLabel("Oersted Field calculation")
        self.statusBar().addWidget(self.status_text, 1)

    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("&File")

        load_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot, tip='Save the plot')
        quit_action = self.create_action("&Quit", slot=self.close, shortcut="Ctrl+Q", tip='Close the application')

        self.add_actions(self.file_menu,(load_file_action, None, quit_action))

        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About", shortcut="F1", slot=self.on_about, tip='About the Demo')

        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(self, text, slot=None, shortcut=None,
                      icon=None, tip=None, checkable=False, signal="triggered"):
        action = QtWidgets.QAction(text, self)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            # self.connect(action, QtWidgets.PYQT_SIGNAL(signal), slot)
            getattr(action, signal).connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()


def calc_field(x_pos, z_pos, width, height, current):
    gamma = (1.2566E-6/(4*np.pi))*current/(width*height)
    x1 = x_pos + width/2
    x2 = x_pos - width/2
    z1 = height - z_pos
    a1 = (np.power(x1, 2) + np.power(z_pos, 2)) / (np.power(x1, 2) + np.power(z1, 2))
    a2 = (np.power(x2, 2) + np.power(z_pos, 2)) / (np.power(x2, 2) + np.power(z1, 2))
    print(gamma, x1, x2, z1, a1, a2)
    return gamma * (0.5 * x1 * np.log(a1) - 0.5 * x2 * np.log(a2) +
                     z_pos * (np.arctan(x1 / z_pos) - np.arctan(x2 / z_pos)) -
                     z1 * (np.arctan(x1 / z1) - np.arctan(x2 / z1)))


# define variables
w = 3e-6  # m
thickness_min = 25e-9  # m
thickness_max = 50e-9  # m
I = 0.15  # A
z0 = 90e-9  # m middle of py stripe
mu0 = 1.2566E-6

# Calculation
print('Oersted field is (mT):', 1000*calc_field(0.0, z0, w, thickness_max, I), '50 nm Au')
print('Oersted field is (mT):', 1000*calc_field(0.0, z0, w, thickness_min, I), '25 nm Au')
#
x_points = np.linspace(-w/2, w/2, 1000)
field_middle_py1 = 1000*calc_field(x_points, z0, w, thickness_max, I)
field_middle_py2 = 1000*calc_field(x_points, z0, w, thickness_min, I)
By1 = 1000*calc_field(x_points, thickness_max, w, thickness_min, I)
By2 = 1000*calc_field(x_points, thickness_max, w, thickness_max, I)
#
#
fig1 = plt.figure()
print('Inplane Oersted in center of Py (mT):', field_middle_py1)
print('Inplane Oersted in center of Py (mT):', field_middle_py2)
ax1 = fig1.add_subplot(111)
ax1.plot(x_points, field_middle_py1, 'bo', label='middle of Py, Au 50nm thick', markersize=4)
ax1.plot(x_points, field_middle_py2, 'rx', label='middle of Py, Au 25 nm thick', markersize=4)
ax1.plot(x_points, By1, 'yo', label='surface of Au, Au 25nm thick', markersize=4)
ax1.plot(x_points, By2, 'gx', label='surface of Au, Au 50nm thick', markersize=4)
# plt.axis([(-w/2 * 1000000), (w/2 * 1000000), 0.0, 50])
ax1.ticklabel_format(axis='x', style='sci', scilimits=(-3, 3), useOffset=False)
ax1.xaxis.major.formatter._useMathText = True
ax1.grid(True)
ax1.set_xlim(-w/2, w/2)
ax1.legend(loc=8)
plt.xlabel("Position across wire (m)")
plt.ylabel(r"$B_{in\hspace{0.2} plane}$ (mT)")
#
# plt.savefig('swsd1_oersted_inplane.png', format='png', dpi=100)
plt.show()


if __name__ == "__main__":
    main()
    quit()