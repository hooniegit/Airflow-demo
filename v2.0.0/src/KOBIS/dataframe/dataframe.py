# module import
import pandas as pd
import json, os
from mysql import connector

config = {
    'user': 'root',
    'password': '1234',
    'host': '34.64.221.56',
    'database': 'cinema'
}
conn = connector.connect(**config)
cursor = conn.cursor()

cnt = 0
year = 2023
# year = 2022

# JSON 파일이 있는 디렉토리 경로
directory_path = f'/Users/kimdohoon/git/hooniegit/Airflow-demo/v2.0.0/datas/KOBIS/{year}'

# 디렉토리 내 모든 파일을 탐색
for filename in os.listdir(directory_path):
    cnt += 1
    if filename.endswith('.json'):
        json_file_path = os.path.join(directory_path, filename)
        with open(json_file_path, "r") as file:
            data = json.load(file)
            movieCd = data["movieInfoResult"]["movieInfo"]["movieCd"]
            if not movieCd : movieCd = None

            movieNm = data["movieInfoResult"]["movieInfo"]["movieNm"]
            if not movieNm : movieNm = None

            movieNmEn = data["movieInfoResult"]["movieInfo"]["movieNmEn"]
            if not movieNmEn : movieNmEn = None

            showTm  = data["movieInfoResult"]["movieInfo"]["showTm"]
            if not showTm : showTm = None

            prdtYear = data["movieInfoResult"]["movieInfo"]["prdtYear"]
            if not prdtYear : prdtYear = None

            openDt = data["movieInfoResult"]["movieInfo"]["openDt"]
            if not openDt : openDt = None

            typeNm = data["movieInfoResult"]["movieInfo"]["typeNm"]
            if not typeNm : typeNm = None

            nations = data["movieInfoResult"]["movieInfo"]["nations"]
            nationNm = [index["nationNm"] for index in nations] if len(nations) != 0 else None

            genres = data["movieInfoResult"]["movieInfo"]["genres"]
            genreNm = [index["genreNm"] for index in genres] if len(genres) != 0 else None

            directors = data["movieInfoResult"]["movieInfo"]["directors"]
            directorNm = [index["peopleNm"] for index in directors] if len(directors) != 0 else None

            actors = data["movieInfoResult"]["movieInfo"]["actors"]
            actorNm = [index["peopleNm"] for index in actors] if len(actors) != 0 else None

            # companyNm = data["movieInfoResult"]["movieInfo"]
            companys= data["movieInfoResult"]["movieInfo"]["companys"]
            companyNm = [index["companyNm"] for index in companys] if len(companys) != 0 else None
            companyPartNm = [index["companyPartNm"] for index in companys] if len(companys) != 0 else None

            QUERY = f"""INSERT INTO movie_data (
                        movieCd,
                        movieNm,
                        movieNmEn,
                        showTm,
                        prdtYear,
                        openDt,
                        typeNm,
                        nationNm,
                        genreNm,
                        directorNm,
                        actorNm,
                        companyNm,
                        companyPartNm
                        )
                        values (
                        "{movieCd}",
                        "{movieNm}",
                        "{movieNmEn}",
                        {showTm},
                        {prdtYear},
                        {openDt},
                        "{typeNm}",
                        "{nationNm}",
                        "{genreNm}",
                        "{directorNm}",
                        "{actorNm}",
                        "{companyNm}",
                        "{companyPartNm}"                        
                        )
                        """
            # print(QUERY)
            cursor.execute(QUERY)
            conn.commit()
            print(f"{cnt} 번째 파일 적재 완료")

# trying to import the above resulted in these errors:
#  - Missing optional dependency 'pyarrow'. pyarrow is required for parquet support. Use pip or conda to install pyarrow.
#  - Missing optional dependency 'fastparquet'. fastparquet is required for parquet support. Use pip or conda to install fastparquet.