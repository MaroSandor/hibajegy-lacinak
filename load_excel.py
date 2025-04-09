import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

def load_excel_data(file_path):
    """Betölti az Excel fő munkalapját és visszaadja a modelleket"""
    df = pd.read_excel(file_path)
    headers = list(df.columns)
    data = df.values.tolist()

    # Eredeti (nem szűrt) adatmodell létrehozása
    base_model = QStandardItemModel()
    base_model.setColumnCount(len(headers))
    base_model.setHorizontalHeaderLabels(headers)

    # Sorok feltöltése az eredeti modelbe
    for row in data:
        items = [QStandardItem(str(cell)) for cell in row]
        base_model.appendRow(items)

    # Külön modellek az oszlopokhoz
    column_models = []
    for i in range(len(headers)):
        model = QStandardItemModel()
        model.setColumnCount(1)
        model.setHorizontalHeaderLabels([headers[i]])
        column_models.append(model)

    return {
        'base_model': base_model,
        'column_models': column_models,
        'headers': headers
    }

def load_sheet2(file_path, sheet_name):
    """Betölti a második munkalapot és visszaadja a modellt"""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    headers = list(df.columns)
    data = df.values.tolist()

    # Modell létrehozása a második munkalaphoz
    sheet2_model = QStandardItemModel()
    sheet2_model.setColumnCount(len(headers))
    sheet2_model.setHorizontalHeaderLabels(headers)

    for row in data:
        items = [QStandardItem(str(cell)) for cell in row]
        sheet2_model.appendRow(items)

    return sheet2_model
