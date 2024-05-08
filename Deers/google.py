from icrawler.builtin import GoogleImageCrawler
from datetime import date

google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/Ева/Desktop/Универ/парсер/EuropeanRoedeer4'})

google_crawler.crawl(keyword = 'европейская косуля в поле', max_num = 800)

# print('Количество фоток: ')
# count=int(input())

# print('Запрос: ')
# resp = str(input())

# google_crawler.crawl(keyword=resp, max_num=count)


# from icrawler.builtin import GoogleImageCrawler
# import datetime

# n_total_images = 10000
# n_per_crawl = 100

# delta = datetime.timedelta(days=30)
# end_day = datetime.datetime(2022, 9, 29)

# def datetime2tuple(date):
#     return (date.year, date.month, date.day)

# for i in range(int(n_total_images / n_per_crawl )):
#     start_day = end_day - delta
#     google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': 'C:/Users/Ева/Desktop/Универ/парсер/google_deer'})
#     google_crawler.crawl(keyword='wild deer', filters={'date':(datetime2tuple(start_day), datetime2tuple(end_day))}, file_idx_offset=i*n_per_crawl , max_num=n_per_crawl)
#     end_day = start_day - datetime.timedelta(days=1)