# Moon Phase Calendar Poster Generator

This Python script generates a full-year moon phase calendar poster for a specified year (default 2025) in A3 vertical format (~30cm x 42cm).  
It places daily moon phase images for each day of the year into a clean grid layout with Polish month and weekday labels.

---

## Features

- Creates an A3 sized poster image (300 DPI) with moon phase thumbnails for each day.
- Displays months and weekdays in Polish.
- Inserts a customizable header image at the top.
- Handles variable month lengths and correctly positions days and moon images.
- Automatically scales and arranges daily moon thumbnails with day numbers and weekdays.
- Outputs a high-quality PNG poster suitable for printing.

---

## Requirements

- Python 3.x
- Libraries:
  - `Pillow` (PIL)
  - `calendar` (built-in)
  - `datetime` (built-in)

Install Pillow via pip if you don’t have it:

```bash
pip3 install Pillow
````

---

## Configuration

Inside the script, you can configure the following parameters:

* `YEAR`: The calendar year to generate (default: 2025).
* `IMAGE_DIR`: Directory path where monthly moon phase images are stored, organized by English month names (e.g., `moon/images/June/`).
* `TOP_IMAGE_PATH`: Path to the top header image displayed at the poster's top.
* `OUTPUT_PATH`: File path for the saved poster PNG.
* Poster dimensions and DPI (default A3 size at 300 DPI).
* Margins and font sizes.
* Polish month names and weekday abbreviations.

Make sure moon phase images follow the naming pattern:
`YYYY-MM-DD.png` (e.g., `2025-06-04.png`) inside respective monthly folders.

---

## Usage

1. Prepare your moon phase images organized in folders by English month name inside `IMAGE_DIR`.
   Example folder structure:

   ```
   moon/images/January/
   moon/images/February/
   ...
   moon/images/December/
   ```

2. Place a header image at the path specified in `TOP_IMAGE_PATH`.

3. Run the script:

```bash
python3 moonphase_image_generator.py
```

4. The script generates the poster PNG file at the location defined by `OUTPUT_PATH`.

---

## How It Works

* Calculates the poster size and layout grid based on A3 paper size at 300 DPI.
* Loads and places a header image centered at the top.
* Iterates through all months and days of the specified year.
* For each day, it:

  * Draws the day number.
  * Loads the corresponding moon phase image and scales it to fit the grid cell.
  * Draws the abbreviated Polish weekday below the moon image.
* Renders all text and images on a black background with white font for clarity.
* Saves the final composed poster image as a high-resolution PNG.

---

## Notes

* The script tries to load common Windows fonts (`segoeui.ttf`, `calibri.ttf`, `tahoma.ttf`, `arial.ttf`).
  If none are found, it falls back to the default PIL font.
* Ensure the font files exist at `C:\Windows\Fonts\` or modify the font loading section to suit your OS.
* If the header image is missing, a red error message is drawn instead.
* Adjust margins, font sizes, and layout constants inside the script as needed.

---

## License

This project is for personal and educational use.
