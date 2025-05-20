import os
import requests
import datetime
import ephem

# Configuration
YEAR = 2025
HOUR = "19:00"
BASE_URL = "https://svs.gsfc.nasa.gov/api/dialamoon/"
SAVE_DIR = "moon/images"
os.makedirs(SAVE_DIR, exist_ok=True)

# Create list of full and new moon dates using ephem
def get_full_and_new_moon_dates(year):
    date = ephem.Date(f"{year}/1/1")
    end = ephem.Date(f"{year}/12/31")
    special_days = set()

    while date < end:
        next_new = ephem.localtime(ephem.next_new_moon(date)).date()
        next_full = ephem.localtime(ephem.next_full_moon(date)).date()
        special_days.add(next_new)
        special_days.add(next_full)
        date = ephem.Date(next_new + datetime.timedelta(days=1))
        date2 = ephem.Date(next_full + datetime.timedelta(days=1))
        date = max(date, date2)

    return special_days

# Download image helper
def download_image(api_date, save_path):
    url = f"{BASE_URL}{api_date}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_url = data["image"]["url"]

        image_response = requests.get(image_url)
        image_response.raise_for_status()

        with open(save_path, "wb") as f:
            f.write(image_response.content)

        print(f"Saved: {save_path}")
    except Exception as e:
        print(f"Error fetching {api_date}: {e}")

# Generate moon image for each day
special_days = get_full_and_new_moon_dates(YEAR)
start_date = datetime.date(YEAR, 1, 1)
end_date = datetime.date(YEAR, 12, 31)
delta = datetime.timedelta(days=1)
current = start_date

while current <= end_date:
    api_date = f"{current.isoformat()}T{HOUR}"

    month_name = current.strftime("%B")
    out_dir = os.path.join(SAVE_DIR, month_name)
    os.makedirs(out_dir, exist_ok=True)

    filename = f"{current.isoformat()}.png"
    save_path = os.path.join(out_dir, filename)

    # Always download — but use same timestamp if it's a new/full moon
    download_image(api_date, save_path)
    current += delta
