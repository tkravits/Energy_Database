import requests, zipfile, io
import pandas as pd

zip_file_url = 'https://www.eia.gov/electricity/data/eia923/xls/f923_2020.zip'

r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
df1 = pd.read_excel(z.open(z.namelist()[0]))