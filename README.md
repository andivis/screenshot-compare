# screenshot compare

## Installation

1. Make sure Python 3.8 or higher, pip and git are installed.
2. Make sure Firefox and geckodriver are installed. Example:

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

1. Make sure `user-data/input/input.txt` contains the channel information. Follow the format of the example in the file.
2. Run `python3 main.py`. Depending on your system you may need run `python main.py` instead

## Command line parameters

- `-u` or `--url`: the url to take the screenshot of
- `-e` or `--email`: the email address to send notifications to
- `-m` or `--max-difference`: the most the current screenshot can differ from the last one, in percent

## Options

`user-data/options.ini` accepts the following options:

- `maximumResultsPerKeyword`: How many pdf's to download for a given site/keyword combination. -1 means no limit. Default 25000.
- `directoryToCheckForDuplicates`: Only download a pdf if it does not exist anywhere in this directory. Blank means don't check any directory. No quotes on directory name.