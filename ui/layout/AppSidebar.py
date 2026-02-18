from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtGui as qtg
from ui.locales import t, get_lang_list, set_lang_code

class AppSidebar(QWidget):
    """现代风格的侧边栏组件"""
    
    # 信号
    menu_clicked = pyqtSignal(str)  # 菜单项点击信号
    toggled = pyqtSignal(bool)      # 侧边栏折叠状态变化信号
    
    def __init__(self, parent=None, secondary_color="#f8f9fa", text_color="#212529", width=220, collapsed_width=60):
        """初始化侧边栏
        
        Args:
            parent: 父窗口
            secondary_color: 侧边栏背景色
            text_color: 侧边栏文本色
            width: 侧边栏展开宽度
            collapsed_width: 侧边栏折叠宽度
        """
        super().__init__(parent)
        
        # 配置
        self.secondary_color = secondary_color
        self.text_color = text_color
        self.width = width
        self.collapsed_width = collapsed_width
        self.is_collapsed = False
        self.current_page = None
        
        # 创建布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # 创建品牌区域
        self.create_brand()
        
        # 创建菜单区域
        self.create_menu()
        
        # 创建折叠按钮
        self.create_toggle_button()
        
        # 设置样式
        self.set_style()
        
        # 设置初始宽度
        self.setFixedWidth(self.width)
        
        # 设置为顶层部件，覆盖标题栏
        self.raise_()
    
    def create_brand(self):
        """创建品牌区域"""
        # 品牌部件
        self.brand = QWidget()
        self.brand.setFixedHeight(60)
        self.brand_layout = QHBoxLayout(self.brand)
        self.brand_layout.setContentsMargins(20, 0, 20, 0)
        
        # 品牌图标
        self.brand_icon = QLabel()
        self.brand_icon.setPixmap(qtg.QPixmap("assets/logo/logo32.png"))
        self.brand_icon.setFixedSize(32, 32)
        self.brand_icon.setAlignment(Qt.AlignCenter)
        
        # 品牌名称
        self.brand_name = QLabel("Minelancher")
        self.brand_name.setAlignment(Qt.AlignCenter)
        
        self.brand_layout.addWidget(self.brand_icon)
        self.brand_layout.addWidget(self.brand_name)
        self.brand_layout.addStretch()
        
        self.layout.addWidget(self.brand)
    
    def create_menu(self):
        """创建菜单区域"""
        # 菜单部件
        self.menu = QWidget()
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setContentsMargins(0, 20, 0, 0)  # 顶部留出空间
        self.menu_layout.setSpacing(0)
        
        # 菜单项 - 只保留首页按钮
        self.menu_items = {
            "home": {"text": t("sidebar.home"), "icon": "■"}
        }
        
        # 创建菜单项按钮
        self.menu_buttons = {}
        for id, info in self.menu_items.items():
            button = QPushButton()
            button.setFixedHeight(48)
            button_layout = QHBoxLayout(button)
            button_layout.setContentsMargins(20, 0, 20, 0)
            
            # 图标
            icon_label = QLabel(info["icon"])
            icon_label.setFixedSize(24, 24)
            icon_label.setAlignment(Qt.AlignCenter)
            
            # 文本
            text_label = QLabel(info["text"])
            text_label.setAlignment(Qt.AlignCenter)
            
            button_layout.addWidget(icon_label)
            button_layout.addWidget(text_label)
            button_layout.addStretch()
            
            # 连接信号
            button.clicked.connect(lambda checked, id=id: self.on_menu_clicked(id))
            
            self.menu_buttons[id] = button
            self.menu_layout.addWidget(button)
        
        # 在菜单下方添加伸缩空间，使按钮集中在顶部
        self.menu_layout.addStretch()
        
        self.layout.addWidget(self.menu, 1)
    
    def create_toggle_button(self):
        """创建折叠按钮"""
        # 折叠按钮部件
        self.toggle = QWidget()
        self.toggle.setFixedHeight(48)
        self.toggle_layout = QHBoxLayout(self.toggle)
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)
        
        # 按钮
        self.toggle_button = QPushButton("«")
        self.toggle_button.setFixedSize(self.width, 48)
        self.toggle_button.clicked.connect(self.toggle_sidebar)
        
        self.toggle_layout.addWidget(self.toggle_button)
        self.layout.addWidget(self.toggle)
    
    def set_style(self):
        """设置样式"""
        # 侧边栏样式
        style = """
        QWidget {
            background-color: %s;
            border-right: 1px solid #e9ecef;
        }
        QLabel {
            color: %s;
            font-size: 14px;
            font-family: 黑体;
            background-color: transparent;
        }
        QPushButton {
            background-color: transparent;
            color: %s;
            font-size: 14px;
            font-family: 黑体;
            border: none;
            text-align: left;
            padding: 0px;
        }
        QPushButton:hover {
            background-color: #e9ecef;
        }
        QPushButton:hover QLabel {
            color: #007bff;
        }
        QPushButton:pressed {
            background-color: #dee2e6;
        }
        """
        self.setStyleSheet(style % (self.secondary_color, self.text_color, self.text_color))
        
        # 品牌图标样式
        brand_icon_style = """
        QLabel {
            background-color: #ffffff;
            color: #007bff;
            border-radius: 6px;
            font-weight: bold;
            font-size: 16px;
        }
        """
        self.brand_icon.setStyleSheet(brand_icon_style)
        
        # 品牌名称样式
        brand_name_style = """
        QLabel {
            color: %s;
            font-weight: bold;
            font-size: 16px;
            margin-left: 10px;
        }
        """
        self.brand_name.setStyleSheet(brand_name_style % self.text_color)
        
        # 折叠按钮样式
        toggle_button_style = """
        QPushButton {
            background-color: transparent;
            color: %s;
            font-size: 16px;
            border: none;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #e9ecef;
        }
        """
        self.toggle_button.setStyleSheet(toggle_button_style % self.text_color)
    
    def toggle_sidebar(self):
        """折叠/展开侧边栏"""
        self.is_collapsed = not self.is_collapsed
        
        if self.is_collapsed:
            # 折叠
            target_width = self.collapsed_width
            self.brand_name.setVisible(False)
            for id, button in self.menu_buttons.items():
                # 隐藏文本，只显示图标
                layout = button.layout()
                if layout.count() > 1:
                    layout.itemAt(1).widget().setVisible(False)
            self.toggle_button.setText("»")
        else:
            # 展开
            target_width = self.width
            self.brand_name.setVisible(True)
            for id, button in self.menu_buttons.items():
                # 显示文本
                layout = button.layout()
                if layout.count() > 1:
                    layout.itemAt(1).widget().setVisible(True)
            self.toggle_button.setText("«")
        
        # 先设置目标宽度，避免崩溃
        self.setFixedWidth(target_width)
        # 更新折叠按钮大小
        self.toggle_button.setFixedWidth(target_width)
        
        # 发送信号
        self.toggled.emit(self.is_collapsed)
    
    def on_menu_clicked(self, menu_id):
        """菜单项点击事件"""
        # 发送信号
        self.menu_clicked.emit(menu_id)
    
    def set_collapsed(self, collapsed):
        """设置侧边栏折叠状态
        
        Args:
            collapsed: 是否折叠
        """
        if collapsed != self.is_collapsed:
            self.toggle_sidebar()
    
    def set_current_page(self, page_id):
        """设置当前选中的页面
        
        Args:
            page_id: 页面ID
        """
        self.current_page = page_id
        # 更新菜单项样式
        self.update_menu_styles()
    
    def update_menu_styles(self):
        """更新菜单项样式，根据当前选中的页面"""
        for id, button in self.menu_buttons.items():
            if id == self.current_page:
                # 选中状态
                button.setStyleSheet("""
                QPushButton {
                    background-color: #e9ecef;
                    color: %s;
                    border: none;
                    text-align: left;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                }
                QPushButton:hover QLabel {
                    color: %s;
                }
                QPushButton QLabel {
                    color: %s;
                    background-color: transparent;
                }
                """ % (self.text_color, self.text_color, self.text_color))
            else:
                # 未选中状态，重置为默认样式
                button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: %s;
                    border: none;
                    text-align: left;
                    padding: 0px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                }
                QPushButton:hover QLabel {
                    color: %s;
                }
                QPushButton QLabel {
                    color: %s;
                    background-color: transparent;
                }
                """ % (self.text_color, self.text_color, self.text_color))

# 测试代码
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QLabel
    import sys
    
    app = QApplication(sys.argv)
    
    # 创建主窗口
    window = QMainWindow()
    window.setWindowTitle("AppSidebar 测试")
    window.setGeometry(100, 100, 900, 600)
    
    # 创建中央部件
    central_widget = QWidget()
    layout = QHBoxLayout(central_widget)
    
    # 创建侧边栏
    sidebar = AppSidebar(window)
    layout.addWidget(sidebar)
    
    # 创建内容区域
    content = QWidget()
    content_layout = QHBoxLayout(content)
    content.setStyleSheet("background-color: #f8f9fa;")
    
    # 内容标签
    content_label = QLabel("内容区域")
    content_label.setAlignment(Qt.AlignCenter)
    content_label.setStyleSheet("font-size: 18px; color: #6c757d;")
    content_layout.addWidget(content_label)
    
    layout.addWidget(content, 1)
    
    # 连接信号
    def on_menu_clicked(menu_id):
        print(f"菜单项点击: {menu_id}")
        content_label.setText(f"内容区域 - {sidebar.menu_items[menu_id]['text']}")
    
    def on_toggled(collapsed):
        print(f"侧边栏状态: {'折叠' if collapsed else '展开'}")
    
    sidebar.menu_clicked.connect(on_menu_clicked)
    sidebar.toggled.connect(on_toggled)
    
    window.setCentralWidget(central_widget)
    window.show()
    
    sys.exit(app.exec_())
