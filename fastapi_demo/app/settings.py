from pydantic_settings import BaseSettings  


class Configs(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_ROOT_PASSWORD:str
    MYSQL_HOST: str 
    MYSQL_PORT: int 
    MYSQL_DB: str


    class Config:
        env_file = ".env"

config = Configs()

# NOTE: airflow-> helm chart에서 정의