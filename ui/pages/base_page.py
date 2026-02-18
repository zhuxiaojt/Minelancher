from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class BasePage(QWidget):
    """所有页面的基类"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(self.__class__.__name__)
        self.setup_ui()
    
    def setup_ui(self):
        """设置UI"""
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(10)
    
    def update_content(self):
        """更新页面内容"""
        pass
    
    def on_show(self):
        """页面显示时调用"""
        pass
    
    def on_hide(self):
        """页面隐藏时调用"""
        pass
