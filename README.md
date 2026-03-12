# PDF Chapter Slicer: Semantic Document Extractor

## 1. Executive Summary
An enterprise-grade Command Line Interface (CLI) pipeline designed to deterministically slice monolithic PDF books into discrete, chapter-based PDF artifacts. 

## 2. Architecture & Algorithms
The system eschews brittle shell pipelines (e.g., piping `pdftotext` to `grep`) in favor of direct C-level memory access to the PDF structure via `PyMuPDF`. 

The extraction strategy is a two-pass algorithm:
1.  **AST Traversal (Primary):** The system parses the PDF's internal Outline dictionary (Bookmarks) and the `/PageLabels` Document Catalog to map logical chapter nodes to physical byte-array indices.
2.  **Spatial Heuristics (Fallback):** For unstructured PDFs lacking an Outline AST, the system falls back to a spatial analysis algorithm. It calculates the local maxima of font sizes and weights on a per-page basis to infer structural chapter boundaries.

## 3. Engineering Constraints
* **Zero-Copy Slicing:** Output generation must slice the original byte stream to avoid CPU-intensive re-encoding/re-rendering of images and vectors.
* **Pure Functions:** Domain logic must remain isolated from the CLI I/O layer (Hexagonal Architecture).
* **Deterministic Testing:** Test suites must synthetically generate PDF fixtures in-memory rather than relying on external binary files.

## 4. Usage (Future Implementation)
`python -m src.cli slice "An_Introduction_to_Statistical_Learning.pdf" --output-dir ./chapters/`
