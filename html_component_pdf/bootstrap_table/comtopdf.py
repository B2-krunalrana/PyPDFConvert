import asyncio
import os
from pyppeteer import launch
from weasyprint import HTML
from bs4 import BeautifulSoup
import urllib.parse

# Add path to chrome.exe
chromeexe = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

def file_uri(file_path):
    """Return the file URI for the given file path."""
    return "http://127.0.0.1:5501/html_component_pdf/bootstrap_table/bootstrap5_table_component_html_cleaned.html"
# here we need to convrt tthat into html and using live server link  only we need to gerante pdf 

async def html_to_pdf(output_file):
    try:
        # Load HTML content from file
        html_file_path = output_file + "_cleaned.html"
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        print(file_uri("55"))
        html_uri = file_uri("55")
        # Create WeasyPrint HTML object
        html = HTML(url=html_uri)

        pdf_file_name = output_file + ".pdf"
        # Specify output PDF file path
        pdf_file_path = os.path.join(os.path.dirname(os.path.abspath(html_file_path)), pdf_file_name)

        # Convert HTML to PDF
        html.write_pdf(pdf_file_path)
        print("PDF created at:", os.path.abspath(pdf_file_path))

    except Exception as e:
        print("Error during PDF creation:", e)

async def download_rendered_html(url, output_file):
    # Launch the headless browser
    browser = await launch(headless=True, executablePath=chromeexe)

    # Create a new page
    page = await browser.newPage()

    # Navigate to the URL
    await page.goto(url)

    # Wait for JavaScript to execute (we can adjust this time according to our page load time)
    await page.waitFor(10000)  # Wait for 10 seconds (10000 milliseconds)

    # Get the rendered HTML after JavaScript execution
    rendered_html = await page.content()

    # Define the output file name
    output_file_name = output_file + ".html"

    # Save the rendered HTML to a file
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(rendered_html)

    # Close the browser
    await browser.close()

    # Remove <script> tags from the HTML
    soup = BeautifulSoup(rendered_html, 'html.parser')
    for script in soup.find_all('script'):
        script.extract()

    # Get the HTML as a string without script tags
    clean_html = str(soup)

    # Define the output file name for cleaned HTML
    output_file_name_cleaned = output_file + "_cleaned.html"

    # Save the cleaned HTML to a file
    with open(output_file_name_cleaned, "w", encoding="utf-8") as file:
        file.write(clean_html)

    # Convert HTML to PDF
    await html_to_pdf(output_file)

# Specify the URL to download
url = "http://127.0.0.1:5501/html_component_pdf/bootstrap_table/component.html"

# Specify the output file path
output_file = "bootstrap5_table_component_html"

# Run the asyncio event loop to execute the function
asyncio.run(download_rendered_html(url, output_file))
