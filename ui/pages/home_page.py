from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QListWidget, QListWidgetItem, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt
from .base_page import BasePage

class HomePage(BasePage):
    """首页页面"""
    
    def setup_ui(self):
        """设置UI"""
        super().setup_ui()
        
        # 添加伸缩空间
        self.layout.addStretch(1)
        
        # 创建模式切换标签页
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
        QTabWidget {
            font-family: 黑体;
        }
        QTabBar {
            font-size: 14px;
        }
        QTabBar::tab {
            padding: 10px 24px;
            margin: 0 2px;
            background-color: #e9ecef;
            border: 1px solid #dee2e6;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        QTabBar::tab:selected {
            background-color: white;
            border-bottom: 1px solid white;
        }
        """)
        
        # 创建正版模式页面
        self.official_page = QWidget()
        self.create_official_page()
        
        # 创建离线模式页面
        self.offline_page = QWidget()
        self.create_offline_page()
        
        # 添加标签页
        self.tab_widget.addTab(self.official_page, "正版")
        self.tab_widget.addTab(self.offline_page, "离线")
        
        self.layout.addWidget(self.tab_widget)
        
        # 添加伸缩空间
        self.layout.addStretch(1)
    
    def create_official_page(self):
        """创建正版模式页面"""
        layout = QVBoxLayout(self.official_page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 创建账号列表标题
        account_title = QLabel("账号列表")
        account_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #212529; font-family: 黑体;")
        layout.addWidget(account_title)
        
        # 创建账号列表
        self.account_list = QListWidget()
        self.account_list.setStyleSheet("""
        QListWidget {
            font-family: 黑体;
            font-size: 14px;
            border: 1px solid #dee2e6;
            border-radius: 8px;
        }
        QListWidget::item {
            padding: 12px;
            border-bottom: 1px solid #e9ecef;
        }
        QListWidget::item:last-child {
            border-bottom: none;
        }
        QListWidget::item:selected {
            background-color: #e9ecef;
        }
        """)
        

        
        layout.addWidget(self.account_list)
        
        # 创建添加新账号按钮
        add_account_btn = QPushButton("添加新账号")
        add_account_btn.setStyleSheet("""
        QPushButton {
            padding: 10px 20px;
            font-size: 14px;
            font-family: 黑体;
            background-color: #6c757d;
            color: white;
            border: none;
            border-radius: 6px;
        }
        QPushButton:hover {
            background-color: #5a6268;
        }
        QPushButton:pressed {
            background-color: #495057;
        }
        """)
        add_account_btn.clicked.connect(self.add_new_account)
        layout.addWidget(add_account_btn)
        
        # 添加伸缩空间
        layout.addStretch()
        
        # 创建底部按钮区域
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(20)
        
        # 创建启动按钮
        launch_btn = QPushButton("启动")
        launch_btn.setStyleSheet("""
        QPushButton {
            padding: 14px 32px;
            font-size: 18px;
            font-family: 黑体;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #0069d9;
        }
        QPushButton:pressed {
            background-color: #005cbf;
        }
        """)
        
        # 创建设置按钮
        settings_btn = QPushButton("设置")
        settings_btn.setStyleSheet("""
        QPushButton {
            padding: 10px 20px;
            font-size: 14px;
            font-family: 黑体;
            background-color: #f8f9fa;
            color: #495057;
            border: 1px solid #dee2e6;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #e9ecef;
            border-color: #ced4da;
        }
        QPushButton:pressed {
            background-color: #dee2e6;
            border-color: #adb5bd;
        }
        """)
        
        bottom_layout.addWidget(launch_btn, 1)
        bottom_layout.addWidget(settings_btn)
        
        layout.addLayout(bottom_layout)
    
    def create_offline_page(self):
        """创建离线模式页面"""
        layout = QVBoxLayout(self.offline_page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # 创建用户名输入区域
        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        
        # 创建用户名输入框
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("请输入用户名")
        self.username_input.setStyleSheet("""
        QLineEdit {
            padding: 10px;
            font-size: 14px;
            font-family: 黑体;
            border: 1px solid #dee2e6;
            border-radius: 6px;
        }
        QLineEdit:focus {
            border-color: #007bff;
        }
        """)
        
        form_layout.addRow("用户名:", self.username_input)
        layout.addLayout(form_layout)
        
        # 添加伸缩空间
        layout.addStretch()
        
        # 创建底部按钮区域
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(20)
        
        # 创建启动按钮
        launch_btn = QPushButton("启动")
        launch_btn.setStyleSheet("""
        QPushButton {
            padding: 14px 32px;
            font-size: 18px;
            font-family: 黑体;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #0069d9;
        }
        QPushButton:pressed {
            background-color: #005cbf;
        }
        """)
        
        # 创建设置按钮
        settings_btn = QPushButton("设置")
        settings_btn.setStyleSheet("""
        QPushButton {
            padding: 10px 20px;
            font-size: 14px;
            font-family: 黑体;
            background-color: #f8f9fa;
            color: #495057;
            border: 1px solid #dee2e6;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #e9ecef;
            border-color: #ced4da;
        }
        QPushButton:pressed {
            background-color: #dee2e6;
            border-color: #adb5bd;
        }
        """)
        
        bottom_layout.addWidget(launch_btn, 1)
        bottom_layout.addWidget(settings_btn)
        
        layout.addLayout(bottom_layout)
    
    def add_new_account(self):
        """添加新账号"""
        # 暂时只打印日志，不实现具体功能
        print("添加新账号")
    
    def on_show(self):
        """页面显示时调用"""
        print("首页显示")
