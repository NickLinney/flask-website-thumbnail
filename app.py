from flask import Flask, request, send_file
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from io import BytesIO

app = Flask(__name__)

@app.route('/thumbnail')
def get_thumbnail():
    url = request.args.get('url')
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('-headless')
    firefox_service = FirefoxService(executable_path='/usr/local/bin/geckodriver')
    browser = Firefox(service=firefox_service, options=firefox_options)
    browser.get(url)
    screenshot = browser.get_screenshot_as_png()
    browser.quit()
    return Response(screenshot, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
