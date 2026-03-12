# tests/test_fixtures.py
"""
Validation suite for synthetic test data builders.
"""

from pathlib import Path

def test_synthetic_pdf_generation(structured_pdf_path: Path) -> None:
    """
    Validates that the pytest fixture successfully compiled the PDF byte stream
    and committed it to non-volatile storage.

    Args:
        structured_pdf_path (Path): Injected path from the pytest fixture.
    """
    assert structured_pdf_path.exists(), "The PDF file was not written to disk."
    assert structured_pdf_path.stat().st_size > 0, "The generated PDF byte stream is empty."
