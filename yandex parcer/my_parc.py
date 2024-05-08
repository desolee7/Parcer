from utils import save_images, make_directory
from yandex_images_parser import Parser

parser = Parser(headless=False)

square_deer = parser.query_search(query="Przewalskium albirostris — Беломордый олень",
                                 limit=200,
                                 size=parser.size.medium,
                                 orientation=parser.orientation.square)

square_deer_url = square_deer[0]

similar_deers = parser.image_search(url=square_deer_url,
                                   limit=500)

print(f"Przewalskium albirostris — Беломордый олень:\n{similar_deers}\n")

print("Przewalskium albirostris — Беломордый олень:")
for cat in similar_deers:
    print(cat)

output_dir = "./Семейство оленевые/Подсемейство Cervinae/Род Przewalskium"
make_directory(output_dir)

save_images(square_deer, dir_path=output_dir, prefix="original_")
save_images(similar_deers, dir_path=output_dir, prefix="similar_", number_images=True)