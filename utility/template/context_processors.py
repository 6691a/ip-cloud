from dataclasses import dataclass


@dataclass
class ToastLevel:
    INFO: str = "info"
    SUCCESS: str = "success"
    WARNING: str = "warning"
    ERROR: str = "error"


@dataclass
class ToastPosition:
    TOP_CENTER: str = "toast-top-center"
    TOP_FULL: str = "toast-top-full-width"
    TOP_RIGHT: str = "toast-top-right"
    TOP_LEFT: str = "toast-top-left"
    BOTTOM_RIGHT: str = "toast-bottom-right"
    BOTTOM_LEFT: str = "toast-bottom-left"
    BOTTOM_CENTER: str = "toast-bottom-center"
    BOTTOM_FULL: str = "toast-bottom-full-width"


@dataclass
class ToastTag:
    level: str = ToastLevel.INFO
    position: str = ToastPosition.TOP_FULL
    close: bool = True

    def __str__(self):
        return f"{self.level}_{self.position}_{self.close}"
