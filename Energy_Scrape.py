import requests, zipfile, io
import pandas as pd

# sets the download url for the zip file
zip_file_url = 'https://www.eia.gov/electricity/data/eia923/xls/f923_2020.zip'

# uses the request library to download the zip file and read it as an excel spreadsheet
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
df = pd.read_excel(z.open(z.namelist()[0]), sheet_name=None)

# loops through all the sheets in an excel file and appends them to one dataframe
full_table = pd.DataFrame()
for name, sheet in df.items():
    sheet['sheet'] = name
    sheet = sheet.rename(columns=lambda x: x.split('\n')[-1])
    full_table = full_table.append(sheet)

full_table.reset_index(inplace=True, drop=True)

#dfs = [x for _, x in full_table.groupby('sheet')]
