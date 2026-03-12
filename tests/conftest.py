# tests/conftest.py
"""
Centralized Test Configuration and Dependency Injection (Fixtures).
Allocates deterministic state objects to isolate tests from unpredictable I/O.
"""

import pytest
import fitz  # type: ignore
from pathlib import Path

# Resolve absolute path to the fixtures directory
FIXTURE_DIR = Path(__file__).parent / "fixtures"

@pytest.fixture(scope="session")
def structured_pdf_path() -> Path:
    """
    Allocates a PDF document in the C-heap and constructs a logical Outline (AST).
    Saves the physical artifact to disk for visual inspection and unit testing.

    Returns:
        Path: The absolute filesystem path to the generated PDF.
    """
    FIXTURE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = FIXTURE_DIR / "structured_book.pdf"

    # Allocate PDF struct
    doc = fitz.open()

    # Construct pages via Cartesian absolute coordinates
    page0 = doc.new_page()
    page0.insert_text(fitz.Point(72, 72), "Title Page", fontsize=24)

    page1 = doc.new_page()
    page1.insert_text(fitz.Point(72, 72), "Chapter 1: The Vector Space", fontsize=20)
    page1.insert_text(fitz.Point(72, 120), "Content for chapter 1...", fontsize=12)

    page2 = doc.new_page()
    page2.insert_text(fitz.Point(72, 72), "Chapter 2: Manifold Topology", fontsize=20)
    page2.insert_text(fitz.Point(72, 120), "Content for chapter 2...", fontsize=12)

    # Define the AST Outline. Format: [hierarchy_level, title, page_number_1_indexed]
    toc = [
        [1, "Title Page", 1],
        [1, "Chapter 1: The Vector Space", 2],
        [1, "Chapter 2: Manifold Topology", 3]
    ]
    doc.set_toc(toc)

    # Flush byte stream to disk and deallocate C-memory
    doc.save(str(out_path))
    doc.close()

    return out_path
