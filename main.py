from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QPlainTextEdit, QWidget, QRadioButton, QShortcut, QSlider, QLabel
from PyQt5.QtCore import QPropertyAnimation, QPoint, QParallelAnimationGroup, Qt, QEvent, QTimer
from PyQt5.QtGui import QCursor, QKeySequence, QPixmap, QIcon
import webbrowser
import resources


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Scrambler Encryption")
        self.setFixedSize(1000, 700)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/icons/logo.png"), QIcon.Selected, QIcon.On)
        self.setWindowIcon(self.icon)
        self.copytoken = QApplication.clipboard()

        WindowStyle = """
            background-color: #0c0c0c
        """
        self.shortcut = QShortcut(QKeySequence('t'), self)

        self.shortcut.activated.connect(self.Encryption)

        self.setStyleSheet(WindowStyle)

        self.YourPUBLICKeyText = "Your PUBLIC Key:"
        self.YourSECRETKeyText = "Your SECRET Key:"
        self.Couldnencrypt = "Couldn't encrypt :("
        self.Couldndecipher = "Couldn't decrypt, check if you wrote down the tokens correctly"
        self.YourTextEn = "Your text"

        self.QPlainTextEditStyle = """
            QPlainTextEdit {
                color: #D3D3D8;
                font-size: 15px;
                border: 1px solid #1c1c1c;
                padding: 10px;
                background: #0c0c0c;
            }
            QPlainTextEdit::hover {
                border: 1px solid #2F2F32;
            }
        """
        self.input_encrypt = QPlainTextEdit(self)  # Field
        self.input_encrypt.setPlaceholderText("Enter the text to encrypt")
        self.input_encrypt.setGeometry(50, 100, 350, 400)
        self.input_encrypt.setStyleSheet(self.QPlainTextEditStyle)

        self.input_encrypt2 = QPlainTextEdit(self)
        self.input_encrypt2.setPlaceholderText("Your text")
        self.input_encrypt2.setGeometry(600, 100, 350, 400)
        self.input_encrypt2.setStyleSheet(self.QPlainTextEditStyle)
        self.input_encrypt2.viewport().setCursor(QCursor(Qt.ForbiddenCursor))
        self.input_encrypt2.setReadOnly(True)

        EncryptionButton = """
            QPushButton {
                color: #fff;
                background-color: #0c0c0c;
                font-size: 20px;
                border-radius: 10;
                border: 1px solid #fff;
            }
            QPushButton::hover {
                background-color: #2F2F32
            }
            QPushButton::pressed {
                background-color: #0c0c0c
            }
        """

        self.EncryptionButton = QPushButton("➜", self)
        self.EncryptionButton.setStyleSheet(EncryptionButton)
        self.EncryptionButton.setGeometry(480, 290, 50, 50)
        self.EncryptionButton.setToolTip("Encrypt")
        self.EncryptionButton.clicked.connect(self.Encryption)

        self.ButtonStyleThree = """
            QPushButton {
                color: #fff;
                background-color: #0c0c0c;
                font-size: 15px;
                border-radius: 10;
                border: 1px solid #fff;
            }
            QPushButton::hover {
                background-color: #2F2F32
            }
            QPushButton::pressed {
                background-color: #0c0c0c
            }
        """

        self.ButtonCopyTokenStyle = """
            QPushButton {
                color: #fff;
                background-color: #0c0c0c;
                font-size: 15px;
                border-radius: 10;
                border: 1px solid #fff;
            }
            QPushButton::hover {
                background-color: #2F2F32
            }
            QPushButton::pressed {
                background-color: #0c0c0c
            }
        """

        self.CopyTextButton = QPushButton("Copy Text", self)
        self.CopyTextButton.setStyleSheet(self.ButtonStyleThree)
        self.CopyTextButton.setGeometry(50, 530, 100, 50)
        self.CopyTextButton.clicked.connect(self.CopyText)

        self.PasteTextButton = QPushButton("Paste Text", self)
        self.PasteTextButton.setStyleSheet(self.ButtonStyleThree)
        self.PasteTextButton.setGeometry(300, 530, 100, 50)
        self.PasteTextButton.clicked.connect(self.PasteText)

        self.ClearTextButton = QPushButton("Clear Text", self)
        self.ClearTextButton.setStyleSheet(self.ButtonStyleThree)
        self.ClearTextButton.setGeometry(175, 530, 100, 50)
        self.ClearTextButton.clicked.connect(self.ClearText)

        self.CopyPublicTokenButton = QPushButton("Copy PUBLIC\nToken", self)
        self.CopyPublicTokenButton.setStyleSheet(self.ButtonCopyTokenStyle)
        self.CopyPublicTokenButton.setGeometry(650, 530, 110, 50)
        self.CopyPublicTokenButton.clicked.connect(self.CopyPublicToken)

        self.CopySecretTokenButton = QPushButton("Copy SECRET\nToken", self)
        self.CopySecretTokenButton.setStyleSheet(self.ButtonCopyTokenStyle)
        self.CopySecretTokenButton.setGeometry(800, 530, 110, 50)
        self.CopySecretTokenButton.clicked.connect(self.CopySecretToken)

        self.OpenPanelButton = QPushButton("≡", self)
        self.OpenPanelButton.setStyleSheet(self.ButtonStyleThree)
        self.OpenPanelButton.setGeometry(890, 20, 60, 40)
        self.OpenPanelButton.setToolTip("Open Panel")
        self.OpenPanelButton.clicked.connect(self.PanelOpen)

        WidgetStyle = """
            QWidget {
                background-color: #242424
            }
        """

        self.InfoButtonStyle = """
            QPushButton {
                color: #C2C2C2;
                font-size: 30px;
                background-color: #242424;
                border: none;
            }
            QPushButton::hover {
                color: #fff;
                font-size: 31px;
            }
        """

        self.NotificationCopyTextStyle = """
            QLabel {
                background-color: #202020;
                border-radius: 10px;
                color: grey;
                font-size: 15px;
            }
            QLabel::hover {
                color: silver;
                background-color: #262626;
            }
        """

        self.WidgetPanel = QWidget(self)  # Panel
        self.WidgetPanel.setStyleSheet(WidgetStyle)
        self.WidgetPanel.setGeometry(1000, 0, 300, 700)

        self._NotificationCopyText = QLabel("Copied", self)  # Panel
        self._NotificationCopyText.setStyleSheet(self.NotificationCopyTextStyle)
        self._NotificationCopyText.setGeometry(450, -200, 100, 50)
        self._NotificationCopyText.setAlignment(Qt.AlignCenter)


        self.CloseButton = QPushButton("✕", self)
        self.CloseButton.setStyleSheet(EncryptionButton)
        self.CloseButton.setGeometry(1200, 20, 30, 30)
        self.CloseButton.clicked.connect(self.PanelClose)

        self.InfoButton = QPushButton("🛈", self)
        self.InfoButton.setStyleSheet(self.InfoButtonStyle)
        self.InfoButton.setGeometry(1300, 19, 30, 30)
        self.InfoButton.setToolTip("Help")
        self.InfoButton.clicked.connect(self.InfoWindows)

        self.DecryptionButton = QPushButton("Decoding", self)
        self.DecryptionButton.setStyleSheet(self.ButtonStyleThree)
        self.DecryptionButton.setGeometry(1000, 600, 200, 50)
        self.DecryptionButton.clicked.connect(self.DecryptionWindows)

        self.TelegramButtonStyle = """
            QPushButton {
                color: #fff;
                background-color: #208FFF;
                font-size: 18px;
                border-radius: 5px;
            }

            QPushButton::hover {
                background-color: #46A0FC;
                font-size: 19px;
            }

            QPushButton::pressed {
                background-color: #208FFF
            }
        """

        self.GitHubButtonStyle = """
            QPushButton {
                color: #fff;
                background-color: #080B0F;
                font-size: 16px;
                font: bold;
                border-radius: 5px;
            }

            QPushButton::hover {
                background-color: #12151A;
                font-size: 17px;
            }

            QPushButton::pressed {
                background-color: #080B0F
            }
        """
        self.TelegramButton = QPushButton("Telegram", self)
        self.TelegramButton.setStyleSheet(self.TelegramButtonStyle)
        self.TelegramButton.setGeometry(1200, 100, 200, 30)
        self.TelegramButton.clicked.connect(self.openTelegramWebBrowser)

        self.GitHubButton = QPushButton("GitHub", self)
        self.GitHubButton.setStyleSheet(self.GitHubButtonStyle)
        self.GitHubButton.setGeometry(1200, 150, 200, 30)
        self.GitHubButton.clicked.connect(self.openGitHubWebBrowser)

        self.ChooseButtonStyle = """
            QRadioButton {
                color: #B4AEAE;
                background-color: none;
                font-size: 16px;
            }
            QRadioButton::hover {
                color: #fff;
            }
            QRadioButton::pressed {
                color: #B4AEAE;
            }
        """
        self.CheckColorTextStyle = """
            QCheckBox {
                color: #B4AEAE;
                background-color: none;
                font-size: 16px;
            }
            QCheckBox::hover {
                color: #fff;
            }
            QCheckBox::pressed {
                color: #B4AEAE;
            }
        """

        self.DescriptionCheckStyle = """
            QLabel {
                color: grey;
                font-size: 16px;
                font: bold;
                background-color: none;
            }
        """

        self.DescriptionChoose = QLabel("Interface language", self)
        self.DescriptionChoose.setStyleSheet(self.DescriptionCheckStyle)
        self.DescriptionChoose.setGeometry(1200, 480, 200, 30)

        self.ChooseButton = QRadioButton("English", self)
        self.ChooseButton.setStyleSheet(self.ChooseButtonStyle)
        self.ChooseButton.setGeometry(1220, 515, 100, 20)
        self.ChooseButton.nextCheckState()
        self.ChooseButton.clicked.connect(self.UpdateLanguageInterfaceEnglish)

        self.ChooseButton2 = QRadioButton("Русский", self)
        self.ChooseButton2.setStyleSheet(self.ChooseButtonStyle)
        self.ChooseButton2.setGeometry(1220, 550, 100, 20)
        self.ChooseButton2.clicked.connect(self.UpdateLanguageInterfaceRussia)

        self.anim_group = QParallelAnimationGroup()  # Objects animations | All object animations Panel in one groups
        self.AnimationPanel = QPropertyAnimation(self.WidgetPanel, b"pos")  # Animations Panle
        self.AdnimationClose = QPropertyAnimation(self.CloseButton, b"pos")  # Animations Close Button
        self.AdnimationDecoding = QPropertyAnimation(self.DecryptionButton, b"pos")  # Animation Decoding Button
        self.AdnimationChooseEnglish = QPropertyAnimation(self.ChooseButton, b"pos")
        self.AdnimationChooseRussia = QPropertyAnimation(self.ChooseButton2, b"pos")
        self.AdnimationTelegramButton = QPropertyAnimation(self.TelegramButton, b"pos")
        self.AdnimationGitHubButton = QPropertyAnimation(self.GitHubButton, b"pos")
        self.AdnimationInfoButton = QPropertyAnimation(self.InfoButton, b"pos")
        self.DescriptionChooseLabel = QPropertyAnimation(self.DescriptionChoose, b"pos")

        self.PanelNotificationCopyText = QPropertyAnimation(self._NotificationCopyText, b"pos")

        self.timer = QTimer(self)

    def openTelegramWebBrowser(self):
        webbrowser.open('https://t.me/ProgramsCreator/')

    def openGitHubWebBrowser(self):
        webbrowser.open('https://github.com/Shedrjoinzz')

    def NotificationCopyText(self):
        self.timer.timeout.connect(self.startTimer)
        self.timer.start(1000)

        self.PanelNotificationCopyText.setEndValue(QPoint(450, 10))  # Geometry Animation
        self.PanelNotificationCopyText.setDuration(400)

        self.anim_group.addAnimation(self.PanelNotificationCopyText)
        self.anim_group.start()

    def startTimer(self):
        self.timer.stop()

        self.PanelNotificationCopyText.setEndValue(QPoint(450, -200))  # Geometry Animation
        self.PanelNotificationCopyText.setDuration(400)

        self.anim_group.addAnimation(self.PanelNotificationCopyText)
        self.anim_group.start()


    def PanelOpen(self):
        self.AnimationPanel.setEndValue(QPoint(700, 0))  # Geometry Animation
        self.AnimationPanel.setDuration(200)
        self.AdnimationClose.setEndValue(QPoint(720, 20))
        self.AdnimationClose.setDuration(200)
        self.AdnimationDecoding.setEndValue(QPoint(750, 600))
        self.AdnimationDecoding.setDuration(200)
        self.AdnimationChooseEnglish.setEndValue(QPoint(750, 515))  # Geometry Animation
        self.AdnimationChooseEnglish.setDuration(200)
        self.AdnimationChooseRussia.setEndValue(QPoint(750, 550))  # Geometry Animation
        self.AdnimationChooseRussia.setDuration(200)
        self.AdnimationTelegramButton.setEndValue(QPoint(750, 100))
        self.AdnimationTelegramButton.setDuration(200)
        self.AdnimationGitHubButton.setEndValue(QPoint(750, 150))
        self.AdnimationGitHubButton.setDuration(200)
        self.AdnimationInfoButton.setEndValue(QPoint(920, 19))
        self.AdnimationInfoButton.setDuration(200)
        self.DescriptionChooseLabel.setEndValue(QPoint(730, 480))
        self.DescriptionChooseLabel.setDuration(200)

        self.input_encrypt.setEnabled(False)  # Enabled Objects (False)
        self.input_encrypt2.setEnabled(False)
        self.OpenPanelButton.setEnabled(False)
        self.CopyTextButton.setEnabled(False)
        self.PasteTextButton.setEnabled(False)
        self.EncryptionButton.setEnabled(False)
        self.ClearTextButton.setEnabled(False)

        self.anim_group.addAnimation(self.AnimationPanel)  # Groups objects for animations
        self.anim_group.addAnimation(self.AdnimationClose)
        self.anim_group.addAnimation(self.AdnimationDecoding)
        self.anim_group.addAnimation(self.AdnimationChooseEnglish)
        self.anim_group.addAnimation(self.AdnimationChooseRussia)
        self.anim_group.addAnimation(self.AdnimationTelegramButton)
        self.anim_group.addAnimation(self.AdnimationGitHubButton)
        self.anim_group.addAnimation(self.AdnimationInfoButton)
        self.anim_group.addAnimation(self.DescriptionChooseLabel)
        self.anim_group.start()  # Start Animations

    def PanelClose(self):
        self.AnimationPanel.setEndValue(QPoint(1000, 0))  # Geometry Animation
        self.AnimationPanel.setDuration(200)
        self.AdnimationClose.setEndValue(QPoint(1200, 20))
        self.AdnimationClose.setDuration(200)
        self.AdnimationDecoding.setEndValue(QPoint(1200, 600))
        self.AdnimationDecoding.setDuration(200)
        self.AdnimationChooseEnglish.setEndValue(QPoint(1220, 515))  # Geometry Animation
        self.AdnimationChooseEnglish.setDuration(200)
        self.AdnimationChooseRussia.setEndValue(QPoint(1220, 550))  # Geometry Animation
        self.AdnimationChooseRussia.setDuration(200)
        self.AdnimationTelegramButton.setEndValue(QPoint(1200, 100))
        self.AdnimationTelegramButton.setDuration(200)
        self.AdnimationGitHubButton.setEndValue(QPoint(1200, 150))
        self.AdnimationGitHubButton.setDuration(200)
        self.AdnimationInfoButton.setEndValue(QPoint(1350, 19))
        self.AdnimationInfoButton.setDuration(200)
        self.DescriptionChooseLabel.setEndValue(QPoint(1200, 480))
        self.DescriptionChooseLabel.setDuration(200)

        self.input_encrypt.setEnabled(True)  # Enabled Objects (True)
        self.input_encrypt2.setEnabled(True)
        self.OpenPanelButton.setEnabled(True)
        self.CopyTextButton.setEnabled(True)
        self.PasteTextButton.setEnabled(True)
        self.EncryptionButton.setEnabled(True)
        self.ClearTextButton.setEnabled(True)

        self.anim_group.addAnimation(self.AnimationPanel)  # Groups objects for animations
        self.anim_group.addAnimation(self.AdnimationClose)
        self.anim_group.addAnimation(self.AdnimationDecoding)
        self.anim_group.addAnimation(self.AdnimationChooseEnglish)
        self.anim_group.addAnimation(self.AdnimationChooseRussia)
        self.anim_group.addAnimation(self.AdnimationTelegramButton)
        self.anim_group.addAnimation(self.AdnimationGitHubButton)
        self.anim_group.addAnimation(self.AdnimationInfoButton)
        self.anim_group.addAnimation(self.DescriptionChooseLabel)
        self.anim_group.start()  # Start Animations

    def Encryption(self):  # Encryption
        text = self.input_encrypt.toPlainText()
        if text != "":
            from cryptography.fernet import Fernet
            try:
                key = Fernet.generate_key()
                f = Fernet(key)
                detoken = f.encrypt(bytes(text, encoding='utf-8'))
                detokenText = detoken
                self.input_encrypt2.setPlainText(f"{self.YourPUBLICKeyText}\n\n" + str(detokenText)[2:][:-1] + f"\n\n{self.YourSECRETKeyText}\n\n" + str(key)[2:][:-1])
                self.PublicToken = str(detokenText)[2:][:-1]
                self.SecretToken = str(key)[2:][:-1]
            except:
                self.input_encrypt2.setPlainText(f"{self.Couldnencrypt}")
        else:
            pass

    def DecryptionWindows(self):
        self.ActiveWindow = False
        self.window = DecryptionWindow()
        if self.ActiveWindow == False:
            self.PanelClose()
            self.ActiveWindow = True
            self.window.setFixedSize(1000, 700)
            self.window.show()
        else:
            self.window.hide()

    def CopyPublicToken(self):
        try:
            if self.copytoken != None:
                self.copytoken.setText(self.PublicToken)
                self.NotificationCopyText()
        except:
            pass

    def CopySecretToken(self):
        try:
            if self.copytoken != None:
                self.copytoken.setText(self.SecretToken)
                self.NotificationCopyText()
        except:
            pass

    def CopyText(self):
        if self.copytoken != None and self.input_encrypt.toPlainText() != "":
            self.copytoken.setText(self.input_encrypt.toPlainText())
            self.NotificationCopyText()

    def PasteText(self):
        if self.copytoken != None:
            self.input_encrypt.setPlainText(self.copytoken.text())

    def ClearText(self):
        self.input_encrypt.setPlainText("")

    def UpdateLanguageInterfaceRussia(self):
        self.input_encrypt.setPlaceholderText("Введите текст для шифрования")
        self.input_encrypt2.setPlaceholderText("Ваш текст")
        self.CopyTextButton.setText("Копировать\nтекст")
        self.CopyTextButton.setGeometry(50, 530, 110, 50)
        self.PasteTextButton.setText("Вставить\nтекст")
        self.PasteTextButton.setGeometry(300, 530, 110, 50)
        self.CopyPublicTokenButton.setText("Коп.ПУБЛИЧНЫЙ\nТокен")
        self.CopyPublicTokenButton.setGeometry(640, 530, 130, 50)
        self.CopySecretTokenButton.setText("Коп.СЕКРЕТНЫЙ\nТокен")
        self.EncryptionButton.setToolTip("Зашифровать Текст")
        self.InfoButton.setToolTip("Помощь")
        self.OpenPanelButton.setToolTip("Открыть Панель")
        self.CopySecretTokenButton.setGeometry(790, 530, 130, 50)
        self.DescriptionChoose.setText("Язык интерфейса")
        self.ClearTextButton.setText("Очистить\nтекст")
        self.ClearTextButton.setGeometry(180, 530, 100, 50)
        self.DecryptionButton.setText("Расшифровка")
        self.YourPUBLICKeyText = "Ваш ПУБЛИЧНЫЙ Токен:"
        self.YourSECRETKeyText = "Ваш СЕКРЕТНЫЙ Токен:"
        self.Couldnencrypt = "Не удалось зашифровать"

    def UpdateLanguageInterfaceEnglish(self):
        self.input_encrypt.setPlaceholderText("Enter the encryption text")
        self.input_encrypt2.setPlaceholderText("Your text")
        self.CopyTextButton.setText("Copy text")
        self.CopyTextButton.setGeometry(50, 530, 110, 50)
        self.PasteTextButton.setText("Paste text")
        self.PasteTextButton.setGeometry(300, 530, 110, 50)
        self.CopyPublicTokenButton.setText("Copy PUBLIC\nToken")
        self.CopyPublicTokenButton.setGeometry(640, 530, 110, 50)
        self.CopySecretTokenButton.setText("Copy SECRET\nToken")
        self.EncryptionButton.setToolTip("Encrypt")
        self.DescriptionChoose.setText("Interface language")
        self.OpenPanelButton.setToolTip("Open Panel")
        self.CopySecretTokenButton.setGeometry(800, 530, 110, 50)
        self.ClearTextButton.setText("Clear text")
        self.ClearTextButton.setGeometry(180, 530, 100, 50)
        self.DecryptionButton.setText("Decoding")
        self.YourPUBLICKeyText = "Your PUBLIC Token:"
        self.YourSECRETKeyText = "Your SECRET Token:"
        self.Couldnencrypt = "Failed to encrypt"


    def InfoWindows(self):
        self.ActiveInfoWindow = False
        self.info_win = InfoWindow()
        if self.ActiveInfoWindow == False:
            self.PanelClose()
            self.ActiveInfoWindow = True
            self.info_win.setFixedSize(1000, 700)
            self.info_win.show()
        else:
            self.info_win.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.PanelOpen()
        elif event.key() != Qt.Key_Escape or event.key() == Qt.Key_Escape:
            self.PanelClose()




class DecryptionWindow(Window):
    def __init__(self):
        super(DecryptionWindow, self).__init__()
        self.setWindowTitle("Scrambler Decryption")

        self.DecryptionButton.hide()
        self.input_encrypt.hide()
        self.ClearTextButton.hide()
        self.CopyPublicTokenButton.hide()
        self.CopySecretTokenButton.hide()
        self.CopyTextButton.hide()
        self.PasteTextButton.hide()

        self.ChooseButton2.clicked.connect(self.UpdateLanguageInterfaceRussia)
        self.input_encrypt2.viewport().setCursor(QCursor(Qt.ArrowCursor))
        self.input_encrypt2.setReadOnly(True)

        self.PastePUBLICTextButtons = QPushButton("Paste PUBLIC\nToken", self)
        self.PastePUBLICTextButtons.setStyleSheet(self.ButtonStyleThree)
        self.PastePUBLICTextButtons.setGeometry(90, 450, 110, 50)
        self.PastePUBLICTextButtons.clicked.connect(self.PastePublicToken)

        self.PasteSECRETTextButtons = QPushButton("Paste SECRET\nToken", self)
        self.PasteSECRETTextButtons.setStyleSheet(self.ButtonStyleThree)
        self.PasteSECRETTextButtons.setGeometry(245, 450, 110, 50)
        self.PasteSECRETTextButtons.clicked.connect(self.PasteSecretToken)

        self.CopyDecryptedTextButton = QPushButton("Copy Text →", self)
        self.CopyDecryptedTextButton.setStyleSheet(self.ButtonStyleThree)
        self.CopyDecryptedTextButton.setGeometry(470, 100, 110, 50)
        self.CopyDecryptedTextButton.clicked.connect(self.CopyDecryptedText)

        QLineEditStyle = """
            QPlainTextEdit {
                color: #fff;
                font-size: 15px;
                border: 1px solid #1c1c1c;
                padding: 10px;
                background-color: #0c0c0c;
            }

            QPlainTextEdit::hover {
                border: 1px solid #2F2F32;
            }
        """
        self.input_encrypt2.setPlaceholderText(self.YourTextEn)

        self.EncryptionButton.clicked.connect(self.Decryption)

        self.input_PUBLIC_key = QPlainTextEdit(self)
        self.input_PUBLIC_key.setPlaceholderText("Enter your PUBLIC token")
        self.input_PUBLIC_key.setStyleSheet(QLineEditStyle)
        # self.input_PUBLIC_key.maxLength(100_000)
        self.input_PUBLIC_key.setGeometry(50, 250, 400, 50)

        self.input_SECRET_key = QPlainTextEdit(self)
        self.input_SECRET_key.setPlaceholderText("Enter your SECRET token")
        self.input_SECRET_key.setStyleSheet(QLineEditStyle)
        # self.input_SECRET_key.maxLength(100_000)
        self.input_SECRET_key.setGeometry(50, 350, 400, 50)

    def UpdateLanguageInterfaceRussia(self):
        self.input_PUBLIC_key.setPlaceholderText("Введите свой ОБЩЕДОСТУПНЫЙ токен")
        self.input_SECRET_key.setPlaceholderText("Введите свой СЕКРЕТНЫЙ токен")
        self.input_encrypt2.setPlaceholderText("Ваш Текст")
        self.PastePUBLICTextButtons.setText("Вставить ПУБЛИЧНЫЙ\nТокен")
        self.PastePUBLICTextButtons.setGeometry(70, 450, 170, 50)
        self.PasteSECRETTextButtons.setText("Вставить СЕКРЕТНЫЙ\nТокен")
        self.Couldndecipher = "Не удалось расшифровать, проверьте, правильно ли вы записали токены"
        self.PasteSECRETTextButtons.setGeometry(250, 450, 170, 50)
        self.CopyDecryptedTextButton.setText("Копировать →\nТекст")

    def UpdateLanguageInterfaceEnglish(self):
        self.input_PUBLIC_key.setPlaceholderText("Enter your PUBLIC Token")
        self.input_SECRET_key.setPlaceholderText("Enter your SECRET Token")
        self.input_encrypt2.setPlaceholderText("Your text")
        self.PastePUBLICTextButtons.setText("Paste PUBLIC\nToken")
        self.PastePUBLICTextButtons.setGeometry(70, 450, 170, 50)
        self.PasteSECRETTextButtons.setText("Paste SECRET\nToken")
        self.PasteSECRETTextButtons.setGeometry(250, 450, 170, 50)
        self.Couldndecipher = "Couldn't decrypt, check if you wrote down the tokens correctly"
        self.CopyDecryptedTextButton.setText("Copy Text →")

    def Decryption(self):  # Decryption
        PUBLIC_KEY = self.input_PUBLIC_key.toPlainText()
        SECRET_KEY = self.input_SECRET_key.toPlainText()

        if PUBLIC_KEY != "" and SECRET_KEY != "":
            from cryptography.fernet import Fernet

            try:
                f = Fernet(bytes(SECRET_KEY, encoding='utf-8'))
                detoken = f.decrypt(bytes(PUBLIC_KEY, encoding='utf-8'))

                self.input_encrypt2.setPlainText(str(detoken.decode('utf-8')))
            except Exception:
                self.input_encrypt2.setPlainText(f"{self.Couldndecipher}")
        else:
            pass

    def PastePublicToken(self):
        if self.copytoken != None:
            self.input_PUBLIC_key.setPlainText(self.copytoken.text())

    def PasteSecretToken(self):
        if self.copytoken != None:
            self.input_SECRET_key.setPlainText(self.copytoken.text())

    def CopyDecryptedText(self):
        if self.copytoken != None and self.input_encrypt2.toPlainText() != "":
            self.copytoken.setText(self.input_encrypt2.toPlainText())
            self.NotificationCopyText()

class InfoWindow(Window):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setWindowTitle("Information Scrambler")
        self.OpenPanelButton.hide()
        self.DecryptionButton.hide()
        self.input_encrypt.hide()
        self.ClearTextButton.hide()
        self.CopyPublicTokenButton.hide()
        self.CopySecretTokenButton.hide()
        self.CopyTextButton.hide()
        self.PasteTextButton.hide()
        self.InfoButton.hide()
        self.EncryptionButton.hide()
        self.input_encrypt2.hide()
        self.DescriptionChoose.hide()

        self.SliderSizeTextInfoStyle = """
             QSlider{
                background: none;
            }
        """
        self.SliderSizeTextInfo = QSlider(Qt.Orientation.Vertical, self)
        self.SliderSizeTextInfo.setGeometry(75, 230, 20, 250)
        self.SliderSizeTextInfo.setStyleSheet(self.SliderSizeTextInfoStyle)
        self.SliderSizeTextInfo.setRange(0, 100)
        self.SliderSizeTextInfo.setValue(17)
        self.SliderSizeTextInfo.setMaximum(100)
        self.SliderSizeTextInfo.setMinimum(1)
        self.SliderSizeTextInfo.valueChanged.connect(self.UpdateSizeInfoText)

        self.ChooseLangEnglishButton = QRadioButton("English", self)
        self.ChooseLangEnglishButton.setGeometry(850, 100, 100, 30)
        self.ChooseLangEnglishButton.nextCheckState()
        self.ChooseLangEnglishButton.setStyleSheet(self.ChooseButtonStyle)
        self.ChooseLangEnglishButton.clicked.connect(self.UpdateInfoLangEnglish)

        self.ChooseLangRussiaButton = QRadioButton("Руский", self)
        self.ChooseLangRussiaButton.setGeometry(850, 150, 100, 30)
        self.ChooseLangRussiaButton.setStyleSheet(self.ChooseButtonStyle)
        self.ChooseLangRussiaButton.clicked.connect(self.UpdateInfoLangRussia)

        self.ResetSlideButton = QPushButton("R", self)
        self.ResetSlideButton.setGeometry(70, 500, 30, 30)
        self.ResetSlideButton.setStyleSheet(self.ButtonCopyTokenStyle)
        self.ResetSlideButton.setToolTip("Reset Size")
        self.ResetSlideButton.clicked.connect(self.ResetSizeInfoText)



        self.InfoPlainTextStyle = """
            QPlainTextEdit {
                color: grey;
                font-size: 17px;
                padding: 10px;
                border: none;
            }

            QPlainTextEdit::hover {
                color: #fff;
            }
        """
        self.InfoPlainText = QPlainTextEdit(self)
        self.InfoPlainText.setGeometry(150, 50, 650, 600)
        self.InfoPlainText.setStyleSheet(self.InfoPlainTextStyle)
        self.InfoPlainText.viewport().setCursor(QCursor(Qt.ArrowCursor))
        self.InfoPlainText.setReadOnly(True)



        self.InformationEnglish = """
Working with the Scrambler program (Encryption and Decryption) You can encrypt your messages or a large amount of text into Tokens (Keys).

1) As soon as you run the Scrambler Encryption program, a window with two fields and buttons will appear

1.1) There will be three buttons under the first field (Copy text, Clear Text, Paste text) they work with your clipboard

1.2) Under the second field there are buttons (Copy PUBLIC Token, Copy PRIVATE Token)

1.3) To encrypt your message, click on the button (Arrow "➜")

Attention: We strongly recommend that you use the interface buttons in order to avoid errors and incorrect work with the program.

2) In the Scrambler Encryption program, you write your message in the first field or using the (Insert text) button You paste your text into the first field (after which you can click on "➜" )

Russian Russian 3) We have taken care of the interface language and added Russian (At the moment there are only two languages in the program: Russian, English)

4) To decrypt your message, open the panel (by clicking on "≡") and after clicking on the ( 'Decoding' | 'Расшифровка' ) button, you will have a new window (Scrambler Decryption) that decrypts your messages by accepting a Public and Private Token

5) You will see three fields and buttons (Insert a PUBLIC Token, Insert a PRIVATE Token) and again we advise you to use them...

5.1) After you have opened the (Scrambler Decryption) window, you can copy FROM the "Scrambler Encryption" window (by clicking on the "Copy PUBLIC Token" button) and go to the (Scrambler Decryption) window after clicking on the (Insert PUBLIC Token) button in the same scenario (copy PRIVATE Token) and click the appropriate button to insert the PRIVATE Key into the appropriate field by clicking (Insert PRIVATE Key) and then click on "➜"

Errors that you may encounter:
1) Failed to decrypt, check if you wrote the tokens correctly - (You cannot decrypt the message WITHOUT a PRIVATE KEY)

2) Failed to encrypt - (Occurs when you do not understand the input of characters that cannot be read by the program "Scrambler Encryption")

Support:

Telegram Channel: @ProgramsCreatorRu
Profile: @ProgramsCreator
        """

        self.InformationRussia = """
Работа с программой Scrambler (Encryption and Decryption) Вы можете шифровать свои сообщения или большой объем текста в Токены (Ключи);

1) Как только Вы запустите программу Scrambler Encryption, то появится окно c двумя полями и кнопками;

1.1) Под первым полем будут три кнопки (Копировать текст, Очистить текст, Вставить текст) они работают c Вашим буфером обмена;

1.2) Под вторым полем находятся кнопки (Копировать ПУБЛИЧНЫЙ Токен, Копировать ПРИВАТНЫЙ Токен);

1.3) Чтобы зашифровать Ваше сообщение нажмите на кнопку (Стрелка "➜");

Внимание: Настоятельно  рекомендуем Вам пользоваться кнопками интерфейса, дабы избежать ошибок и некорректной работы c программой;

2) В программе Scrambler Encryption, в первое поле Вы записываете своё сообщение или пользуясь кнопкой (Вставить текст) Вы вставляете свой текст в первое поле (после чего можете нажать на "➜" )

3) Мы позаботились языком интерфейса и добавили Русский Язык (на данный момент в программе только два языка: Русский , Английский)

4) Для Расшифровывания вашего сообщения откройте панель (нажав на "≡" ) и после внизу на кнопку ( 'Decoding' | 'Расшифровка' ), у вас откроется новое окно (Scrambler Decryption ) которое _расшифровывает_ Ваши сообщения принимая Публичный и Приватный Токен;

5) У Вас отобразится три поля и кнопки (Вставить ПУБЛИЧНЫЙ Токен, Вставить ПРИВАТНЫЙ Токен) и снова Вам советуем пользоваться кнопками;

5.1) После того как открыли (Scrambler Decryption ) окно то Вы сможете скопировать ИЗ окна "Scrambler Encryption" (нажав на кнопку "Копировать ПУБЛИЧНЫЙ Токен") и перейти на окно (Scrambler Decryption) после нажать на кнопку (Вставить ПУБЛИЧНЫЙ Токен), таким же сценарием (копируете ПРИВАТНЫЙ Токен)  и жмёте соответствующую кнопку для вставки ПРИВАТНОГО Ключа в соответствующее поле нажав (Вставить ПРИВАТНЫЙ Ключ), после чего жмите на "➜"

Ощибки с которыми Вы сможете столкнуться:
1) Не удалось расшифровать, проверьте, правильно ли вы записали токены - (Вы не можете расшифровать сообщение БЕЗ ПРИВАТНОГО КЛЮЧА)

2)  Не удалось зашифровать - (Возникает при не понятном вводе сиволов которых не прочесть программе "Scrambler Encryption")

Поддержка:
Telegram Канал: @ProgramsCreatorRu
Профиль: @ProgramsCreator
        """
        self.installEventFilter(self)
        self.InfoPlainText.setPlainText(self.InformationEnglish)

    def UpdateInfoLangEnglish(self):
        self.InfoPlainText.setPlainText(self.InformationEnglish)
        self.ResetSlideButton.setToolTip("Reset Size")

    def UpdateInfoLangRussia(self):
        self.InfoPlainText.setPlainText(self.InformationRussia)
        self.ResetSlideButton.setToolTip("Сбросить размер")

    def UpdateSizeInfoText(self, value):
        try:
            NewSizeInfoText = self.InfoPlainTextStyle.replace("font-size: 17", "font-size: " + str(value))
            self.InfoPlainText.setStyleSheet(NewSizeInfoText)
        except:
            pass

    def ResetSizeInfoText(self):
        self.SliderSizeTextInfo.setValue(17)
        self.InfoPlainText.setStyleSheet(self.InfoPlainTextStyle)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            self.ResetSizeInfoText()

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.MouseButtonPress,
                            QEvent.MouseButtonDblClick):
            return True
        return super(InfoWindow, self).eventFilter(obj, event)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())
