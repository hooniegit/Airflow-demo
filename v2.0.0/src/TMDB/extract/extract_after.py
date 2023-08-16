import requests, json, sys

# 외부 입력 변수
year = int(sys.argv[1])
mid_num = int(sys.argv[2])
# year = 2023, 2022, 2021, ...
# mid_num = 500, 1000, 1500, ...

# 가장 마지막 release_date 반환
dir_mid = f"/Users/kimdohoon/Desktop/TMDB/JSON/{year}/TMDB_movie_{year}_{mid_num}.json"
with open(dir_mid, "r") as file:
    reference = json.load(file)

# API request 파라미터
language = "ko-KR"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMzllMGE3ZTBhZmRkNjg3ZDQ0Njc1NTVhNzA4NzIwNyIsInN1YiI6IjY0ZGMyY2M5Yjc3ZDRiMTE0MDE4YzAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sjjmrmLiPAw6lbU9NSLvhQlaFYli3rfCSKI-9Rpai-s"
date_lte = reference["results"][-1]["release_date"]
date_gte = f"{year}-01-01"

# 500 페이지까지 response 출력
for page in range(1, 501):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&language={language}&watch_region=KR&primary_release_date.lte={date_lte}&primary_release_date.gte={date_gte}&page={page}&sort_by=primary_release_date.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers).json()
    path = f"/Users/kimdohoon/Desktop/TMDB/JSON/{year}/TMDB_movie_{year}_{page + mid_num}.json"
    with open(path, "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        print(f"page {page + mid_num} extract SUCCEED")