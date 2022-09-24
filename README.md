# Product Availability Scraper
Check whether or not the URL contains certain text. For example, we can check whether a page contains the text "in stock" or, conversely, whether it contains the text "out of stock".

## How to run the availability checker/scraper
1. Clone this project
   ```shell
   git clone https://github.com/david-pivonka/product-availability-scraper.git
   ```
2. Install `python`
    ```shell
    brew install python # For Mac
    ``` 
3. Install `pipenv`
    ```shell
    brew install pipenv # For Mac
    ```
4. Install project dependencies 
    ```shell
    pipenv install
    ```
5. Configure products to check inside [configuration.yaml](https://github.com/david-pivonka/product-availability-scraper/blob/main/configuration.yaml) file based on already included examples
6. Run the scraper:
    ```shell
    python scrape.py
    ```
7. Check for the command output

## Run as the cron on Linux
You can run this script as a cron command to constantly check for product availability.   
1. Run all the steps in "How to run" tutorial
2. Create the new cron file on the Linux server
   ```shell
   sudo vim /etc/cron.d/product-availability-checker
   ```
3. Append the following content
   ```text
   */10 * * * *    python    /absolute/path/to/scraper.py
   
   ```
   **Make sure to include empty line at the end of the file!**\
   _You can replace `*/10 * * * *` with different cron rule, check https://crontab.guru/_
4. Save the file
