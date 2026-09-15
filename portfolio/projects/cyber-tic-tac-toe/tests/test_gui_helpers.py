import sys
from pathlib import Path

import pytest

# Importing the GUI module should not open a window because main() is guarded.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_gui_module_imports_without_starting_app():
    pytest.importorskip("tkinter")
    import cyber_tic_tac_toe_gui  # noqa: F401
