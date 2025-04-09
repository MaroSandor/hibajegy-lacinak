from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class logo_iamge:
    _pixmap = None

    @classmethod
    def load(cls, eleresi_ut):
        """Egyszeri betöltés a memóriába"""
        if cls._pixmap is None:
            cls._pixmap = QPixmap(eleresi_ut)
            if cls._pixmap.isNull():
                print(f"Hiba: A logo nem tölthető be: {eleresi_ut}")
                return False
        return True

    @classmethod
    def meretezett_logo(cls, width=None, height=None):
        """Méretezett változat visszaadása"""
        if cls._pixmap is None:
            return None

        pixmap = cls._pixmap
        if width and height:
            return pixmap.scaled(
                width,
                height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        elif width:
            return pixmap.scaledToWidth(
                width,
                Qt.TransformationMode.SmoothTransformation
            )
        elif height:
            return pixmap.scaledToHeight(
                height,
                Qt.TransformationMode.SmoothTransformation
            )
        return pixmap