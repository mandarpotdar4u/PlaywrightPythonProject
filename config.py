from dotenv import load_dotenv

load_dotenv()


class Settings:
    excel_config_path = 'data/testfile.xlsx'
    excel_sheet_name = 'LoginTest'

    json_config_path = 'data/Json_data.json'


settings = Settings()
