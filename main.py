import os
import markdown

# --- Configuration ---
PROJECT_DIR = '.'
OUTPUT_FILE = 'compiled_project.html'
DOCUMENT_TITLE = 'Övning 3'  # <-- Change this to whatever you want!

TARGET_EXTENSIONS = {'.md', '.py', '.js', '.ts', '.css', '.cpp', '.java', '.json'}
IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', '.pytest_cache'}


def gather_files(directory):
    matched_files = []
    current_script_path = os.path.abspath(__file__)

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            # Skip the readme file (case-insensitive)
            if file.lower() == 'readme.md':
                continue

            file_path = os.path.join(root, file)

            # Skip this compiler script itself
            if os.path.abspath(file_path) == current_script_path:
                continue

            ext = os.path.splitext(file)[1].lower()
            if ext in TARGET_EXTENSIONS:
                matched_files.append(file_path)

    # Sort alphabetically
    return sorted(matched_files)


def build_markdown(files):
    # Inject the custom title as the main H1 header
    combined_md = f"# {DOCUMENT_TITLE}\n\n"

    for file_path in files:
        ext = os.path.splitext(file_path)[1].lower()

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            combined_md += f"## `{file_path}`\n\n"

            if ext == '.md':
                combined_md += content + "\n\n"
            else:
                lang = ext[1:]
                combined_md += f"```{lang}\n{content}\n```\n\n"

        except Exception as e:
            print(f"Skipping {file_path} due to error: {e}")

    return combined_md


def main():
    print("Scanning directories...")
    files = gather_files(PROJECT_DIR)

    if not files:
        print("No matching files found.")
        return

    print(f"Found {len(files)} files. Combining into Markdown...")
    combined_markdown = build_markdown(files)

    print("Converting Markdown to HTML...")
    html_body = markdown.markdown(combined_markdown, extensions=['fenced_code', 'tables'])

    # Inject the custom title into the HTML <title> tag
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{DOCUMENT_TITLE}</title>

        <script>
            MathJax = {{
              tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
              }}
            }};
        </script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                line-height: 1.6;
                color: #24292e;
                max-width: 1000px;
                margin: 0 auto;
                padding: 40px;
            }}
            h1 {{ border-bottom: 2px solid #eaecef; padding-bottom: 10px; }}
            h2 {{ color: #0366d6; margin-top: 40px; border-bottom: 1px solid #eaecef; padding-bottom: 5px; page-break-after: avoid; }}
            pre {{
                background-color: #f6f8fa;
                border-radius: 6px;
                padding: 16px;
                overflow: auto;
                font-size: 85%;
                line-height: 1.45;
                page-break-inside: avoid;
            }}
            code {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }}

            @media print {{
                body {{ padding: 0; max-width: 100%; }}
                pre {{ white-space: pre-wrap; word-wrap: break-word; }}
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    print("Saving HTML file...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Success! Open '{OUTPUT_FILE}' in your web browser.")
    print("Wait a second or two for equations to render, then press Cmd+P / Ctrl+P to save as PDF.")


if __name__ == "__main__":
    main()
