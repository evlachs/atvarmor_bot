import requests


req = requests.get('https://atvarmor.ru/wp-content/uploads/wpallexport/exports/b0f4f3b1e8ce9e67b54debacd69e5f48/current-parts.xml')
print(req.text)
