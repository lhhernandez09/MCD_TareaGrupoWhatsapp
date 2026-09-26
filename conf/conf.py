from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests

def create_onedrive_direct_download(shared_url):
    """Añade el parámetro de descarga a un enlace compartido de SharePoint."""
    url = urlsplit(shared_url)
    query = dict(parse_qsl(url.query))
    query["download"] = "1"
    return urlunsplit((url.scheme, url.netloc, url.path, urlencode(query), url.fragment))

# 1. Paste your copied OneDrive share link here
shared_link = "https://unisonmx-my.sharepoint.com/:t:/g/personal/a219210858_unison_mx/IQBh3amADe8IQI1Tl29bHYdcAdSShZtBHYKaNZ29dm45ZG0?e=8fY8OB"

# 2. Convert to direct download link
download_url = create_onedrive_direct_download(shared_link)

# 3. Define the destination in the project's raw-data directory
raw_data_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
raw_data_dir.mkdir(parents=True, exist_ok=True)
local_filename = raw_data_dir / "chat.txt"  # Change extension to match your file type

print("Downloading file...")
response = requests.get(download_url, timeout=60)
response.raise_for_status()

# 4. Save the binary content locally
with open(local_filename, 'wb') as file:
    file.write(response.content)
print(f"Success! File saved as {local_filename}")
