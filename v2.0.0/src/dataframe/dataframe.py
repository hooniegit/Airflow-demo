# module import
import pandas as pd
import json

# 파일 불러오기
for page in range (1, 11):
    file_path = f"/Users/kimdohoon/Desktop/movie/2023/KOBIS_MOVIE_LIST_2023_{page}.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    df_test = pd.json_normalize(data["movieListResult"]["movieList"])
    df_test["director"] = df_test["directors"].apply(lambda x: x[0]["peopleNm"] if len(x) != 0 else None)
    df_test["company"] = df_test["companys"].apply(lambda x: x[0]["companyNm"] if len(x) != 0 else None)
    df_test.drop(columns=["directors", "companys"], inplace=True)
    # print(df_test)

    parquet_filename = f"/Users/kimdohoon/Desktop/movie/parquet/KOBIS_MOVIE_LIST_2023_{page}.parquet"
    df_test.to_parquet(parquet_filename, index=False)
    print(f"Parquet 파일 '{parquet_filename}'이 저장되었습니다.")

# trying to import the above resulted in these errors:
#  - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
#  - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.