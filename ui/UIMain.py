import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from .layout import AppHeader, AppSidebar
from .pages import HomePage

class ResizableMainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MineLancher")
        self.setGeometry(100,100,800,600)
        self.setWindowIcon(qtg.QIcon("assets/logo/logo32.png"))
        # 隐藏系统标题栏，使用自定义标题栏
        self.setWindowFlags(qtc.Qt.FramelessWindowHint)
        
        # 添加窗口阴影
        shadow = qtw.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(qtg.QColor(0, 0, 0, 100))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)
        
        # 边缘拖动相关
        self.edge_size = 8  # 增加边缘大小，减少敏感度
        self.is_resizing = False
        self.resize_direction = None
        
    def mousePressEvent(self, event):
        if event.button() == qtc.Qt.LeftButton:
            # 检查鼠标是否在窗口边缘
            pos = event.pos()
            rect = self.rect()
            
            # 确定拖动方向
            if pos.x() <= self.edge_size:
                if pos.y() <= self.edge_size:
                    self.resize_direction = "topleft"
                elif pos.y() >= rect.height() - self.edge_size:
                    self.resize_direction = "bottomleft"
                else:
                    self.resize_direction = "left"
            elif pos.x() >= rect.width() - self.edge_size:
                if pos.y() <= self.edge_size:
                    self.resize_direction = "topright"
                elif pos.y() >= rect.height() - self.edge_size:
                    self.resize_direction = "bottomright"
                else:
                    self.resize_direction = "right"
            elif pos.y() <= self.edge_size:
                self.resize_direction = "top"
            elif pos.y() >= rect.height() - self.edge_size:
                self.resize_direction = "bottom"
            else:
                self.resize_direction = None
            
            if self.resize_direction:
                self.is_resizing = True
                self.resize_start_pos = event.globalPos()
                # 保存起始状态
                self.resize_start_geometry = self.geometry()
        
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        # 检查鼠标是否在窗口边缘，设置相应的光标
        if not self.is_resizing:
            self.update_cursor(event.pos())
        
        if self.is_resizing and self.resize_direction:
            delta = event.globalPos() - self.resize_start_pos
            
            # 直接使用原始delta值，不限制调整速度
            delta_x = delta.x()
            delta_y = delta.y()
            
            # 最小窗口大小
            min_width = 200
            min_height = 200
            
            # 起始几何信息
            geom = self.resize_start_geometry
            start_x = geom.x()
            start_y = geom.y()
            start_width = geom.width()
            start_height = geom.height()
            
            # 计算新的窗口大小和位置
            new_x = start_x
            new_y = start_y
            new_width = start_width
            new_height = start_height
            
            # 根据调整方向计算
            if self.resize_direction == "left":
                # 从左侧调整宽度
                # 当用户从左侧向右拖动鼠标时，delta_x为正，窗口应该向右缩小
                # 当用户从左侧向左拖动鼠标时，delta_x为负，窗口应该向左扩大
                
                # 计算起始右边界位置
                start_right = start_x + start_width
                
                # 计算新的左边界位置
                new_left = start_x + delta_x
                # 计算新的宽度
                new_width = start_right - new_left
                
                if new_width < min_width:
                    # 当窗口达到最小宽度时，保持右边界不变
                    new_width = min_width
                    # 计算新的左边界，确保右边界位置不变
                    new_left = start_right - new_width
                
                # 更新窗口位置和宽度
                new_x = new_left
            elif self.resize_direction == "right":
                # 从右侧调整宽度
                new_width = start_width + delta_x
                if new_width < min_width:
                    new_width = min_width
            elif self.resize_direction == "top":
                # 从顶部调整高度
                new_height = start_height - delta_y
                if new_height < min_height:
                    new_height = min_height
                    # 当窗口达到最小高度时，不移动窗口位置
                else:
                    # 窗口高度大于最小高度时，调整位置
                    new_y = start_y + delta_y
            elif self.resize_direction == "bottom":
                # 从底部调整高度
                new_height = start_height + delta_y
                if new_height < min_height:
                    new_height = min_height
            elif self.resize_direction == "topleft":
                # 处理宽度
                new_width = start_width - delta_x
                if new_width < min_width:
                    new_width = min_width
                else:
                    new_x = start_x + delta_x
                
                # 处理高度
                new_height = start_height - delta_y
                if new_height < min_height:
                    new_height = min_height
                else:
                    new_y = start_y + delta_y
            elif self.resize_direction == "topright":
                # 处理宽度
                new_width = start_width + delta_x
                if new_width < min_width:
                    new_width = min_width
                
                # 处理高度
                new_height = start_height - delta_y
                if new_height < min_height:
                    new_height = min_height
                else:
                    new_y = start_y + delta_y
            elif self.resize_direction == "bottomleft":
                # 处理宽度
                new_width = start_width - delta_x
                if new_width < min_width:
                    new_width = min_width
                else:
                    new_x = start_x + delta_x
                
                # 处理高度
                new_height = start_height + delta_y
                if new_height < min_height:
                    new_height = min_height
            elif self.resize_direction == "bottomright":
                # 处理宽度
                new_width = start_width + delta_x
                if new_width < min_width:
                    new_width = min_width
                
                # 处理高度
                new_height = start_height + delta_y
                if new_height < min_height:
                    new_height = min_height
            
            # 更新窗口几何信息
            self.setGeometry(new_x, new_y, new_width, new_height)
            
            # 注意：这里不再更新起始位置和几何信息，避免累积误差
            # 这样可以确保每次计算都基于原始的起始状态
            # 当用户释放鼠标时，起始状态会被重置
            
            event.accept()
        
        super().mouseMoveEvent(event)
    
    def update_cursor(self, pos):
        """根据鼠标位置更新光标样式"""
        rect = self.rect()
        
        # 检查鼠标是否在窗口边缘
        if pos.x() <= self.edge_size:
            if pos.y() <= self.edge_size:
                self.setCursor(qtc.Qt.SizeFDiagCursor)  # 左上
            elif pos.y() >= rect.height() - self.edge_size:
                self.setCursor(qtc.Qt.SizeBDiagCursor)  # 左下
            else:
                self.setCursor(qtc.Qt.SizeHorCursor)  # 左
        elif pos.x() >= rect.width() - self.edge_size:
            if pos.y() <= self.edge_size:
                self.setCursor(qtc.Qt.SizeBDiagCursor)  # 右上
            elif pos.y() >= rect.height() - self.edge_size:
                self.setCursor(qtc.Qt.SizeFDiagCursor)  # 右下
            else:
                self.setCursor(qtc.Qt.SizeHorCursor)  # 右
        elif pos.y() <= self.edge_size:
            self.setCursor(qtc.Qt.SizeVerCursor)  # 上
        elif pos.y() >= rect.height() - self.edge_size:
            self.setCursor(qtc.Qt.SizeVerCursor)  # 下
        else:
            self.unsetCursor()  # 恢复默认光标
    
    def enterEvent(self, event):
        """鼠标进入窗口时更新光标"""
        self.update_cursor(event.pos())
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """鼠标离开窗口时恢复默认光标"""
        self.unsetCursor()
        super().leaveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.is_resizing = False
        self.resize_direction = None
        self.unsetCursor()  # 恢复默认光标
        super().mouseReleaseEvent(event)

def create_app():
    app=qtw.QApplication([])
    return app
def create_main_window():
    # 使用自定义的可调整大小的主窗口
    main_window=ResizableMainWindow()
    
    # 创建中央部件
    central_widget=qtw.QWidget()
    main_layout=qtw.QVBoxLayout(central_widget)
    main_layout.setContentsMargins(0,0,0,0)
    main_layout.setSpacing(0)
    
    # 创建内容区域（包含侧边栏和主内容）
    content_widget=qtw.QWidget()
    content_layout=qtw.QHBoxLayout(content_widget)
    content_layout.setContentsMargins(0,0,0,0)
    content_layout.setSpacing(0)
    
    # 创建侧边栏
    sidebar=AppSidebar(main_window)
    content_layout.addWidget(sidebar)
    
    # 创建右侧区域（包含标题栏和主内容）
    right_widget=qtw.QWidget()
    right_widget.setStyleSheet("background-color: #ffffff;")
    right_layout=qtw.QVBoxLayout(right_widget)
    right_layout.setContentsMargins(0,0,0,0)
    right_layout.setSpacing(0)
    
    # 创建标题栏
    header=AppHeader(main_window=main_window, title="首页")
    right_layout.addWidget(header)
    
    # 创建主内容区域（页面容器）
    main_content=qtw.QWidget()
    main_content.setStyleSheet("background-color: #f8f9fa;")
    content_layout_inside=qtw.QVBoxLayout(main_content)
    content_layout_inside.setContentsMargins(0,0,0,0)
    content_layout_inside.setSpacing(0)
    
    # 创建页面实例
    home_page=HomePage()
    
    # 添加页面到容器
    content_layout_inside.addWidget(home_page)
    
    # 保存页面引用
    pages={
        "home": home_page
    }
    
    # 当前显示的页面
    current_page="home"
    
    # 设置默认选中首页
    sidebar.set_current_page(current_page)
    
    # 连接侧边栏信号
    def on_menu_clicked(menu_id):
        nonlocal current_page
        if menu_id in pages:
            # 隐藏当前页面
            if current_page in pages:
                pages[current_page].hide()
                pages[current_page].on_hide()
            
            # 显示新页面
            pages[menu_id].show()
            pages[menu_id].on_show()
            current_page=menu_id
            
            # 更新侧边栏选中状态
            sidebar.set_current_page(current_page)
            
            # 更新标题栏标题
            if menu_id == "home":
                header.set_title("首页")
    
    sidebar.menu_clicked.connect(on_menu_clicked)
    
    right_layout.addWidget(main_content,1)  # 1表示占满剩余空间
    
    content_layout.addWidget(right_widget,1)  # 1表示占满剩余空间
    
    main_layout.addWidget(content_widget,1)  # 1表示占满剩余空间
    
    # 设置中央部件
    main_window.setCentralWidget(central_widget)
    main_window.show()
    return main_window