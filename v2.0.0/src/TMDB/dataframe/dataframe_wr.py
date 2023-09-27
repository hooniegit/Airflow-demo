import pandas as pd
import json, os

tmp_dir = "/Users/woorek/Downloads/movie/2023/"
file_name = "KOBIS_MOVIE_LIST_2023_1.json"

with open(os.path.join(tmp_dir, file_name), "r") as data:
    json_data = json.load(data)


final_data = json_data["movieListResult"]["movieList"]
movie_data=[]
for movie in final_data:
    directors = ", ".join([director["peopleNm"] for director in movie["directors"]])
    companies = ", ".join([company["companyNm"] for company in movie["companys"]])

    movie_data.append({
        "movieCd": movie["movieCd"],
        "movieNm": movie["movieNm"],
        "movieNmEn": movie["movieNmEn"],
        "prdtYear": movie["prdtYear"],
        "openDt": movie["openDt"],
        "prdtStatNm":movie["prdtStatNm"],
        "nationAlt":movie["nationAlt"],
        "genreAlt":movie["genreAlt"],
        "repNationNm":movie["repNationNm"],
        "repGenreNm":movie["repGenreNm"],
        "directors": directors,
        "companies": companies
    })

df = pd.DataFrame(movie_data)
df.to_csv("/Users/woorek/Downloads/tmp1.csv",index=False)