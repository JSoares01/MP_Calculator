from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.central_window = QWidget()
        self.vbox_layout = QVBoxLayout()

        self.central_window.setLayout(self.vbox_layout)
        self.setCentralWidget(self.central_window)
