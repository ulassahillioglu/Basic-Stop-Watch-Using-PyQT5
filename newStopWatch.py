from PyQt5 import QtCore, QtGui, QtWidgets

class StopWatch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.elapsed = QtCore.QTime(0, 0, 0)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.start_button = QtWidgets.QPushButton('Start')
        self.start_button.clicked.connect(self.start_timer)
        self.start_button.setStyleSheet(("""background-color:
         rgba(0,255,0,155);color:rgba(25,25,25,255);
         border-style: ridge;border-width : 2px; 
         border-radius: 10px;border-color: cyan ;padding : 6px"""))
        self.start_button.adjustSize()

        self.stop_button = QtWidgets.QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setEnabled(False)
        self.stop_button.setStyleSheet(("""background-color:
         rgba(255,0,0,175);color:rgba(25,25,25,255);
         border-style: ridge;border-width : 2px; 
         border-radius: 10px;border-color: cyan ;padding : 6px"""))

        self.reset_button = QtWidgets.QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_timer)
        self.reset_button.setEnabled(False)
        self.reset_button.setStyleSheet(("""background-color:
         rgba(0,0,255,175);color:rgba(255,255,255,255);
         border-style: ridge;border-width : 2px; 
         border-radius: 10px;border-color: cyan ;padding : 6px"""))

        self.time_label = QtWidgets.QLabel('00:00:00')
        self.time_label.setFont(QtGui.QFont('Times New Roman', 30))
        self.time_label.adjustSize()

        self.setStyleSheet("""background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop: 0.4 rgba(105, 125, 145, 40),stop:1 rgba(0, 140, 140, 175));""")

        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        layout.addWidget(self.time_label, 0, 0, QtCore.Qt.AlignCenter)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)
        layout.addLayout(button_layout, 1, 0, QtCore.Qt.AlignCenter)
        self.setLayout(layout)

    def start_timer(self):
        self.timer.start(1000)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.reset_button.setEnabled(True)

    def reset_timer(self):
        self.timer.stop()
        self.elapsed = QtCore.QTime(0, 0, 0)
        self.time_label.setText('00:00:00')
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.reset_button.setEnabled(False)

    def update_time(self):
        self.elapsed = self.elapsed.addSecs(1)
        text = self.elapsed.toString('hh:mm:ss')
        self.time_label.setText(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setApplicationName("Stopwatch Application")
    stopwatch = StopWatch()
    stopwatch.show()
    app.exec_()