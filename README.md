# How to run the availability checker

1. Install `python`
    ```shell
    brew install python # For Mac
    ``` 
2. Install `pipenv`
    ```shell
    brew install pipenv # For Mac
    ```
3. Install project dependencies 
    ```shell
    pipenv install
    ```
4. Configure products to check inside `configuration.yaml` file based on already included examples
5. Run the scraper:
    ```shell
    python scrape.py
    ```
6. Check for the command output
