from flask import Flask, request, send_file
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/export_pdf', methods=['GET'])
def export_pdf():
    url = request.args.get('url')

    if not url:
        return 'URL parameter is required', 400

    try:
        html = HTML(url=url)
        pdf = render_pdf(html)
        return send_file(pdf, attachment_filename='exported_pdf.pdf', as_attachment=True, mimetype='application/pdf'), 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(port=5005)
