from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QSplitter,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow


from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QSplitter,
    QWidget, QSpacerItem, QSizePolicy, QFrame
)
from PySide6.QtCore import Qt

def setup_responsive_layout(ui, main_window):
    """Reszponzív elrendezés 4 gombbal"""
    # 1. Eltávolítjuk az eredeti centralwidget-et
    old_central = ui.centralwidget
    old_central.setParent(None)

    # 2. Fő keret létrehozása
    main_frame = QFrame()
    main_layout = QHBoxLayout(main_frame)
    main_layout.setContentsMargins(5, 5, 5, 5)
    main_layout.setSpacing(10)

    # 3. Bal oldali keret (csak graphicsView)
    left_frame = QFrame()
    left_layout = QVBoxLayout(left_frame)
    left_layout.setContentsMargins(0, 0, 0, 0)


    # 4. Jobb oldali keret (kereső, fák, gombok)
    right_frame = QFrame()
    right_layout = QVBoxLayout(right_frame)
    right_layout.setContentsMargins(5, 5, 5, 5)
    right_layout.setSpacing(8)

    # Keresőmező
    right_layout.addWidget(ui.search_box)

    # TreeView-ek
    trees_container = QFrame()
    trees_layout = QHBoxLayout(trees_container)
    trees_layout.setContentsMargins(0, 0, 0, 0)
    trees_layout.setSpacing(10)

    # Bal oldali fák (függőlegesen)
    left_trees = QSplitter(Qt.Vertical)
    left_trees.addWidget(ui.tree_view_1)
    left_trees.addWidget(ui.tree_view_2)
    left_trees.addWidget(ui.tree_view_3)
    trees_layout.addWidget(left_trees, 2)  # 2/3 arány

    # Jobb oldali fa
    trees_layout.addWidget(ui.tree_view_4, 1)  # 1/3 arány

    right_layout.addWidget(trees_container)

    # Gombok alul - most már 4 gombbal
    button_frame = QFrame()
    button_layout = QHBoxLayout(button_frame)
    button_layout.setContentsMargins(0, 5, 0, 0)
    button_layout.setSpacing(8)

    # Mind a 4 gomb hozzáadása
    button_layout.addWidget(ui.pushButton)
    button_layout.addWidget(ui.pushButton_2)
    button_layout.addWidget(ui.pushButton_3)
    button_layout.addWidget(ui.pushButton_4)

    # Rugalmas tér a gombok után
    button_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    right_layout.addWidget(button_frame)

    # 5. Fő elrendezés - Splitter használata
    main_splitter = QSplitter(Qt.Horizontal)
    main_splitter.addWidget(left_frame)
    main_splitter.addWidget(right_frame)
    main_splitter.setSizes([400, 400])  # Kezdeti méretek

    # Splitter nem csukható össze teljesen
    main_splitter.setCollapsible(0, False)
    main_splitter.setCollapsible(1, False)

    main_layout.addWidget(main_splitter)

    # 6. Méretkorlátozások
    main_window.setCentralWidget(main_frame)
    left_trees.setSizes([200, 200, 200])  # Fák kezdeti mérete

    # 7. Stretch faktorok
    main_layout.setStretch(0, 1)  # Bal oldal
    main_layout.setStretch(1, 1)  # Jobb oldal
 # 7. Stílusbeállítások
    main_window.setStyleSheet("""
        QPushButton {
            min-width: 120px;
            max-width: 200px;
            min-height: 45px;
            padding: 5px;
            font-size: 12px;
            background-color: #80DEEA;
        }
        QFrame {
            background-color: #FFFFFF;
            border-radius: 3px;
        }
        QTreeView {
            font-size: 12px;
            background-color: #FFFFFF;
            min-width: 248px;
        }
        QLineEdit {
            padding: 5px;
            background-color: #FFFFFF;
        }

        QGraphicsView {
        min-width: 248px;
        max-width: 1,240px;
        min-height: 350,8px;
        max-heightL 1704px;

        }
    """)

