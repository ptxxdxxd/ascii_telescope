# ASCII Telescope

[![tests](https://github.com/ptxxdxxd/ascii_telescope/actions/workflows/tests.yml/badge.svg)](https://github.com/ptxxdxxd/ascii_telescope/actions/workflows/tests.yml)

Watch the Sun in your terminal. ASCII Telescope downloads the latest public solar images from NASA and NOAA and redraws them as ASCII art, refreshing every five minutes.

The frame layout looks like this:

```
=== ASCII TELESCOPE - LIVE SOLAR OBSERVATION ===
Source: NASA SDO HMI Continuum
============================================================
<80 x 24 ASCII rendering of the solar disk>
============================================================
Updated: <time> UTC
Next refresh in 300 seconds
```

## How it works

1. **Fetch.** Tries each image source in order and uses the first one that answers:
   - NASA SDO HMI Continuum (visible-light solar surface)
   - NASA SDO HMI Magnetogram (magnetic field)
   - NOAA GOES SUVI 171 (extreme ultraviolet, fallback)
2. **Prepare.** Converts the image to grayscale and crops it to a centered square.
3. **Convert.** Resizes it to 80 x 24 and maps each pixel's brightness to one of ten characters, from ` ` (dark) to `@` (bright).
4. **Display.** Clears the terminal, prints the frame with its source and time, and waits for the next refresh. If every source fails it retries after a minute.

## Quick start

Requires Python 3.9 or newer.

```bash
git clone https://github.com/ptxxdxxd/ascii_telescope.git
cd ascii_telescope
pip install -r requirements.txt
python ascii_telescope.py
```

Press `Ctrl+C` to stop.

## Two versions

| File | Image sources | Extra |
| --- | --- | --- |
| `ascii_telescope.py` | NASA SDO HMI Continuum, SDO HMI Magnetogram, NOAA GOES SUVI 171 | |
| `v2.py` | SOHO EIT 195, 171 and 304, then NASA SDO HMI Continuum | Saves each original image to `solar_photos/` with a timestamp |

Run v2 with `python v2.py`. Set `SAVE_PHOTOS = False` at the top of the file to turn off image saving.

## Configuration

Edit the constants at the top of either script:

- `REFRESH_SEC`: seconds between updates (default 300). Please keep this polite to NASA and NOAA servers.
- `WIDTH` and `HEIGHT`: size of the ASCII frame (default 80 x 24).
- `ASCII_CHARS`: the brightness ramp, darkest first (default `" .:-=+*#%@"`).
- `SOURCES`: the list of image URLs to try, in order.

## Tips

- Use a terminal at least 80 x 24 with a monospace font.
- Dark terminal themes make the solar disk easier to read.

## Dependencies

`opencv-python-headless`, `numpy`, `requests` and `Pillow` (see `requirements.txt`). The headless OpenCV build is enough, since the scripts only resize and save images and never open a window.

## Tests

```bash
pip install -r requirements.txt pytest
pytest
```

The tests run offline. They fake the image sources to check the fallback order, the square crop and that a corrupt image is skipped, and they check the ASCII frame's size and brightness mapping. GitHub Actions runs them on Python 3.9, 3.11 and 3.13 for every pull request. `v2.py` is only byte-compiled in CI, not tested.

## Data credits

Solar imagery is public data from:

- [NASA Solar Dynamics Observatory](https://sdo.gsfc.nasa.gov/)
- [SOHO](https://soho.nascom.nasa.gov/), a mission of ESA and NASA
- [NOAA Space Weather Prediction Center](https://www.swpc.noaa.gov/)

## Ideas

- Color output for different wavelengths
- Command-line flags instead of editing constants
- Saving ASCII frames to text files
- Merging `v2.py` into the main script as an option

## License

MIT. See [License.txt](License.txt).
