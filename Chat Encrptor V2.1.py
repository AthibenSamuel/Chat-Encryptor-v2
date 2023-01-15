import pyperclip
from cryptography.fernet import Fernet
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QDialog)
from PyQt6.QtCore import Qt

def encrypt(data, key):
    encryptor = Fernet(key)
    encrypted = encryptor.encrypt(bytes(data, 'utf-8'))
    return encrypted
def decrypt(encrypted_text, key):
    f = Fernet(key)
    dec = f.decrypt(encrypted_text)
    return dec.decode('utf-8')

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("Chat Encryptor v2.1")

        layout = QVBoxLayout()
        self.setLayout(layout)

        def get_key():
            key=self.input.text()
            return key

        def decode():
            text1=self.input2.text()
            key=get_key()
            normal_text = decrypt(text1.encode('utf-8'),key)
            msg=QDialog(parent=self)
            msg.setWindowTitle("Decrypted Text")
            layout.addWidget(msg,alignment=Qt.AlignmentFlag.AlignCenter)
            message=QLabel(normal_text)
            msg.layout=QVBoxLayout()
            msg.layout.addWidget(message)
            msg.setLayout(msg.layout)

        def encode():
            text1=self.input1.text()
            key=get_key()
            txt=encrypt(text1,key)
            pyperclip.copy(str(txt.decode('utf-8')))

        def clear():
            self.input.clear()
            self.input1.clear()
            self.input2.clear()
            
        def key_generator():
            key = Fernet.generate_key().decode('utf-8')
            pyperclip.copy(str(key))
            msg=QDialog(parent=self)
            msg.setWindowTitle("New Key")
            layout.addWidget(msg,alignment=Qt.AlignmentFlag.AlignCenter)
            message=QLabel(key)
            message1=QLabel("Save this key for later")
            msg.layout=QVBoxLayout()
            msg.layout.addWidget(message,alignment=Qt.AlignmentFlag.AlignCenter)
            msg.layout.addWidget(message1,alignment=Qt.AlignmentFlag.AlignCenter)
            msg.setLayout(msg.layout)


        self.label=QLabel("<h1>Enter Info</h1>", parent=self)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        

        self.input = QLineEdit()
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input.setFixedWidth(150)
        self.input1.setFixedWidth(150)
        self.input2.setFixedWidth(150)

        self.label1=QLabel("Key:-",parent=self)
        layout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
        self.label1=QLabel("Text to encode:-",parent=self)
        layout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input1, alignment= Qt.AlignmentFlag.AlignCenter)
        self.label1=QLabel("Text to decode:-",parent=self)
        layout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input2, alignment= Qt.AlignmentFlag.AlignCenter)
        
        button = QPushButton("Encode")
        button.clicked.connect(encode)
        layout.addWidget(button)
        
        button = QPushButton("Decode")
        button.clicked.connect(decode)
        layout.addWidget(button)

        button = QPushButton("Generate Key")
        button.clicked.connect(key_generator)
        layout.addWidget(button)


        button = QPushButton("Clear All")
        button.clicked.connect(clear)
        layout.addWidget(button)

        
app = QApplication([])
window = Window()
window.show()
app.exec()
