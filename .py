from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox

import stylesheet_rc
from ui_mainwindow import Ui_MainWindow
from stylesheeteditor import StyleSheetEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.nameLabel.setProperty('class', 'mandatory QLabel')
        self.styleSheetEditor = StyleSheetEditor(self)
        self.statusBar().addWidget(QLabel("Ready"))
        self.ui.exitAction.triggered.connect(QApplication.instance().quit)
        self.ui.aboutQtAction.triggered.connect(QApplication.instance().aboutQt)

    def on_editStyleAction_triggered(self):
        self.styleSheetEditor.show()
        self.styleSheetEditor.activateWindow()

    def on_aboutAction_triggered(self):
        QMessageBox.about(self, "About Style sheet", "The <b>Style Sheet</b> example shows how widgets can be " "styled using " "<a href=\"http://doc.qt.digia.com/4.5/stylesheet.html\">Qt " "Style Sheets</a>. Click <b>File|Edit Style Sheet</b> to pop " "up the style editor, and either choose an existing style " "sheet or design your own.")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
