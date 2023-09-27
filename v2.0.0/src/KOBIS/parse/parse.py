import json

list_merged = []
year = 2019

for page in range (1, 86):
    file_path = f"/Users/kimdohoon/Desktop/movie/{year}/KOBIS_MOVIE_LIST_{year}_{page}.json"
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    movie_cds = [movie["movieCd"] for movie in data["movieListResult"]["movieList"]]
    print(movie_cds)
    list_merged += movie_cds

list_path = f"/Users/kimdohoon/Desktop/movie/list_{year}.txt"
with open(list_path, "w") as file:
    file.write(str(list_merged))