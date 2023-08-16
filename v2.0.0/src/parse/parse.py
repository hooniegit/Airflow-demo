import json

list_merged = []

for page in range (1, 11):
    file_path = f"/Users/kimdohoon/Desktop/movie/2023/KOBIS_MOVIE_LIST_2023_{page}.json"
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    movie_cds = [movie["movieCd"] for movie in data["movieListResult"]["movieList"]]
    print(movie_cds)
    list_merged += movie_cds

list_path = "/Users/kimdohoon/Desktop/movie/list.txt"
with open(list_path, "w") as file:
    file.write(str(list_merged))