# html to pdf Converter 


## Description

This is a script to convert a web page  to a PDF file. It utilizes Puppeteer and WeasyPrint for the conversion process.

## How it Works

When converting a URL to PDF, we use Puppeteer and WeasyPrint. Since <strong> WeasyPrint does not support JavaScript execution </strong>, we first fetch the loaded HTML, CSS, and content using Puppeteer. We then create an HTML file from that fetched content, preserving the same structure. Finally, we convert this HTML file to a PDF file using WeasyPrint.

## Installation

To run this script, we need to install WeasyPrint and Puppeteer also we need path of chrome.exe

### Step 1 : 
```bash or cmd 
git clone https://github.com/B2-krunalrana/python_pdf_conversion.git

```
### Step 2 : 
```bash or cmd 
pip install WeasyPrint
pip install pyppeteer
```

## Reference links

### weasyprint:  https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
### pyppeteer:  https://pypi.org/project/pyppeteer/

### Tips : 

#### When dealing with images, we need to convert them into data URLs and then include them in HTML files. This helps improve the layout and ensures that everything looks right.
#### Image to data url : https://ezgif.com/image-to-datauri 

#### Defuault path of chrome.exe 
64-bit Windows :
```javascript 64-bit Windows
    C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
```
32-bit Windows : 
```javascript 32-bit Windows
    C:\Program Files\Google\Chrome\Application\chrome.exe
```
Xubuntu 20.04 :
```javascript Xubuntu 20.04
    /opt/google/chrome/chrome
```

### Quick Note:

Just a heads up, we're avoiding CSS frameworks like Bootstrap that heavily depend on JavaScript. Sometimes, these frameworks can cause compatibility issues with WeasyPrint. Therefore, we're committed to steering clear of any frameworks, like Bootstrap, that rely on JavaScript to apply CSS styles.

