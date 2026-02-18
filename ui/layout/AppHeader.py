from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QMenu, QAction, QWidgetAction
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPalette, QColor
from ui.locales import t, get_lang_list, set_lang_code, lang_code

class AppHeader(QWidget):
    """现代风格的标题栏组件"""
    
    def __init__(self, main_window=None, title="Minelancher", primary_color="#ffffff", text_color="#212529"):
        """初始化标题栏
        
        Args:
            main_window: 主窗口
            title: 应用标题
            primary_color: 标题栏背景色
            text_color: 标题栏文本色
        """
        super().__init__()
        
        # 保存主窗口引用
        self.main_window = main_window
        
        # 配置
        self.title = title
        self.primary_color = primary_color
        self.text_color = text_color
        self.setFixedHeight(40)
        
        # 拖动相关
        self.drag_pos = QPoint()
        
        # 创建布局
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(20, 0, 10, 0)
        self.layout.setSpacing(0)
        
        # 创建应用信息区域
        self.create_app_info()
        
        # 创建控制按钮区域
        self.create_controls()
        
        # 设置样式
        self.set_style()
    
    def set_title(self, title):
        """设置标题栏标题
        
        Args:
            title: 新的标题
        """
        self.title = title
        self.app_name.setText(title)
    
    def create_app_info(self):
        """创建应用名称（不含图标）"""
        # 应用信息部件
        self.app_info = QWidget()
        self.app_info_layout = QHBoxLayout(self.app_info)
        self.app_info_layout.setContentsMargins(0, 0, 0, 0)
        self.app_info_layout.setSpacing(10)
        
        # 应用名称
        self.app_name = QLabel(self.title)
        self.app_name.setAlignment(Qt.AlignCenter)
        self.app_name.setStyleSheet(f"color: {self.text_color}; font-weight: bold; font-size: 14px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;")
        self.app_info_layout.addWidget(self.app_name)
        
        self.layout.addWidget(self.app_info)
        self.layout.addStretch()
    
    def create_controls(self):
        """创建窗口控制按钮"""
        # 控制按钮部件
        self.controls = QWidget()
        self.controls_layout = QHBoxLayout(self.controls)
        self.controls_layout.setContentsMargins(0, 0, 0, 0)
        self.controls_layout.setSpacing(0)
        
        # 语言切换按钮
        self.lang_btn = QPushButton("🌐")
        self.lang_btn.setFixedSize(40, 40)
        # 去掉小三角形并调整图标显示
        self.lang_btn.setStyleSheet("""
        QPushButton {
            background-color: transparent;
            border: none;
            padding: 0px;
            text-align: center;
        }
        QPushButton::menu-indicator {
            image: none;
        }
        """)
        self.controls_layout.addWidget(self.lang_btn)
        
        # 创建语言菜单
        self.lang_menu = QMenu()
        # 设置菜单样式
        self.lang_menu.setStyleSheet("""
        QMenu {
            background-color: rgba(255, 255, 255, 0.95);
            border: 1px solid #e9ecef;
            border-radius: 4px;
            padding: 5px 0;
        }
        QMenu::item {
            padding: 8px 20px;
            font-family: 黑体;
            font-size: 14px;
            color: #212529;
        }
        QMenu::item:hover {
            background-color: #e9ecef;
            color: #007bff;
        }
        QMenu::item:selected {
            background-color: #e9ecef;
            color: #007bff;
        }
        """)
        self.lang_actions = {}
        
        # 添加语言选项
        for lang in get_lang_list():
            # 创建自定义菜单项
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(20, 8, 20, 8)
            layout.setSpacing(0)
            
            label = QLabel(lang["lang_name"])
            label.setStyleSheet("font-family: 黑体; font-size: 14px;")
            
            # 检查是否是当前语言
            if lang["lang_code"] == lang_code:
                # 为当前语言设置与悬停效果一样的样式
                widget.setStyleSheet("background-color: #e9ecef;")
                label.setStyleSheet("font-family: 黑体; font-size: 14px; color: #007bff;")
            
            layout.addWidget(label)
            widget.setLayout(layout)
            
            # 创建QWidgetAction
            action = QWidgetAction(self)
            action.setDefaultWidget(widget)
            action.triggered.connect(lambda checked, code=lang["lang_code"]: self.on_lang_change(code))
            # 存储语言代码到action的data中
            action.setData(lang["lang_code"])
            
            self.lang_actions[lang["lang_code"]] = action
            self.lang_menu.addAction(action)
        
        self.lang_btn.setMenu(self.lang_menu)
        
        # 最小化按钮
        self.minimize_btn = QPushButton("_")
        self.minimize_btn.setFixedSize(40, 40)
        self.minimize_btn.clicked.connect(self.on_minimize)
        self.controls_layout.addWidget(self.minimize_btn)
        
        # 最大化按钮
        self.maximize_btn = QPushButton("□")
        self.maximize_btn.setFixedSize(40, 40)
        self.maximize_btn.clicked.connect(self.on_maximize)
        self.controls_layout.addWidget(self.maximize_btn)
        
        # 关闭按钮
        self.close_btn = QPushButton("×")
        self.close_btn.setFixedSize(40, 40)
        self.close_btn.setObjectName("closeButton")
        self.close_btn.clicked.connect(self.on_close)
        self.controls_layout.addWidget(self.close_btn)
        
        self.layout.addWidget(self.controls)
    
    def on_lang_change(self, lang_code):
        """语言切换事件"""
        set_lang_code(lang_code)
        
        # 清空并重新添加语言选项，确保当前语言有特殊样式
        self.lang_menu.clear()
        self.lang_actions = {}
        
        for lang in get_lang_list():
            # 创建自定义菜单项
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(20, 8, 20, 8)
            layout.setSpacing(0)
            
            label = QLabel(lang["lang_name"])
            label.setStyleSheet("font-family: 黑体; font-size: 14px;")
            
            # 检查是否是当前语言
            if lang["lang_code"] == lang_code:
                # 为当前语言设置与悬停效果一样的样式
                widget.setStyleSheet("background-color: #e9ecef;")
                label.setStyleSheet("font-family: 黑体; font-size: 14px; color: #007bff;")
            
            layout.addWidget(label)
            widget.setLayout(layout)
            
            # 创建QWidgetAction
            action = QWidgetAction(self)
            action.setDefaultWidget(widget)
            action.triggered.connect(lambda checked, code=lang["lang_code"]: self.on_lang_change(code))
            # 存储语言代码到action的data中
            action.setData(lang["lang_code"])
            
            self.lang_actions[lang["lang_code"]] = action
            self.lang_menu.addAction(action)
        
        # 这里可以添加更新界面语言的逻辑
        print(f"语言切换为: {lang_code}")
    
    def set_style(self):
        """设置样式"""
        # 标题栏样式
        style = """
        QWidget {
            background-color: %s;
            border-bottom: 1px solid #e9ecef;
        }
        QLabel {
            color: %s;
            font-weight: bold;
            font-size: 14px;
            font-family: 黑体;
        }
        QPushButton {
            background-color: transparent;
            color: %s;
            font-size: 14px;
            font-family: 黑体;
            border: none;
            padding: 10px;
            margin: 0;
        }
        QPushButton:hover {
            background-color: #e9ecef;
        }
        QPushButton#closeButton:hover {
            background-color: #dc3545 !important;
            color: white !important;
        }
        """
        self.setStyleSheet(style % (self.primary_color, self.text_color, self.text_color))
    
    def on_minimize(self):
        """最小化窗口"""
        if self.main_window:
            self.main_window.showMinimized()
    
    def on_maximize(self):
        """最大化窗口"""
        if self.main_window:
            if self.main_window.isMaximized():
                self.main_window.showNormal()
                self.maximize_btn.setText("□")
            else:
                self.main_window.showMaximized()
                self.maximize_btn.setText("▢")
    
    def on_close(self):
        """关闭窗口"""
        if self.main_window:
            self.main_window.close()
    
    def mousePressEvent(self, event):
        """鼠标按下事件，开始拖动"""
        if event.button() == Qt.LeftButton:
            if self.main_window:
                # 检查鼠标是否在窗口边缘，如果是则不执行拖动
                # 将局部坐标转换为全局坐标，再转换为主窗口的局部坐标
                global_pos = event.globalPos()
                main_window_local_pos = self.main_window.mapFromGlobal(global_pos)
                
                # 检查是否在窗口边缘（边缘大小8像素）
                edge_size = 8
                rect = self.main_window.rect()
                is_at_edge = (
                    main_window_local_pos.x() <= edge_size or
                    main_window_local_pos.x() >= rect.width() - edge_size or
                    main_window_local_pos.y() <= edge_size or
                    main_window_local_pos.y() >= rect.height() - edge_size
                )
                
                if not is_at_edge:
                    self.drag_pos = global_pos - self.main_window.frameGeometry().topLeft()
                    event.accept()
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件，拖动窗口"""
        if event.buttons() == Qt.LeftButton and self.drag_pos:
            if self.main_window:
                # 检查鼠标是否在窗口边缘，如果是则不执行拖动
                global_pos = event.globalPos()
                main_window_local_pos = self.main_window.mapFromGlobal(global_pos)
                
                edge_size = 8
                rect = self.main_window.rect()
                is_at_edge = (
                    main_window_local_pos.x() <= edge_size or
                    main_window_local_pos.x() >= rect.width() - edge_size or
                    main_window_local_pos.y() <= edge_size or
                    main_window_local_pos.y() >= rect.height() - edge_size
                )
                
                if not is_at_edge:
                    self.main_window.move(global_pos - self.drag_pos)
                    event.accept()
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件，结束拖动"""
        self.drag_pos = QPoint()

# 测试代码
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
    import sys
    
    app = QApplication(sys.argv)
    
    # 创建主窗口
    window = QMainWindow()
    window.setWindowTitle("AppHeader 测试")
    window.setGeometry(100, 100, 800, 600)
    window.setWindowFlags(Qt.FramelessWindowHint)
    
    # 创建中央部件
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    
    # 创建标题栏
    header = AppHeader(window, "测试应用")
    layout.addWidget(header)
    
    # 创建内容区域
    content = QWidget()
    content.setStyleSheet("background-color: #f8f9fa;")
    layout.addWidget(content, 1)
    
    window.setCentralWidget(central_widget)
    window.show()
    
    sys.exit(app.exec_())
