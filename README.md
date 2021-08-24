#Web Crawler

### Prerequities
- Python 3.6 or higher
- Pip
- Scrapy

### Info
In this section, a web crawler has been created for scraping the content of https://www.snopes.com/fact-check/ domain. In every page, the details of every fact will be scraped. These details contain some information of a fact such as:
1. Title
2. Author
3. Publish Date
4. URL
5. Content
6. Claim
7. Rating
8. Category
9. Tags

### Usage
- You can crawl the mentioned above domain and extract the information with the following command:

   ```scrapy crawl FactChecks```

- If you want to save the scraped content into a file, you can use the following command:

   ```scrapy crawl FactChecks -o output.json``` 
   
   After the completion of crawling, Run the command below to get the prettified json output:
   
   ```python main.py```

   **Note**: You can export the crawled content to other formats e.g. _csv_, _xlsx_ by specifying the extension of output file. You can also use the *__Pandas__* module as shown below:
   ```
    df = pandas.read_json('output.json')
    df.to_csv('output.csv', ...)
   ```   
