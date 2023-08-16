import pandas as pd
import json, sys

# 외부 입력 변수
# year = sys.argv[1]
# cnt = sys.argv[2]
year = 2022
cnt = 1941

base_image_url = "https://image.tmdb.org/t/p/original"

# 파일 불러오기
for page in range (1, cnt+1):
    file_path = f"/Users/kimdohoon/Desktop/TMDB/JSON/{year}/TMDB_movie_{year}_{page}.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    df_test = pd.json_normalize(data["results"])

    poster_path = str(df_test["poster_path"])
    poster_endpoint = df_test["poster_path"] if poster_path != 'None' else '/error'
    poster_image_url = base_image_url + poster_endpoint

    df_test["poster_path"] = poster_image_url

    parquet_filename = f"/Users/kimdohoon/Desktop/TMDB/dataframe/parquet/{year}/TMDB_movie_{year}_{page}.parquet"
    df_test.to_parquet(parquet_filename, index=False)
    print(f"Parquet 파일 '{parquet_filename}'이 저장되었습니다.")

# trying to import the above resulted in these errors:
#  - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
#  - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.