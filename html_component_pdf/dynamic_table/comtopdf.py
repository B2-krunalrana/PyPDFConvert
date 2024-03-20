import asyncio
import os
from pyppeteer import launch
from bs4 import BeautifulSoup
from weasyprint import HTML,CSS

# Specify the path to the Chrome executable
chrome_exe_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

async def fetch_rendered_html(url):
    try:
        # Launch the headless browser with the specified Chrome executable path
        browser = await launch(headless=True, executablePath=chrome_exe_path)

        # Create a new page
        page = await browser.newPage()

        # Navigate to the URL
        await page.goto(url)

        # Wait for JavaScript to execute (you can adjust this time according to your page load time)
        await page.waitFor(5000)  # Wait for 5 seconds (5000 milliseconds)

        # Get the rendered HTML after JavaScript execution
        rendered_html = await page.content()

        # Close the browser
        await browser.close()

        return rendered_html

    except Exception as e:
        print("Error during HTML fetch:", e)
        return None


def html_to_pdf(rendered_html, output_file):
    try:
        # Parse the rendered HTML using BeautifulSoup
        soup = BeautifulSoup(rendered_html, 'html.parser')

        # Create WeasyPrint HTML object
        html = HTML(string=str(soup))

        # Specify output PDF file path
        pdf_file_name = output_file + ".pdf"
        pdf_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), pdf_file_name)
        print("PDF creation started.")

        # bootstrap_css_link = r"D:/#Live_project/html_to_pdf/html_component_pdf/dynamic_table/bootstrap-4.3.1-dist/css/bootstrap.min.css"
        # css = CSS(string=f'@import url("file://{bootstrap_css_link}");')


        # Create WeasyPrint HTML object with CSS
        # html = HTML(string=str(soup))
        # html.write_pdf(output_file + ".pdf", stylesheets=[css])
        # Convert HTML to PDF
        html.write_pdf(pdf_file_path)

        # Print success message
        print("PDF created successfully at:", os.path.abspath(pdf_file_path))

    except Exception as e:
        print("Error during PDF creation:", e)


async def main():
    # Specify the URL to fetch
    url = "http://127.0.0.1:5501/html_component_pdf/dynamic_table/component.html"

    # Specify the output file path
    output_file = "generated_pdf"

    # Fetch rendered HTML
    rendered_html = await fetch_rendered_html(url)

    if rendered_html:
        # Convert HTML to PDF
        html_to_pdf(rendered_html, output_file)


# Run the asyncio event loop to execute the function
asyncio.get_event_loop().run_until_complete(main())
