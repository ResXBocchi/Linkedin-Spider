from decouple import config
search_query = 'site:linkedin.com/in AND "python developer" AND "Alagoas"'
username = config('EMAIL')
password = config('PASSWORD')
driver_path = config('DRIVER_PATH')