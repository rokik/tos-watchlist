# TOS watchlist

## Validation List
- Liquidity
- Open Interest

## Scrap for following
- Most Active
- Unusual Activity
- High Implied Volatility/Rankings
- Short Interest

## Prerequisites
- Python 3.6+, https://www.python.org/downloads/
- Install pip3, https://pip.pypa.io/en/stable/
- Install webdriver, https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
- Make sure all of the above executables are added to $PATH


## How to Build and Generate watch lists
- Open bash and change directory to project root directory 
- Execute `pip3 install -r requirements.txt`
- Execute `chmod 600 launch.sh`
- Execute `./launch.sh`
- Watch lists should be generated in ./out directory