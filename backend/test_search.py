from services.fashion.search import search_similar

results = search_similar(
    "../dataset/fashion-dataset/images/10000.jpg",
    top_k=5
)

for r in results:
    print("-" * 50)
    print(r)