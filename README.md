# PDF Table to Excel Converter

## Description

This project provides a simple web application built with Flask that converts tables extracted from PDF files into Excel spreadsheets. The application uses `pdfplumber` to extract tables from PDF documents and `pandas` to create Excel files.

## Features

- Upload a PDF file containing tables.
- Extracts tables from each page of the PDF.
- Saves extracted tables into an Excel file.
- Displays the location of the saved Excel file after processing.

## Requirements

- Python 3.x
- Flask
- pdfplumber
- pandas
- openpyxl

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/pdf_table_to_excel_table.git
Navigate to the project directory:
cd pdf_table_to_excel_table

Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

Install the required packages:
pip install Flask pdfplumber pandas openpyxl

Usage
Run the Flask application:
python newpdfexcel.py

