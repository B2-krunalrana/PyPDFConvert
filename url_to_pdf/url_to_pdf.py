#  pip install pyppeteer
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
url = "https://api.ahaguru-dev.clustrex.com/gethtmlfile/13032024065801/67413"
# url="http://localhost/studentperformancepdfnew?student_id_mr=53769&course_id_mr=653&report_name_mr=UGVyZm9ybWFuY2UgUmVwb3J0IHwgQUREIDogbWlsZXN0b25lLXRhYmxlIGluIHN0dWRlbnQgcGRmIHJlcG9ydCBURVNUIDE=&lesson_ids_mr=141%2C161%2C228%2C270%2C276%2C162%2C163%2C288%2C283%2C330%2C478%2C479%2C480%2C290%2C333%2C473%2C1020%2C456%2C375%2C376%2C374%2C555%2C567%2C335%2C336%2C344%2C576%2C578%2C538%2C574%2C571%2C557%2C577%2C584%2C585%2C583%2C474%2C563%2C575%2C573%2C3823&lesson_display_mr=L1%2CL2%2CL3%2CL4%2CL5%2CL6%2CL7%2CL8%2CL9%2CL10%2CL11%2CL12%2CL13%2CL14%2CL15%2CL16%2CL17%2CL18%2CL19%2CL20%2CL21%2CL22%2CL23%2CL24%2CL25%2CL26%2CL27%2CL28%2CL29%2CL30%2CL31%2CL32%2CL33%2CL34%2CL35%2CL36%2CL37%2CL38%2CL39%2CL40%2CL41&session_ids_mr=3360%2C3364%2C3374%2C3375%2C3387%2C3392%2C3407%2C3416%2C3439%2C3449%2C3473%2C3483&test_ids_mr=%283407%2C15699%29%2C%283439%2C15845%29%2C%283473%2C16060%29%2C%284733%2C962%29&test_display_mr=T1%2CT2%2CT3%2CT4&good_score_mr=98%2C85%2C66%2C98&opening_remarks=PHN0cm9uZz5QZXJmb3JtYW5jZSBSZXBvcnQgfCBBREQ6IG1pbGVzdG9uZS10YWJsZSBpbiBzdHVkZW50IHBkZiByZXBvcnQgVEVTVCAxIDwvc3Ryb25nPiA6ICRuYW1l&system_remarks_attendance=on&system_remarks_test=on&system_remarks_score=on&closing_remarks=UGVyZm9ybWFuY2UgUmVwb3J0IHwgQUREIDogbWlsZXN0b25lLXRhYmxlIGluIHN0dWRlbnQgcGRmIHJlcG9ydCBURVNUIDE=&batch_ids_mr=606"

# Specify the output file path
output_file = "ahaguru_student_report"


# Run the asyncio event loop to execute the function
asyncio.get_event_loop().run_until_complete(download_rendered_html(url, output_file))

