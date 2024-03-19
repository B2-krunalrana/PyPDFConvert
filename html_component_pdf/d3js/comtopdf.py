#  pyppeteer

import asyncio
import os
from pyppeteer import launch
from weasyprint import HTML, CSS

# add path to chrome.exe
chromeexe="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def html_to_pdf(output_file):
    try:
        # Load HTML content from file
        html_file_path = output_file + ".html"
        html_content = open(html_file_path, 'r', encoding='utf-8').read()
        print("HTML content read successfully.")

        # No font configuration or custom CSS needed

        # Create WeasyPrint HTML object
        html = HTML(string=html_content)

        pdf_file_name = output_file + ".pdf"
        # Specify output PDF file path
        pdf_file_path = os.path.join(os.path.dirname(os.path.abspath(html_file_path)), pdf_file_name)
        print("PDF creation started.")

        # Convert HTML to PDF (no font_config argument)
        pdf_bytes = html.write_pdf(pdf_file_path)
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
    await page.waitFor(5000)  # Wait for 5 seconds (5000 milliseconds)

    # Get the rendered HTML after JavaScript execution
    rendered_html = await page.content()

    print()
    print(rendered_html)
    print()

    output_file_name=output_file+".html"
    # Save the rendered HTML to a file
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(rendered_html)

    html_to_pdf(output_file)
    # Close the browser
    await browser.close()

# Specify the URL to download
url = "http://127.0.0.1:5501/html_component_pdf/d3js/component.html"

# Specify the output file path
output_file = "d3js_component_html"


# Run the asyncio event loop to execute the function
asyncio.get_event_loop().run_until_complete(download_rendered_html(url, output_file))

