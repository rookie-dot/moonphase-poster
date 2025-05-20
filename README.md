# NASA Moon Phase Poster Generator

This repository contains two Python scripts that allow you to:

1. **Download daily images of the Moon** from NASA's [Dial-A-Moon API](https://svs.gsfc.nasa.gov/api/dialamoon).
2. **Generate a printable A3-size Moon phase calendar poster** using the downloaded images.

## Features

* Automatically downloads high-resolution images of the Moon for each day of the selected year.
* Organizes images into appropriate directories by month.
* Generates a visually appealing A3-format calendar poster (29.7 x 42 cm) ready for print.
* Poster includes:

  * Date number above each Moon image.
  * Day of the week abbreviation below (e.g., PN, WT, ŚR, CZW, PT, SB, N – for Polish locale).
  * Centered title and high-quality layout suitable for wall display.

## Usage

### 1. Downloading the Images

Run the script:

```bash
python3 moonphase_downlaoder.py
```

This will fetch the Moon images for the selected year and save them into structured folders.

### 2. Generating the Poster

After all images are downloaded, run:

```bash
python3 moonphase_image_generator.py
```

This script will create a ready-to-print A3 poster as a high-resolution PDF or image file.

## Requirements

* Python 3.8+
* Required packages: `requests`, `Pillow`, `reportlab` (or other depending on implementation)

Install dependencies with:

```bash
pip3 install -r requirements.txt
```

## License

MIT License

## Credits

Data and images provided by [NASA's Scientific Visualization Studio](https://svs.gsfc.nasa.gov/).
