from utils import save_images, make_directory
from yandex_images_parser import Parser

parser = Parser(headless=False)


output_dir = "./чб/кабарга фотоохота ночь"
make_directory(output_dir)

square_deer = parser.query_search(query='кабарга ночная фотоохота',
                                 limit=43,
                                 color=parser.color.gray,
                                 )
for i in range (1, 43):
    square_deer_url = square_deer[i]
    similar_deers = parser.image_search(url=square_deer_url,
                                    limit=3000)

    print(f"Moschidae:\n{similar_deers}\n")

    print("Moschidae:")

    for kos in similar_deers:
        print(kos)
    save_images(square_deer, dir_path=output_dir, prefix="original_")
    save_images(similar_deers, dir_path=output_dir, prefix="similar_", number_images=True)