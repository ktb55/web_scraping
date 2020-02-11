import subprocess

s_prompt = 'scrapy crawl book_scrape -o books.csv'

run = subprocess.Popen(s_prompt, shell=True)
