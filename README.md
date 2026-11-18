# codebinder
A tool for compiling code files into a single beautifully formatted HTML file for viewing in the browser, converting to PDF, or printing to paper. It saves a lot of time and effort each time one wishes to compile all files of different types into a single clean document.

## Disclosure on AI usage
The list of features have been generated with Gemini AI.

## Features
* **Zero System Dependencies:** No need to install finicky tools like `wkhtmltopdf` or `LaTeX` engines. It leverages your web browser's native print engine for perfect rendering.
* **MathJax Support:** Automatically renders complex mathematical equations (`$x^2$` and `$$y=mx+b$$`) written in your Markdown files.
* **Syntax Highlighting:** Formats your source code neatly into fenced code blocks.
* **Smart Filtering:** Automatically ignores itself, your `README.md`, and common junk folders (like `node_modules`, `venv`, and `.git`).
* **Alphabetical Sorting:** Groups and sorts your files logically by directory and filename.
* **Print-Optimized CSS:** Ensures code blocks aren't awkwardly split across multiple pages when printing to PDF.

## Prerequisites

You only need Python and a single standard library module.

```bash
pip install markdown
