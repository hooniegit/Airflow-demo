# 🔬 Intro
airflow를 docker container 환경에서 빌드하고, 간단한 airflow DAG 작성 실습을 진행합니다.

### about airflow
- airflow는 데이터 오케스트레이션 툴이며, 오픈 소스로 제공됩니다.
- python 환경에서 작성되는 dag 스크립트를 통해 (특정 작업을 수행하는) 파이프라인을 설계하고 일정에 따라 작업을 스케줄링(진행 및 조정)할 수 있습니다.
- airflow는 파이프라인 진행 상황 및 로그 정보를 웹 대시보드를 통해 간단히 확인할 수 있습니다.

### need to know
- 

### target
- dockerfile 및 docker-compose.yml 파일을 통해 airflow를 실행하는 docker-container을 빌드합니다.
- 

# 🛠️ build & run docker container
| docker-compose.yml 파일이 있는 경로에서 실행
``` bash
$ docker compose up -d 
```

# 🪧 notice
1. This repository runs in python3.10
2. `/src/create_table` 이하의 모든 스크립트는 aws s3 접속을 위한 key 정보를 포함하고 있습니다.
해당 레포지토리에서는 AWS와 관련된 내용에 대해서는 다루지 않습니다. 이 점을 참조 부탁드립니다.
또한 config parser와 관련된 내용도 다루지 않습니다.