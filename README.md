# ascii_telescope
Live solar telescope in your terminal using ASCII art and NASA SDO data  Transform NASA solar images into beautiful terminal ASCII art in real-time  Terminal-based solar observatory streaming live ASCII art from space  🔴 Watch the Sun live: NASA SDO → ASCII art in your terminal
# 🌞 Neural ASCII Telescope

Real-time solar observations in your terminal using ASCII art. Watch the Sun live from NASA's Solar Dynamics Observatory (SDO) without leaving your command line!

![Demo](demo.gif)

## Features

- 🔴 **Live Solar Data** - Streams real-time images from NASA SDO
- 🎨 **ASCII Art Conversion** - Converts solar images to beautiful terminal art  
- 🌐 **Multiple Sources** - Automatic fallback between NASA and NOAA data feeds
- ⚡ **Lightweight** - Zero-cost monitoring, runs anywhere Python does
- 🛡️ **Robust** - Handles network failures and continues streaming
- 🎯 **Focus Mode** - Crops to central solar disk, avoiding limb artifacts

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/neural-ascii-telescope.git
cd neural-ascii-telescope

# Install dependencies
pip install -r requirements.txt

# Launch the telescope
python telescope.py
```

## Installation

### Requirements
- Python 3.7+
- Terminal with at least 80x24 character display

### Dependencies
```bash
pip install opencv-python numpy requests pillow
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python telescope.py
```

### Configuration
Edit the configuration section in `telescope.py` to customize:

- `REFRESH_SEC` - Update interval (default: 300 seconds)
- `WIDTH` / `HEIGHT` - ASCII art dimensions (default: 80x24)
- `ASCII_CHARS` - Character gradient for brightness mapping

## Data Sources

The telescope automatically tries multiple sources for maximum reliability:

1. **NASA SDO HMI Continuum** - High-resolution solar surface images
2. **NASA SDO HMI Magnetogram** - Magnetic field visualization  
3. **NOAA Space Weather** - Backup solar imagery

## How It Works

1. **Fetch** - Downloads latest solar images from NASA/NOAA APIs
2. **Process** - Crops to central disk and normalizes brightness
3. **Convert** - Maps pixel intensities to ASCII characters
4. **Display** - Renders live solar activity in your terminal

## Solar Features You'll See

- 🔴 **Sunspots** - Dark regions of intense magnetic activity
- ⚡ **Solar Granulation** - Convective cells on the solar surface
- 🌊 **Plasma Flows** - Dynamic movement of solar material
- 💥 **Active Regions** - Bright areas of magnetic complexity

## Troubleshooting

### Network Issues
The telescope automatically retries failed connections and switches between data sources.

### Display Problems
- Ensure terminal is at least 80x24 characters
- Use a monospace font for best results
- Try adjusting terminal contrast/brightness

### Performance
- Default 5-minute refresh balances data freshness with server load
- Reduce `REFRESH_SEC` for faster updates (be respectful to NASA servers!)

## Contributing

Contributions welcome! Ideas for enhancements:

- [ ] Color support for different solar features
- [ ] Historical image playback
- [ ] Solar flare detection alerts
- [ ] Multiple wavelength support (UV, X-ray)
- [ ] Export ASCII frames to files
- [ ] Web interface version

## Data Credits

Solar imagery courtesy of:
- **NASA Solar Dynamics Observatory (SDO)** - [sdo.gsfc.nasa.gov](https://sdo.gsfc.nasa.gov)
- **NOAA Space Weather Prediction Center** - [spaceweather.gov](https://spaceweather.gov)

## License

MIT License - feel free to fork, modify, and share!

## Astronomy Links

- [Solar Dynamics Observatory](https://sdo.gsfc.nasa.gov/) - NASA's premier solar observatory
- [Space Weather Live](https://spaceweatherlive.com/) - Real-time space weather data
- [SOHO Solar Images](https://soho.esac.esa.int/data/) - ESA/NASA solar observatory

---

*"The Sun, with all those planets revolving around it and dependent on it, can still ripen a bunch of grapes as if it had nothing else in the universe to do."* - Galileo Galilei
