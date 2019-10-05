import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Google Cloud PlatformからダウンロードしたJSONファイルを指定
key_name = 'gspread-xxxxxxxxxxxx.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(key_name, scope)
gc = gspread.authorize(credentials)
sp = gc.open_by_key(sp_id)

sh = gc.create('A new spreadsheet')
sh.share('91katsuhisa@gmail.com', perm_type='user', role='writer')
print('https://docs.google.com/spreadsheets/d/' + sh.id)
