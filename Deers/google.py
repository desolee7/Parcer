from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/Ева/Desktop/Универ/парсер/google_deer'})

print('Количество фоток: ')
count=int(input())

print('Запрос: ')
resp = str(input())

google_crawler.crawl(keyword=resp, max_num=count)