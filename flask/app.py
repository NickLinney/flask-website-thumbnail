from flask import Flask, request, send_file
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
import io

app = Flask(__name__)

@app.route('/thumbnail')
def thumbnail():
    url = request.args.get('url')
    if not url:
        return 'Please provide a URL'

    # Configure Firefox options
    options = Options()
    options.headless = True

    # Launch Firefox browser
    driver = webdriver.Firefox(options=options)

    # Navigate to URL and take a screenshot
    driver.get(url)
    screenshot = driver.get_screenshot_as_png()

    # Close the browser
    driver.quit()

    # Create thumbnail image from the screenshot
    image = Image.open(io.BytesIO(screenshot))
    image.thumbnail((300, 300))

    # Convert the image to PNG format and return it
    output = io.BytesIO()
    image.save(output, format='PNG')
    output.seek(0)
    return send_file(output, mimetype='image/png')