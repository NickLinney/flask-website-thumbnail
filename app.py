from flask import Flask, request, send_file
from selenium import webdriver
import os

app = Flask(__name__)

# Set the path to the chromedriver executable
chromedriver_path = "/path/to/chromedriver"

# Define the function to generate a thumbnail
def generate_thumbnail(url):
    # Set the options for the headless Chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1200x600')

    # Set the path to the chromedriver executable
    chromedriver_path = "/path/to/chromedriver"
    browser = webdriver.Chrome(chromedriver_path, options=options)

    # Open the webpage and take a screenshot
    browser.get(url)
    browser.set_window_size(1200, 600) # This is larger than 300x300 so we can take a high resolution image
    screenshot_path = os.path.join(os.getcwd(), "screenshot.png")
    browser.save_screenshot(screenshot_path)

    # Crop and resize the image to a thumbnail
    from PIL import Image
    image = Image.open(screenshot_path)
    image = image.crop((0, 0, 1200, 600)) # Crop to the same size as the window
    image.thumbnail((300, 300)) # Resize to 300x300 pixels
    thumbnail_path = os.path.join(os.getcwd(), "thumbnail.png")
    image.save(thumbnail_path)

    # Clean up the browser and return the thumbnail
    browser.quit()
    return thumbnail_path

# Define the Flask route to handle thumbnail requests
@app.route("/thumbnail", methods=["GET"])
def thumbnail():
    url = request.args.get('url')
    thumbnail_path = generate_thumbnail(url)
    return send_file(thumbnail_path, mimetype='image/png')

# Run the app
if __name__ == '__main__':
    app.run()
