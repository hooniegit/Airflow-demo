# 모듈 import
import requests, json
from datetime import datetime as dt

# requests informations
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?"
key = "bedea8450005818cf88ff722e915dd14"

# url structure create
url_test = url + f"key={key}&itemPerPage=100&openStartDt=2023&curPage=1"
response = requests.get(url_test)
# 파일 저장
date = dt.now().strftime("%y%m%d")
dir = f"/Users/kimdohoon/Desktop/movie/2023/KOBIS_MOVIE_LIST_{date}.json"
with open (dir, "w", encoding="utf-8") as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)