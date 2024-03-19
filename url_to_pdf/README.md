# URL to PDF Converter

## Description

This is a script to convert a web page from a URL to a PDF file. It utilizes Puppeteer and WeasyPrint for the conversion process.

## How it Works

When converting a URL to PDF, we use Puppeteer and WeasyPrint. Since WeasyPrint does not support JavaScript execution, we first fetch the loaded HTML, CSS, and content using Puppeteer. We then create an HTML file from that fetched content, preserving the same structure. Finally, we convert this HTML file to a PDF file using WeasyPrint.

## Installation

To run this script, you need to install WeasyPrint and Puppeteer also you need path of chrome.exe

```bash or cmd 
git clone https://github.com/B2-krunalrana/python_pdf_conversion.git

```

```bash or cmd 
pip install WeasyPrint
pip install pyppeteer
```

### weasyprint:  https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
### pyppeteer:  https://pypi.org/project/pyppeteer/

