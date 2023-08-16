import requests, json, sys

year = int(sys.argv[1])
language = "ko-KR"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMzllMGE3ZTBhZmRkNjg3ZDQ0Njc1NTVhNzA4NzIwNyIsInN1YiI6IjY0ZGMyY2M5Yjc3ZDRiMTE0MDE4YzAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sjjmrmLiPAw6lbU9NSLvhQlaFYli3rfCSKI-9Rpai-s"

for page in range(1, 501):

    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&language={language}&watch_region=KR&primary_release_year={year}&page={page}&sort_by=primary_release_date.desc"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers).json()
    path = f"/Users/kimdohoon/Desktop/TMDB/JSON/{year}/TMDB_movie_{year}_{page}.json"
    with open(path, "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        print(f"page {page} extract SUCCEED")