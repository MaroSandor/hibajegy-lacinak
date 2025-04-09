import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QSortFilterProxyModel

from ui_form import Ui_MainWindow  # A QtCreator által generált UI betöltése

from load_excel import load_excel_data, load_sheet2
from responsive_layout import setup_responsive_layout

class RowFilterProxyModel(QSortFilterProxyModel):
    """ Egyedi proxy model, amely az első oszlop értékei alapján szűri az összes oszlopot. """
    def filterAcceptsRow(self, source_row, source_parent):
        if not self.filterRegularExpression().pattern():
            return True  # Ha nincs keresés, minden sor látható

        model = self.sourceModel()
        index = model.index(source_row, 0, source_parent)  # Első oszlop
        return self.filterRegularExpression().match(model.data(index)).hasMatch()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search_box.setPlaceholderText("Keresés:")
        self.setWindowTitle("Hibajegy kezelő")

        #responsive_layout meghivasa
        setup_responsive_layout(self.ui, self)

        self.tree_views = []  # Az összes QTreeView tárolására
        self.models = []  # Az összes QStandardItemModel tárolására
        self.proxy_models = []  # Az összes QSortFilterProxyModel tárolására
        # Keresőmező esemény összekapcsolása az összes oszlopra
        self.ui.search_box.textChanged.connect(self.apply_filter)

        # Proxy model hozzáadása mindkét munkalaphoz
        self.base_proxy_model = RowFilterProxyModel()
        self.base_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

        self.sheet2_proxy_model = RowFilterProxyModel()
        self.sheet2_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

        # Excel adatok betöltése
        excel_data = load_excel_data("DataBase/Data_2.xlsx")
        self.base_model = excel_data['base_model']
        self.models = excel_data['column_models']

        # Második munkalap betöltése
        self.sheet2_model = load_sheet2("DataBase/Data_2.xlsx", "Munka2")

        # Proxy modellek beállítása
        self.base_proxy_model.setSourceModel(self.base_model)
        self.base_proxy_model.setFilterKeyColumn(0)

        self.sheet2_proxy_model.setSourceModel(self.sheet2_model)
        self.sheet2_proxy_model.setFilterKeyColumn(0)

        # Külön QTreeView modellek beállítása
        for i, model in enumerate(self.models):
            proxy_model = QSortFilterProxyModel()
            proxy_model.setSourceModel(model)
            proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

            tree_view = getattr(self.ui, f"tree_view_{i+1}")
            tree_view.setModel(proxy_model)

            self.tree_views.append(tree_view)
            self.proxy_models.append(proxy_model)

        # A második munkalap QTreeView-ját beállítjuk
        self.ui.tree_view_4.setModel(self.sheet2_proxy_model)

        self.sync_columns()

    def sync_columns(self):
        """ Az első oszlop szűrésének megfelelően frissíti az összes oszlop adatait. """
        self.base_model.layoutChanged.emit()

        # Frissítjük az egyes oszlopokat
        for col_index, model in enumerate(self.models):
            model.clear()
            model.setHorizontalHeaderLabels([self.base_model.headerData(col_index, Qt.Horizontal)])

            for row in range(self.base_proxy_model.rowCount()):
                index = self.base_proxy_model.index(row, col_index)
                item = QStandardItem(self.base_proxy_model.data(index))
                model.appendRow(item)

    def apply_filter(self, text):
        self.base_proxy_model.setFilterFixedString(text)
        self.sheet2_proxy_model.setFilterFixedString(text)
        self.sync_columns()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
