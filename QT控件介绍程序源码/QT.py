# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

from Ui_QT import Ui_MainWindow
import webbrowser
import time

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
       # time.sleep(1)
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'form', 'QFormLayout 表单就像一个只有两列的表格，非常适合填写注册表单这种类型的界面' )
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'vertical', 'QVerticalLayout 把控件从上到下竖着摆放' )
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'horizontal', 'QHorizontalLayout 把控件从左到右 水平横着摆放' )
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'grid', 'QGridLayout 把多个控件 格子状摆放，有的控件可以 占据多个格子' )

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'vertical', '垂直增加与减少控件之间的间距' )
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'horizontal', '水平增加与减少控件之间的间距' )
    
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'checkbox', '1）控件位置：Buttons->CheckBox\n2）控件介绍：复选框，继承自QButton，与RadioButton的区别是选则模式，单选框提供多选一，复选框提供多选多。\n3）控件属性设置选项：\n（1）name：该控件对应源代码中所显示的名字。\n（2）text：该控件对应图形界面中所显示的名字。\n（3）font：设置text字体。\n（4）enabled：该控件是否可用，可用为true，不可用为false。\n（5）checked：用来设置或返回是否选中单选按钮，选中为true，未选中为false。\n4）常用成员函数：\n（1）QCheckBox：：QCheckBox（const QString &text，QWidget *parent，const char *name = 0）构造一个名称为name、父对象为parent并且文本为text的复选框。\n（2）QCheckBox：：isChecked（）const选中该复选框，返回true，否则返回false。\n（3）void QButton：：setText（const QString &）设置该按钮上显示的文本。\n（4）QString QButton：：text（）const返回该按钮上显示的文本。\n（5）void QButton：：stateChange（int state）[signal]当更改checked属性时，将发射这个信号。\n（6）void QCheckBox：：setChecked（bool check）[槽]设置复选框是否选中，状态为check的值。' )
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'pushbutton', '1）控件位置：Button->PushButton\n2）控件介绍：该控件继承自QButton类，通常用于执行命令或触发事件。\n3）控件属性设置选项：\n（1）name：该控件对应源代码中的名字。\n（2）text：该控件对应图形界面中显示的名字。\n（3）font：设置text的字体。\n（4）enabled：该控件是否可用。\n4）常用成员函数：\n（1）QPushButton：：QPushButton（const QString &text，QWidget *parent，const char *name = 0）；构造一个名称为name，父对象为parent并且文本为text的推动按钮。\n（2）void QButton：：pressed（）[信号]当按下该按钮时发射信号。\n（3）void QButton：：clicked（）[信号]当单击该按钮时发射信号。\n（4）void QButton：：released（）[信号]当释放该按钮时，发射信号。\n（5）void QButton：：setText（const QString &）设置该按钮上显示的文本。\n（6）QString QButton：：text（）const' )

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'radio', '1）控件位置：Buttons->RadioButton\n2）控件介绍：单选框，继承自QButton类，通常成组出现，用于提供两个或多个互斥选项。\n3）控件属性设置选项：\n（1）name：该控件对应源代码中所显示的名字。\n（2）text：该控件对应图形界面中所显示的名字。\n（3）font：设置text字体。\n（4）enabled：该控件是否可用，可用为true，不可用为false。\n（5）checked：用来设置或返回是否选中单选按钮，选中为true，未选中为false。\n4）常用成员函数：\n（1）QRaidoButton：：QRadioButton（const QString &text，QWidget *parent，const char *name = 0）构造一个名称为name、父对象为parent并且文本为text的单选按钮。\n（2）bool QRadioButton：：isChecked（）const返回是否选中单选按钮，选中时返回true，没有选中时返回false。\n（3）void QButton：：setText（const QString &）设置该按钮上显示的文本。\n（4）QString QButton：：text（）const返回该按钮上显示的文本。\n（5）void QButton：：stateChanged（int state）[signal]当更改checked属性值时，将发射信号。\n（6）void QRadioButton：：setChecked（bool check）[virtual slot]设置单选按钮是否被选中为check。' )
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self, 'tool', '1）控件位置：Buttons->ToolButton\n2）控件介绍：工具按钮，继承自QButton类，是一种用于命令或者选项的可以快速访问的按钮，通常在ToolBar里面。工具按钮通常显示的是图标，而不是文本标签。ToolButton支持自动浮起。在自动浮起模式中，按钮只有在鼠标指向它的时候才绘制三维的框架。\n3）控件设置选项：\n（1）name：该控件对应源代码中的名称。\n（2）text：工具按钮标签文本。\n（3）font：设置工具按钮标签的字体。\n（4）autoRaise：自动浮起是否生效。\n（5）iconSet：提供显示在按钮上的图标的图标集。\n（6）on：工具按钮是否为开。\n（7）textLabel：工具按钮自动提示文本。\n（8）usesTextLabel：自动提示文本textLabel是否工作，默认为false。' )
        my_button=QMessageBox.about(self,'tool补充','4）常用成员函数：\n（1）QToolButton：：QToolButton（QWidget *parent，const char *name = 0）构造一个名字为name，父对象为parent的ToolButton。\n（2）QToolButton：：QToolButton（const QIconset &iconSet，const QString &textLabel，const QString &grouptext，QObject *receiver，const char *slot，QToolBar *parent，const char *name = 0）构造一个名称为name，父对象为parent（必须为QToolBar）的工具按钮。工具按钮将显示iconSet，工具提示为textLabel，状态条信息为grouptext，同时会将工具按钮链接到receiver对象的槽函数。\n（3）QToolBButton：：QToolButton（ArrowType type，QWidget *parent，const char *name = 0）此构造函数是把工具按钮构造成箭头按钮，type定义了箭头的方向，可用的值有LeftArrow、RightArrow、UpArrow、DownArrow。\n（4）void QToolButton：：setAutoRaise（bool enable）根据参数enable值设置按钮是否可自动浮起。\n（5）void QToolButton：：setIcon（const QIconSet &）设置显示在工具按钮上的图标。\n（6）void QToolButton：：setOn（bool enable）[虚槽]设置按钮是否为开，enable等于true则设置为开，否则设置为关。\n（7）void QToolButton：：setTextLabel（const QString &）[槽]设置按钮的提示标签。\n（8）QString QToolButton：：textLabel（）const返回按钮的提示标签。')
    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'commandlink','1）控件位置：Buttons->CommandLinkButton\n2）控件介绍：命令链接按钮，继承自QPushButton，用于在互斥选项中选择一项，CommandLinkButton除带有正常的按钮上的文字描述文本外，默认情况下，它也将携带一个箭头图标，表明按下按钮将打开另一个窗口或页面。\n3）控件属性设置选项：\n（1）name：该控件对应源代码中的名称。\n（2）text：该控件对应图形界面中所显示的标签。\n（3）font：设置text的字体。\n（4）enabled：该控件是否可用。\n（5）description：一个描述性的标签，以配合按钮上的文字。')
        my_button=QMessageBox.about(self,'commandlink补充','4）常用成员函数：\n（1）QCommandLinkButton：：QCommandLinkButton（QWidget *parent = 0）构造一个父对象为parent的命令链接按钮。\n（2）QCommandLinkButton：：QCommandLinkButton（const QString &text，QWidget *parent = 0）构造一个父对象为parent、文本为text的命令链接按钮。\n（3）QCommandLinkButton：：QCommandLinkButton（const QString &text，const QString &description，QWidget *parent = 0）构造一个父对象为parent、文本为text和描述文本为description的命令链接按钮。\n（4）void QButton：：clicked（）[信号]当单击该按钮时，发射信号。\n（5）void QButton：：pressed（）[信号]当按下该按钮时，发射这个信号。\n（6）void QButton：：released（）[信号]当释放该按钮时，发射这个信号。\n（7）void QButton：：setText（const QString &）设置改按钮上显示的文本。\n（8）QString QButton：：text（）cosnt返回按钮上显示的文本。')
    @pyqtSlot()
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'buttonbox','1）控件位置：Buttons->ButtonBox\n2）控件介绍：按钮键，室友QDialogButtonBox类包装成的。\n3）控件属性设置选项：\n（1）name：该控件对应源代码中的名称。\n（2）font：设置text的字体。\n（3）enabled：该控件是否可用。\n（4）centerButtons：ButtonBox中的按钮是否居中布局，默认值为false。\n（5）orientation：按钮布局方向，Qt提供QT：：Horizontal和QT：：Vertical两种。\n（6）standardButtons：标准按钮集合。')
        my_button=QMessageBox.about(self,'buttonbox补充','4）常用成员函数：\n（1）QDialogButtonBox：：QDialogButtonBox（QWidget *parent = 0）构造一个按钮盒，父对象为parent。\n（2）QDialogButtonBox：：QDialogButtonBox（QT：：Orientation orientation，QWidget *parent = 0）构造一个按钮盒，父对象为parent，排列方向为orientation，并且包含buttons。\n（3）QDialogButtonBox：：QDialogButtonBox（StandardButton buttons，QT：：Orientation orientation = QT：：Horizontal，QWidget *parent = 0）构造一个按钮盒，父对象为parent，排列方向为orientation。\n（4）void QDialogButtonBox：：accepted（）[signal]当单击按钮盒里的定义为AcceptRole和YesRole的按钮时，发射信号。\n（5）void QDialogButtonBox：：addButton（QAbstractButton *button，ButtonRole role）向按钮盒里添加按钮button，定义按钮button的角色为role，如果role是无效的，则不添加按钮，如果按钮已添加，移除并在次添加为新角色。\n（6）QPushButton *QDialogButtonBox：：addButton（StandarButton button）向按钮盒中添加一个标准按钮button，并返回标准按钮。如果按钮无效，不添加，返回0.')
        my_button=QMessageBox.about(self,'buttonbox函数补充','（7）QPushButton *QDialogButtonBox：：addButton（const QString &text，ButtonRole role）创建一个按钮的文本为text，以指定角色添加到按钮盒，并返回相应的按钮，如果role是无效的，则不创建，返回0.\n（8）void QDialogButtonBox：：clear（）清空该按钮盒里的所有按钮。\n（9）void QDialogButtonBox：：clicked（QAbstractButton *button）[signal]当单击按钮盒里的按钮button时，发射这个信号。\n（10）void QDialogButtonBox：：helpRequested（）[signal]当单击按钮盒里的定义为HelpRole的按钮时，发射这个信号。\n（11）void QDialogButtonBox：：rejected（）[signal]当单击按钮盒里定义为RejectRole和NoRole的按钮时，发射这个信号。\n（12）void QDialogButtonBox：：removeButton（QAbstractButton *button）移除按钮盒里的按钮Button，但是不删除，设置它的父母为0.')
    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'undo','撤销视图控件')
    @pyqtSlot()
    def on_pushButton_19_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'column','1.控件位置：Item View->ColumnView\n2.控件介绍：列视图\n3.控件属性设置选项：\n（1）name：该控件对应源代码中的名字\n（2）font：设置表格内部的字体')
        my_button=QMessageBox.about(self,'column补充','4.常用成员函数\n（1）QColumnView：：QColumnView（QWidget *parent = 0）构造一个父对象为parent的ColumnView\n（2）QAbstractItemView * QColumnView：：createColumn（const QModelIndex *index）[virtual protected]index是视图的根模型索引，返回新的视图\n（3）void QColumnView：：currentChanged（const QModelIndex &current，const QModelIndex &previous）[virtual protected]把current指定为当前项目，previous是以前的当前项目\n（4）QModelIndex QColumnView：：indexAt（cosnt QPoint &point）const [virtual]返回点pos处项目的索引模型\n（5）QWidget *QColumnView：：previewWidget（）const返回预览组件，如果没有则返回0\n（6）void QColumnView：：rowsInserted（const QModelIndex &parent，int start，int end）[virtual protected]插入新行，新行的父母是parent包括从start到end的所有项目\n（7）void QColumnView：：selectAll（）[virtual]设置该ColumnView中的所有项目为选中状态\n（8）void QColumnView：：setPreviewWidget（QWidget *widget）设置widget为该columnView的预览组件。')
    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'tree','1.控件位置：Item View->TreeView\n2.控件介绍：树形视图，继承自QAbstractItemView，是基于模型的列表/图标视图，也是Qt模型/视图框架的一部分。\n3.控件属性设置选项：\n（1）name：该控件对应源代码中的名称。\n（2）font：设置该控件内所有文本的字体。\n（3）sortingEnable：项目是否排序。')
        my_button=QMessageBox.about(self,'tree补充','4.常用成员函数：\n（1）QTreeView：：QTreeView（QWidget *parent = 0）构造一个父对象为parent的TreeView。\n（2）void QTreeView：：collapse（const QModena &index）[slot]折叠模型索引为index的项目\n（3）void QTreeView：：collapseAll（）[slot]折叠所有项目\n（4）int QTreeView：：columnAt（int x）const返回x坐标处的列。\n（5）void QTreeView：：columnCountChanged（int oldCount，int newCount）[protected slot]通知树形视图中的列数，从oldCount改变到newCount。\n（6）void QTreeView：：currentChanged（const QModelIndex &current，const QModelIndex &previous）[virtual protected]把current定为当前项目，previous是以前的当前项目')
        my_button=QMessageBox.about(self,'tree函数补充','（7）void QTreeView：：dataChanged（const QModelIndex &topLeft，const QModelIndex &bottomRight）[virtual]更改模型中项目topLeft到bottomRight。\n（8）void QTreeView：：drawBranches（QPainter *painter，const QRect &rect，const QModelIndex &index）const [virtual protected[在项目index的同一行，用painter绘制指定的rect矩形分支。\n（9）void QTreeView：：drawRow（QPainter *painter，const QStyleOptionViewItem &option，const QModelIndex &index）const [virtual protected]用painter绘制新行，新行包含模型索引 为index的项目，option是如何显示项目。\n（10）void QTreeView：：drawTree（QPainter *painter，const QRegion &region）const [protected]用painter在区域region绘制树\n（11）void QTreeView：：expand（const QModelIndex &index）[slot]展开模型索引为index的项目。\n（12）void QTreeView：：expandAll（）[slot]展开所有的项目')
        my_button=QMessageBox.about(self,'tree函数补充','（13）void QTreeView：：expandToDepth(int depth) [slot]展开树形视图中的项目，深度为depth\n（14）QHeaderView *QTreeView：：header（）const返回该树形视图的header\n（15）QModelIndex QTreeView：：indexAbove（const QModelIndex &index）const返回模型索引index的上一个索引\n（16）QModelIndex QTreeView：：indexAt（const QPoint &point）const [virtual]返回点point处项目的模型索引\n（17）QModelIndex QTreeView：：indexBelow（const QModelIndex &index）const\n返回模型索引index的下一个索引\n（18）bool QTreeView：：isExpanded（const QModelIndex &index）const如果模型索引index处的项目是展开着的，返回true，否则返回false\n（19）void QTreeV：：rowsInserted（const QModelIndex &parent，int start，int end）[virtual protected]插入新行，新行的父母是parent，包括从start到end的所有项目。')
        my_button=QMessageBox.about(self,'tree函数补充','（20）void QTreeView：：rowsRemoved（const QModelIndex &parent，int start，int end）[protected slot]删除行，行的父母是parent，包括从start到end的所有项目\n（21）void QTreeView：：selectAll（）[virtual]设置所有的项目都是选择状态\n（22）QModelIndexList QTreeView：：selectedIndexes（）const [virtual protected]返回所有选中和非隐藏的项目的模型索引\n（23）void QTreeView：：setHeader（QHeaderView *header）设置该TreeView的标题为header\n（24）void QTreeView：：sortByColumn（int column，QT：：SortOrder order）对列column按order进行排序')
    @pyqtSlot()
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'list','1.控件位置：Item Views->ListView\n2.控件介绍：列表视图，继承自QAbstractItemView。ListView是基于模型的列表/图标视图，为Qt的模型/视图结构提供了更灵活的方式。\n3.控件属性设置：\n（1）name：该控件对应源代码中的名称。\n（2）font：设置视图内字体。\n（3）batchSize：如果将layoutMode设置为Batched，则这个属性保存批量处理的规格。\n（4）layoutModel：项目的布局模式。\n（5）modeColumn：模型中可见的类，默认情况下，置为0，表述模型中第一列可见。\n（6）viewModel：保存该ListView的视图模型。')
        my_button=QMessageBox.about(self,'list补充','4.常用成员函数：\n（1）QListView：：QListView（QWidget *parent = 0）构造一个父对象为parent的ListView。\n（2）void QListView：：currentChanged（const QModelIndex &current，const QModelIndex &previous）[virtual protected]把current定位当前项目，previous是以前的项目。\n（3）void QListView：：dataChanged（const QModelIndex &topLeft，const QModelIndex &bottomRight）[virtual protected]更改模型中项目topLeft到bottomRight。\n（4）QModelIndex QListView：：indexAt（const QPoint &p）const [virtual]返回坐标点p处项目的模型索引。\n（5）void QListView：：rowsInserted（const QModelIndex &parent，int start，int end）[virtual protected]插入新行，新行的父母是parent，从start到end的所有项目。\n（6）QModelIndexList QListView：：selectedIndexes（）const[virtual protected]返回所有选中的非隐藏的项目的模型索引。')
    @pyqtSlot()
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'table','1.控件位置：Item View->TableView\n2.控件介绍：表格视图，是一个模型/视图结构的表视图实现，用来显示模型的项目。它提供了QTable类提供的标准表格。是Qt的模型/视图框架的一部分。由QAbstractItemView类定义的接口来实现，使其能够显示由QAbstractItemModel类派生的模型提供的数据。\n3.控件属性设置选项：\n（1）name：该控件对应源代码中的名称\n（2）font：设置表格内部的字体\n（3）cornerButtonEnabled：左上角的按钮是否有用\n（4）gridStyle：表格的格式\n（5）showGrid：是否显示网格，值为true，显示，否则不显示\n（6）sortingEnabled：是否对项目排序')    
        my_button=QMessageBox.about(self,'table补充','4.常用成员函数\n（1）QTableView：：QTableView（QWidget *parent = 0）构造一个父对象为parent的TableView\n（2）void QTableView：：clearSpans（）删除该TableView中的所有行和列的跨度\n（3）int QTableView：：columnAt（int x）const返回坐标x处的列，如果坐标处没有项目则返回-1\n（4）int QTableView：：columnSpan（int row，intcolumn）const\n返回行row、列column处的行跨度\n（5）void QTableView：：currentChanged（const QModelIndex &current，const QModelIndex &previous）[virtual protected]把current指定为当前项目，previous是以前的项目\n（6）QHeaderView *QTableView：：horizontalHeader（）const返回该TableView的水平标题')
        my_button=QMessageBox.about(self,'table函数补充','（7）QModelIndex QTableView：：indexAt（const QPoint *pos）const [virtual]返回点pos处项目的模型索引\n（8）int QTableView：：rowAt（int y）const返回坐标y处的行，如果坐标处没有项目则返回-1\n（9）int QTableView：：rowSpan（int row，int column）const返回行row、列column处的列跨度\n（10）void QTableView：：selectcolumn（int column）[slot]设置列column为选中状态\n（11）void QTableView：：selectRow（int row）[slot]设置行row为选中状态\n（12）QModelIndexList QTableView：：selectedIndexes（）const [virtual protected]返回所有选中和非隐藏的项目的模型索引\n（13）void QTableView：：setHorizontalHeader（QHeaderView *header）设置该TableView的水平标题为header\n（14）void QTableView：：setSpan（int row，int column，int rowSpanCount，int columnCount）设置行row、列column处的行跨度为rowSpanCount、列跨度为columnSpanCount\n（15）void QTableView：：setVerticalHeader（QHeaderView *header）设置该TableView的垂直标题为header\n（16）void QTableView：：showColumn（int column）[slot]显示列column\n（17）void QTableView：：showRow（int row）[slot]显示行row\n（18）QHeaderView *QTableView：：verticalHeader（）const返回TableView的垂直标题')
    @pyqtSlot()
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'list','1.控件位置：Item Widget->ListWidget\n2.控件介绍：ListWidget继承自QListView类，基于Item的列表控件。\n3.控件属性设置选项：\n（1）name：该控件对应源代码内的名称\n（2）font：设置该表格内部的字体\n（3）count：保持项目的数目\n（4）currentRow：保持当前项目的行\n（5）sortingEnabled：是否对item排序')
        my_button=QMessageBox.about(self,'list补充','4.常用成员函数：\n（1）QListWidget：：QListWidget（QWidget *parent = 0）构造父对象为parent的ListWidget\n（2）void QListWidget：：addItem（QListWidgetItem *item）添加项目item\n（3）void QListWidget：：addItem（const QString &label）\n添加一个新的项目，在新添加的项目中添加label标签\n（4）void QListWidget：：addItems（const QStringList &labels）添加一列项目\n（5）void QListWidget：：clear（）[slot]\n清除该ListWidget中的所有项目\n（6）QListWidgetItem *QListWidget：：currentItem（）const返回当前活动的项目')
        my_button=QMessageBox.about(self,'list函数补充','（7）void QListWidget：：editItem（QListWidgetItem *item）如果项目item是可编辑的，开始编辑项目item\n（8）QList<QListWidgetItem *>QListWidget：：findItems（const QString &text，Qt：：MatchFlags flags）const查找匹配字符串text的项目，并返回查找结果\n（9）void QListWidget：：insertItem（int row，QListWidgetItem * item）在行row处插入项目item\n（10）void QListWidget：：insertItem（int row，const QString &label）这是一个重载函数，功能同（9），在行row处插入标签为label的新项目\n（11）void QListWidget：：insertItem（int row，const QStringList &labels）\n在行row处插入一列项目\n（12）QListWidgetItem *QListWidget：：item（int row）const\n返回行row处的项目，如果行row处没有项目则返回0\n（13）QListWidgetItem *QListWidget：：itemAt（const QPoint &p）const返回点p处的项目\n（14）QListWidgetItem *QListWidget：：itemAt（int row，int y）const返回坐标（x，y）处的项目\n（15）QWidget *QListWidget：：itemWidget（QListWidgetItem *item）const返回项目item处显示的控件\n（16）QListWidgetItem *QListWidget：：takeItem（int row）移除行row处的项目，并返回项目控件')
        my_button=QMessageBox.about(self,'list函数补充','（17）void QListWidget：：removeItemWidget（QListWidgetItem *item）移除项目item处的控件\n（18）int QListWidget：：row（const QListWidgetItem *item）cosnt返回项目item所在的行\n（19）QList<QListWidgetItem*> QListWidget：：selectedItems（）const返回所有被选中的项目的控件\n（20）void QListWidget：：setcurrentItem（QListWidgetItem *item）设置项目item为当前项目\n（21）void QListWidget：：setItemWidget（QListWidgetItem *item，QWidget *widget）设置控件widget为项目item的显示控件\n（22）void QListWidget：：setItemWidget（QListWidgetItem *item，QWidget *widget）\n（23）void QListWidget：：sortItems（Qt：：SortOrder order = Qt：：AscendingOrder）把项目按照order进行排序')
    @pyqtSlot()
    def on_pushButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'table','1.控件位置：Item Widget->Table Widget\n2.控件介绍：表格单元控件\n3.控件属性设置选项：\n（1）name：同上\n（2）font：同上\n（3）columnCount：保存列的数目\n（4）rowCount：保存行的数目')  
        my_button=QMessageBox.about(self,'table补充','4.常用成员函数\n（1）QTableWidget：：QTableWidget（QWidget * parent = 0）构造一个父对象为parent的TableWidget\n（2）QTableWidget：：QTableWidget（int rows，int columns，QWidget *parent = 0）构造一个rows行，columns列，父对象为parent的TableWidget控件\n（3）QWidget *QTableWidget：：cellWidget（int row，int column）const返回行row，列column的单元格处的控件\n（4）void QTableWidget：：clear（）[slot]删除该TreeWidget中的所有项目\n（5）void QTableWidget：：clearContents（）[slot]删除该TreeWidget中除了header外的所有项目\n（6）int QTableWidget：：column（const QTableWidgetItem *item）const返回项目item所在的列')
        my_button=QMessageBox.about(self,'table函数补充','（7）int QTableWidget：：currentColumn（）const返回当前活动的列\n（8）QTableWidgetItem *QTableWidget：：currentItem（）const返回当前活动的项目\n（9）int QTableWidget：：currentRow（）const返回当前活动的行\n（10）void QTableWidget：：editItem（QTableWidgetItem *item）\n如果item是可编辑的，开始编辑item\n（11）QList<QTableWidgetItem *> QTableWidget：：findItems（const QString &text，Qt：：MatchFlags flags）const查找匹配字符串text的项目，并返回查找结果\n（12）void QTableWidget：：insertColumn（int column）[slot]在列column处插入新列\n（13）void QTableWidget：：insertRow（int row）[slot]在行row处插入新行\n（14）QTableWidgetItem *QTableWidget：：item（int row，int column）const返回行row、列column处的项目\n（15）QTableWidgetItem *QTableWidget：：itemAt（const QPoint &point）const返回点point处的项目\n（16）QTableWidgetItem *QTableWidget：：itemAt（int ax，int ay）const返回坐标（ax，ay）处的项目\n（17）void QTableWidget：：removeCellWidget（int row，int column）移除行row、列column单元格处的显示控件\n（18）void QTableWidget：：removeColumn（int column）[slot]移除列column\n（19）void QTableWidget：：removerRow（int row）[slot]移除行row')
        my_button=QMessageBox.about(self,'table函数补充','（20）int QTableWidget：：row（const QTableWidgetItem *item）cosnt返回item的行\n（21）QList<QTableWidgetItem *> QTableWidget：：selectedItems（）返回所有选中状态的项目\n（22）void QTableWidget：：setCellWidget（int row，int column，QWidget *widget）设置行row、列column处的显示控件为widget。\n（23）void QTableWidget：：setCurrentCell（int row，int column）设置行row，列column处的单元格为当前活动单元格\n（24）void QTableWidget：：setCurrentItem（QTableWidgetItem *item）设置项目item为当前活动项目\n（25）void QTableWidget：：setHorizontalHeaderItem（int column，QTableWidgetItem *item）设置项目item为列column的水平头项目，功能同setVerticalHeaderItem（）\n（26）void QTableWidget：：setHorizontalHeaderLabels（const QStringList *labels）设置水平标题为labels，功能同setVerticalHeaderLabels（）')
        my_button=QMessageBox.about(self,'table函数补充','\n（27）void QTableWidget：：setItem（int row，int column，QTableWidgetItem *item）\n设置行row、列column的单元格的项目为item\n（28）void QTableWidget：：sortItems（int column，Qt：：SortOrder order = Qt：：AscendingOrder）对列column按照order进行排序\n（29）QTableWidgetItem *QTableWidget：：takeHorizonalHeaderItem（int column）移除列column的水平头项目，功能同takeVerticalHeaderItem（）\n（30）QTableWidgetItem *QTableWidget：：takeItem（int row，int column）移除行row、列column单元格处的项目\n（31）QTableWidgetItem *QTableWidget：：verticalHeaderItem（int row）const返回行row的垂直头项目')
    @pyqtSlot()
    def on_pushButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'tree','1.控件位置：Item Widget->TreeWidget\n2.控件介绍：树形单元控件，继承自QTreeView类，是树形视图使用预定义的模型，他也是基于模型/视图结构的控件，为方便开发人员使用树形视图，可以使用这个控件来创建简单地树形结构列表\n3.控件属性设置选项：\n（1）name：同上\n（2）font：同上\n（3）columnCount：保存该TreeWidget的列数')
        my_button=QMessageBox.about(self,'tree补充','4.常用成员函数\n（1）QTreeWidget：：QTreeWidget（QWidget *parent = 0）构造一个父对象为parent的TreeWidget\n（2）void QTreeWidget：：addTopLevelItem（QTreeWidgetItem * item）在该TreeWidget中追加item为顶级项目\n（3）void QTreeWidget：：addTopLevelItems（const QList<QTreeWidgetItem*> &items）把items中的项目作为顶级项目追加到该TreeWidget中\n（4）void QTreeWidget：：clear（）[slot]清除该TreeWidget中的所有项目\n（5）void QTreeWidget：：collapseItem（const QTreeWidgetItem *item）[slot]折叠项目item\n（6）int QTreeWidget：：currentColumn（）const返回当前活动列')
        my_button=QMessageBox.about(self,'tree函数补充','（7）QTreeWidgetItem *QTreeWidget：：currentItem（）const返回当前活动项目\n（8）void QTreeWidget：：editItem（QTreeWidgetItem *item，int column = 0）如果列column的item是可编辑的，开始编辑\n（9）void QTreeWidget：：expandItem（const QTreeWidgetItem *item）[slot]展开项目\n（10）QList<QTreeWidgetItem*> QTreeWidget：：findItems（const QString &text，Qt：：MatchFlags flags，int column = 0）const查找匹配字符串的text的项目，并返回查找结果\n（11）QTreeWidgetItem *QTreeWidget：：headerItem（）const返回头项目\n（12）QModelIndex QTreeWidget：：indexFromItem（QTreeWidgetItem *item，int column = 0）const [protected]返回列column的项目item模型索引\n（13）int QTreeWidget：：indexOfTopLevelItem（QTreeWidgetItem *item）const返回顶级项目item的模型索引，如果item不存在返回-1\n（14）int QTreeWidget：：sortColumn（）const返回排序的列\n（15）void QTreeWidget：：sortItems（int column，Qt：：SortOrder order）对列column的项目按照order进行排序\n（16）QTreeWidgetItem *QTreeWidget：：itemAbove（const QTreeWidgetItem *item）const返回item的上一个项目\n（17）QTreeWidgetItem *QTreeWidget：：itemAt（const QPoint &p） const返回点p处的项目')
        my_button=QMessageBox.about(self,'tree函数补充','（18）QTreeWidgetItem *QTreeWidget：：itemAt（int x，int y）const返回坐标（x，y）处的项目\n（19）void QTreeWidget：：setItemWidget（QTreeWidgetItem *item，int column，QWidget *widget）设置控件widget为项目item的显示控件，项目item在列column中\n（20）QTreeWidgetItem *QTreeWidget：：itemBelow（const QTreeWidgetItem *item）const返回item的下一个项目\n（21）QWidget *QTreeWidget：：itemWidget（QTreeWidgetItem *item，int column）const返回列column中的项目item显示控件\n（22）void QTreeWidget：：removeItemWidget（QTreeWidgetItem *item，int column）移除列column中的项目item的显示控件\n（23）QList<QTreeWidgetItem *> QTreeWidget：：selectItems（）const返回所有选中状态的项目\n（24）void QTreeWidget：：setCurrentItem（QTreeWidgetItem *item）设置item为当前项目\n（25）void QTreeWidget：：setCurrentItem（QTreeWidgetItem *item，int column）设置列column的项目item为当前项目\n（26）void QTreeWidget；：setHeaderItem（QTreeWidgetItem *item）设置item为该TreeWidget的头项目\n（27）void QTreeWidget：：setHeaderLabel（const QString &label）设置label为头标题\n（28）QTreeWidgetItem *QTreeWidget：：topLevelItem（int index）cosnt返回所有index的顶级项目')
    @pyqtSlot()
    def on_commandLinkButton_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=webbrowser.open('https://blog.csdn.net/yuxikuo_1/article/details/17455063?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158780667219724845012123%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=158780667219724845012123&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v25-3')
    @pyqtSlot()
    def on_commandLinkButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=webbrowser.open('https://blog.csdn.net/yuxikuo_1/article/details/17488975?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158780667219724845012123%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=158780667219724845012123&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v25-2')
    @pyqtSlot()
    def on_commandLinkButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        my_button=webbrowser.open('https://blog.csdn.net/yuxikuo_1/article/details/17501649?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158780667219724845012123%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=158780667219724845012123&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v25-4')
    @pyqtSlot()
    def on_actionjdl_triggered(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'帮助','关于这个软件的使用十分简单哪里能点，点哪里，因为容器、输入组件与显示组件的介绍内容太多了，我懒得复制粘贴了，所以我加上了网址，其中按钮点了没用')
    @pyqtSlot()
    def on_actionlianxi_triggered(self):
        """
        Slot documentation goes here.
        """
        my_button=QMessageBox.about(self,'联系','我的手机号是13171654043\n微信可以用手机号搜到\nQQ是3185769956\n以下联系方式供可以翻墙的人使用：\nfacebook:+8613171654043\ntwitter:@k9SC5cw0YmSNsrZ')

















   



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('1001370.png'))
    splash=QSplashScreen(QtGui.QPixmap(":/K/1001370.jpg"))
    splash.show()
    splash.setFont(QtGui.QFont('楷体', 36))
    splash.showMessage('正在加载程序...',Qt.AlignCenter,Qt.blue)
   # time.sleep(1)
    app.processEvents()
    ui = MainWindow()
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
    
   