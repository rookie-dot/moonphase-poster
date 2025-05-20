import os
from PIL import Image, ImageDraw, ImageFont
import calendar
from datetime import datetime

# Configuration
YEAR = 2025
IMAGE_DIR = "moon/images"
TOP_IMAGE_PATH = os.path.join("moon/header", "moon-june.png")
OUTPUT_PATH = "moon_calendar_2025_poster_A3_vertical.png"

# Poster size A3 ~30cm x 42cm (portrait)
DPI = 300
POSTER_WIDTH_CM = 30
POSTER_HEIGHT_CM = 42
WIDTH_PX = int(POSTER_WIDTH_CM / 2.54 * DPI)
HEIGHT_PX = int(POSTER_HEIGHT_CM / 2.54 * DPI)

# Margins
LEFT_MARGIN_CM = 2
OTHER_MARGIN_CM = 3
LEFT_MARGIN_PX = int(LEFT_MARGIN_CM / 2.54 * DPI)
MARGIN_PX = int(OTHER_MARGIN_CM / 2.54 * DPI)
RIGHT_MARGIN_PX = MARGIN_PX
TOP_MARGIN_PX = MARGIN_PX
BOTTOM_MARGIN_PX = MARGIN_PX

# Layout constants
MONTH_LABEL_WIDTH = int(2.5 / 2.54 * DPI)
NUM_DAYS = 31
NUM_MONTHS = 12
GAP_X = 10
GAP_Y = 4
HEADER_HEIGHT = HEIGHT_PX // 3
CAL_TOP = TOP_MARGIN_PX + HEADER_HEIGHT
TEXT_MARGIN = 8  # Margin between text and moon image

# Font sizes
FONT_SIZE_MONTH = 28
FONT_SIZE_DAY = 16
FONT_SIZE_HEADER = 48
FONT_SIZE_WEEKDAY = 14

# Polish month names and weekdays
months_pl = [
    "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
    "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
]
weekday_pl = ["PN", "WT", "ŚR", "CZW", "PT", "SB", "N"]

# Font loading
possible_fonts = ["segoeui.ttf", "calibri.ttf", "tahoma.ttf", "arial.ttf"]

def load_font(fonts, size):
    for font_name in fonts:
        try:
            return ImageFont.truetype(os.path.join("C:\\Windows\\Fonts", font_name), size)
        except:
            continue
    return ImageFont.load_default()

font_month = load_font(possible_fonts, FONT_SIZE_MONTH)
font_day = load_font(possible_fonts, FONT_SIZE_DAY)
font_weekday = load_font(possible_fonts, FONT_SIZE_WEEKDAY)
font_header = load_font(possible_fonts, FONT_SIZE_HEADER)

# Grid layout
GRID_WIDTH = WIDTH_PX - MONTH_LABEL_WIDTH - LEFT_MARGIN_PX - RIGHT_MARGIN_PX
CELL_WIDTH = GRID_WIDTH // NUM_DAYS
CELL_HEIGHT = ((HEIGHT_PX - HEADER_HEIGHT - TOP_MARGIN_PX - BOTTOM_MARGIN_PX) // NUM_MONTHS)
GRID_X_OFFSET = LEFT_MARGIN_PX + MONTH_LABEL_WIDTH + (GRID_WIDTH - (CELL_WIDTH * NUM_DAYS)) // 2
THUMBNAIL_HEIGHT = CELL_HEIGHT - FONT_SIZE_DAY - TEXT_MARGIN - FONT_SIZE_WEEKDAY - (TEXT_MARGIN + 4)
THUMBNAIL_SIZE = (CELL_WIDTH - GAP_X, THUMBNAIL_HEIGHT)

# Create canvas
canvas = Image.new("RGB", (WIDTH_PX, HEIGHT_PX), (0, 0, 0))
draw = ImageDraw.Draw(canvas)

# Insert top image
if os.path.exists(TOP_IMAGE_PATH):
    top_img = Image.open(TOP_IMAGE_PATH).convert("RGB")
    ratio = min((WIDTH_PX - LEFT_MARGIN_PX - RIGHT_MARGIN_PX) / top_img.width, HEADER_HEIGHT / top_img.height)
    new_size = (int(top_img.width * ratio), int(top_img.height * ratio))
    top_img = top_img.resize(new_size)
    x_offset = (WIDTH_PX - new_size[0]) // 2
    y_offset = TOP_MARGIN_PX
    canvas.paste(top_img, (x_offset, y_offset))
else:
    draw.text((LEFT_MARGIN_PX, TOP_MARGIN_PX), "Missing photo for provided date", fill=(255, 0, 0), font=font_header)

# Draw months and images
for row, month in enumerate(months_pl):
    y = CAL_TOP + row * CELL_HEIGHT
    text_width = draw.textlength(month, font=font_month)
    draw.text((LEFT_MARGIN_PX + MONTH_LABEL_WIDTH - text_width - 40,
               y + (CELL_HEIGHT - FONT_SIZE_MONTH) // 4),
              month, fill=(255, 255, 255), font=font_month)

    month_eng = calendar.month_name[row + 1]
    num_days = calendar.monthrange(YEAR, row + 1)[1]
    month_dir = os.path.join(IMAGE_DIR, month_eng)

    for day in range(1, num_days + 1):
        x = GRID_X_OFFSET + (day - 1) * CELL_WIDTH
        date_obj = datetime(YEAR, row + 1, day)
        weekday = weekday_pl[date_obj.weekday()]
        filename = f"{YEAR}-{str(row + 1).zfill(2)}-{str(day).zfill(2)}.png"
        path = os.path.join(month_dir, filename)

        moon_img = None
        if os.path.exists(path):
            try:
                moon_img = Image.open(path).convert("RGB")
                moon_img.thumbnail(THUMBNAIL_SIZE)
            except Exception as e:
                print(f"Error loading {path}: {e}")

        # Calculate positions
        moon_img_height = moon_img.height if moon_img else THUMBNAIL_SIZE[1]
        moon_x = x + (CELL_WIDTH - THUMBNAIL_SIZE[0]) // 2
        moon_y = y + FONT_SIZE_DAY + TEXT_MARGIN

        # Draw day number
        day_text = str(day)
        day_width = draw.textlength(day_text, font=font_day)
        draw.text((x + (CELL_WIDTH - day_width) // 2, y), day_text, fill=(255, 255, 255), font=font_day)

        # Paste moon image
        if moon_img:
            canvas.paste(moon_img, (moon_x, moon_y))

        # Draw weekday
        weekday_width = draw.textlength(weekday, font=font_weekday)
        weekday_y = moon_y + moon_img_height + TEXT_MARGIN + 4
        draw.text((x + (CELL_WIDTH - weekday_width) // 2, weekday_y), weekday, fill=(255, 255, 255), font=font_weekday)

# Save final poster
canvas.save(OUTPUT_PATH)
print(f"Kalendarz zapisany jako: {OUTPUT_PATH}")
