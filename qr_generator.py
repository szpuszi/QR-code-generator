import sys
import qrcode
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                              QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, 
                              QFileDialog, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QImage
from io import BytesIO

class ModernFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            ModernFrame {
                background-color: #ffffff;
                border-radius: 10px;
                border: 1px solid #e0e0e0;
                padding: 20px;
            }
        """)

class QRGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setMinimumSize(600, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
            QLineEdit {
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #e0e0e0;
                background-color: white;
                font-size: 14px;
            }
            QLabel {
                color: #333333;
            }
        """)
        
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        title_label = QLabel("Generator kodów QR")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        input_frame = ModernFrame()
        input_layout = QVBoxLayout(input_frame)
        
        url_label = QLabel("Wprowadź URL:")
        url_label.setFont(QFont("Arial", 12))
        input_layout.addWidget(url_label)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://example.com")
        self.url_input.textChanged.connect(self.on_text_changed)
        input_layout.addWidget(self.url_input)
        
        button_layout = QHBoxLayout()
        
        self.generate_btn = QPushButton("Generuj")
        self.generate_btn.clicked.connect(self.generate_qr)
        self.generate_btn.setEnabled(False)
        
        self.save_btn = QPushButton("Zapisz")
        self.save_btn.clicked.connect(self.save_qr)
        self.save_btn.setEnabled(False)
        
        button_layout.addWidget(self.generate_btn)
        button_layout.addWidget(self.save_btn)
        input_layout.addLayout(button_layout)
        
        main_layout.addWidget(input_frame)

        self.qr_frame = ModernFrame()
        qr_layout = QVBoxLayout(self.qr_frame)
        
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setMinimumSize(400, 400)
        qr_layout.addWidget(self.qr_label)
        
        main_layout.addWidget(self.qr_frame)
        
        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))
        main_layout.addWidget(self.status_label)

        self.qr_image = None

    def on_text_changed(self, text):
        self.generate_btn.setEnabled(bool(text.strip()))
        self.save_btn.setEnabled(False)
        self.status_label.clear()
        self.qr_label.clear()

    def generate_qr(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Błąd", "Proszę wprowadzić URL!")
            return

        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            self.qr_image = qr.make_image(fill_color="black", back_color="white")
            
            buffer = BytesIO()
            self.qr_image.save(buffer, format='PNG')
            qimage = QImage.fromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)
            
            scaled_pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            self.qr_label.setPixmap(scaled_pixmap)
            self.save_btn.setEnabled(True)
            self.status_label.setText("Kod QR został wygenerowany!")
            self.status_label.setStyleSheet("color: #4CAF50;")

        except Exception as e:
            QMessageBox.critical(self, "Błąd", f"Wystąpił błąd podczas generowania kodu QR: {str(e)}")
            self.status_label.setText("Wystąpił błąd podczas generowania kodu QR!")
            self.status_label.setStyleSheet("color: #F44336;")

    def save_qr(self):
        if not self.qr_image:
            QMessageBox.warning(self, "Błąd", "Najpierw wygeneruj kod QR!")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Zapisz kod QR",
            "qr_code.png",
            "PNG Files (*.png);;All Files (*.*)"
        )

        if file_path:
            try:
                self.qr_image.save(file_path)
                self.status_label.setText(f"Kod QR został zapisany: {file_path}")
                self.status_label.setStyleSheet("color: #4CAF50;")
            except Exception as e:
                QMessageBox.critical(self, "Błąd", f"Nie udało się zapisać pliku: {str(e)}")
                self.status_label.setText("Wystąpił błąd podczas zapisywania!")
                self.status_label.setStyleSheet("color: #F44336;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRGenerator()
    window.show()
    sys.exit(app.exec())