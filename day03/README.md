# Day03 – Pixel Area to mm² Converter

This project converts pixel area into mm² using the formula:

mm² = 2.1462 * pixel_area / 1,000,000

yaml
Copy code

The project also supports normalization of the converted value by an additional number.

In this exercise, the “business logic” was moved into a separate module, and a third-party library (`click`) was used to improve the command-line interface. Tests were added using `pytest`.

---

## 📦 Installation

Before running the project, install the dependencies:

```sh
pip install -r requirements.txt
Dependencies include:

click – for the command-line interface

pytest – for running tests

▶️ How to Run
1. CLI (Click-based)
Run with arguments:

sh
Copy code
python day03/pixels_to_mm_cli.py --pixel-area 200000 --normalization-value 2
Or run interactively:

sh
Copy code
python day03/pixels_to_mm_cli.py
2. GUI
sh
Copy code
python day03/pixels_to_mm_gui.py
3. Run Tests
sh
Copy code
pytest day03/tests -q
🤖 Use of AI
I used AI tools (ChatGPT/Copilot) to help with:

Refactoring code into separate modules

Implementing a Click-based CLI

Creating pytest tests for the business logic

Writing the requirements.txt file

Writing this README file

Prompts used
Some of the prompts I used:

“Please rewrite my CLI using Click instead of argparse.”

“Write pytest tests for my pixel-to-mm conversion function.”

“Create a requirements.txt for click and pytest.”

“Write a README.md that explains dependencies, how to run the project, and how AI was used.”

📁 Project Structure
bash
Copy code
day03/
│── pixels_to_mm.py          # business logic
│── pixels_to_mm_cli.py      # Click CLI
│── pixels_to_mm_gui.py      # GUI
│── requirements.txt
│── tests/
│     └── test_pixels_to_mm.py
└── README.md