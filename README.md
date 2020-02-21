# screenshot compare

## Videos

https://www.loom.com/share/c6c45aa6f3e445a18068e803b552971c
https://www.loom.com/share/10263dd3ae2e4b189a078cdbbd0ded6e

## Installation

1. Make sure Python 3.8 or higher, pip and git are installed.
2. Make sure Firefox and geckodriver are installed. geckodriver must be in your `PATH`. Example:

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/location-of-geckodriver
```

3. Run the commands below. Depending on your system you may need run `pip` instead of `pip3`.

```
git clone https://github.com/andivis/screenshot-compare.git
cd screenshot-compare
pip3 install -r requirements.txt
```

## Instructions

1. Make sure `user-data/input/input.txt` contains the list of url's.
2. Run `python3 main.py`. Depending on your system you may need run `python main.py` instead

## Command line parameters

- `-u` or `--url`: the url to take the screenshot of
- `-e` or `--email`: the email address to send notifications to
- `-m` or `--max-difference`: the most the current screenshot can differ from the last one, in percent

## Options

`user-data/options.ini` accepts the following options:

- `inputFile`: Default: `user-data/input/input.txt`
- `outputDirectory`: Default: `user-data/output`
- `browser`: Can be firefox or chrome. Default: `firefox`
- `emailAddress`: the email address to send notifications to. Default: ``
- `smtpHost`: Default: ``
- `smtpPort`: Default: ``
- `smtpUsername`: Default: ``
- `smtpPassword`: Default: ``
- `secondsBeforeScreenshot`: Wait after page load before taking screenshot. Default: `1`
- `allowedDifference`: The most the current screenshot can differ from the last one, in percent. Default: 5