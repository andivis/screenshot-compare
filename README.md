# Screenshot Compare

-   Get notified when the screenshot of a given webpage changes
-   The change must be at least X percent of the pixels. X defaults to 5. This way you can ignore insignificant changes.
-   Use it to easily monitor your websites for unintended changes and bugs
-   **100%** Python. Uses headless Chrome or headless Firefox.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Command line parameters](#command-line-parameters)
4. [Options](#options)

## Installation

1. Make sure Python 3.8 or higher, pip and git are installed.
2. Make sure Firefox and geckodriver are installed. geckodriver must be in your `PATH`. Example:

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/location-of-geckodriver
```

3. If you prefer to use Chrome instead of Firefox, make sure Chrome and chromedriver are installed. chromedriver must be in your `PATH`.

4. Run the commands below. Depending on your system you may need run `pip` instead of `pip3`.

```
git clone https://github.com/andivis/screenshot-compare.git
cd screenshot-compare
pip3 install -r requirements.txt
```

## Usage

1. Make sure `user-data/input/input.txt` contains the list of url's.
2. If you want to get notified by email, put your SMTP credentials in `user-data/options.ini`.
3. Run `python3 main.py --initial`. Depending on your system you may need to run `python main.py --initial` instead. This simply takes the initial screenshots to compare against later.
4. Run `python3 main.py --compare`. The app checks if the screenshot of any of the webpages differs from the screenshot it took last time. If so, it will print a message to the terminal and email you.
5. For subsequent runs, you can just `python3 main.py --compare` again.

## Command line parameters

-   `-u` or `--url`: the url to take the screenshot of
-   `-e` or `--email`: the email address to send notifications to
-   `-m` or `--max-difference`: the most the current screenshot can differ from the last one, in percent

## Options

`user-data/options.ini` accepts the following options:

-   `inputFile`: Default: `user-data/input/input.txt`
-   `outputDirectory`: Default: `user-data/output`
-   `browser`: Can be firefox or chrome. Default: `firefox`
-   `emailAddress`: the email address to send notifications to. Default: ``
-   `smtpHost`: Default: ``
-   `smtpPort`: Default: ``
-   `smtpUsername`: Default: ``
-   `smtpPassword`: Default: ``
-   `secondsBeforeScreenshot`: Wait after page load before taking screenshot. Default: `1`
-   `allowedDifference`: The most the current screenshot can differ from the last one, in percent. Default: 5
