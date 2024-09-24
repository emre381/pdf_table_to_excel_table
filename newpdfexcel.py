from flask import Flask, request, render_template
import pdfplumber
import pandas as pd
import os

app = Flask(__name__)

def pdf_to_excel(pdf_file, excel_file):
    # Open the pdf file
    with pdfplumber.open(pdf_file) as pdf:
        # Extract text from each page
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table:
                    df = pd.DataFrame(table)
                    all_tables.append(df)

        if not all_tables:
            all_tables.append(pd.DataFrame([["No tables found"]]))

        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            for id, df in enumerate(all_tables):
                df.to_excel(writer, sheet_name=f"Sheet_{id}", index=False)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return 'No file part'
        
        file = request.files['pdf_file']
        if file.filename == '':
            return 'No selected file'
        
        if file and file.filename.endswith('.pdf'):
            # Save the file to a temporary location
            file_path = './uploaded.pdf'
            file.save(file_path)
            
            # Define the output Excel file name based on the uploaded PDF file name
            base_filename = os.path.splitext(file.filename)[0]  # Get the filename without extension
            output_excel_file = f'{base_filename}.xlsx'  # Change the extension to .xlsx
            
            # Process the PDF and export to Excel
            pdf_to_excel(file_path, output_excel_file)
            
            # Get the absolute path of the saved Excel file
            excel_file_path = os.path.abspath(output_excel_file)
            
            return f'File processed and saved as {output_excel_file}. <br> Location: {excel_file_path}'
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
