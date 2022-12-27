<h1>
Keep your tos watchlist uptodate
</h1>

<p>

</p>

<h2>Validation List</h2>
1. Liquidity
2. Open Interest

<h2>Scrap for following</h2>
1. Most Active
2. Unusual Activity
3. High Implied Volatility/Rankings
4. Short Interest

<h2>Prerequisites</h2>
1. Python 3.6+, https://www.python.org/downloads/
2. Install pip3, https://pip.pypa.io/en/stable/
3. Install webdriver, https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
4. Make sure all of the above executables are added to $PATH

<h2>How to Build and Generate watch lists</h2>
1. Open bash and change directory to project root directory
2. Execute `pip3 install -r requirements.txt`
3. Execute `chmod 600 launch.sh`
4. Execute `./launch.sh`
5. Watch lists should be generated in ./out directory