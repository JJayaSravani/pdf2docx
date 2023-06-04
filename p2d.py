from flask import Flask, request, send_file, render_template
import pdf2docx
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_pdf_to_docx():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        f1 = request.files['f1']
        os.makedirs('uploads', exist_ok=True)
        os.makedirs('converted', exist_ok=True)
        # Save the uploaded PDF file to a temporary location
        pdf_path = 'uploads/input.pdf'
        f1.save(pdf_path)
        #doc path
        docx_path = os.path.join(os.getcwd(), 'converted', 'output.docx')

        # Convert the PDF to DOCX
        pdf2docx.parse(pdf_path, docx_path)
        
        # Return the converted DOCX file for download
        return send_file(docx_path, as_attachment=True,download_name='output.docx')

if __name__ == '__main__':
    app.run(debug=True)
