# 모듈 import
import requests, json
from datetime import datetime as dt

# requests informations
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?"
key = "bedea8450005818cf88ff722e915dd14"


for page in range(1, 1000):
    url_test = url + f"key={key}&itemPerPage=100&openStartDt=2023&curPage={page}"
    response = requests.get(url_test)
    dir = f"/Users/kimdohoon/Desktop/movie/2023/KOBIS_MOVIE_LIST_2023_{page}.json"
    with open (dir, "w", encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)