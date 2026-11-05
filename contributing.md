# Contributing to ASCII Telescope

Thanks for your interest. Contributions from developers, astronomers and space fans are welcome.

## Getting started

1. Fork the repository on GitHub.
2. Clone your fork and create a branch for your change.
3. Make your changes and test them.
4. Open a pull request.

## Development setup

```bash
git clone https://github.com/<your-username>/ascii_telescope.git
cd ascii_telescope
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python ascii_telescope.py
```

## Code style

- Follow PEP 8.
- Use meaningful names and add docstrings to functions.
- Keep functions small and focused.
- Handle network and image errors gracefully.

## Feature ideas

High priority:

- Color support for different solar features
- Configuration file or command-line flags
- Clearer error messages

Medium priority:

- Historical image playback
- More wavelengths (171, 193, 211 angstrom)
- Solar flare alerts
- Exporting frames to files

Low priority:

- A web version
- Solar weather data overlay
- Interactive zoom and pan

## Adding data sources

- Use only publicly available images.
- Add proper attribution to the README.
- Handle failures so the telescope falls back to the next source.
- Keep image handling consistent with the existing sources.

## Before you submit

- Run the telescope through at least one full refresh cycle.
- Test network failures and bad image data.
- Try different terminal sizes.
- Update the README and `requirements.txt` if you add features or dependencies.
- Write clear commit messages, for example `Add: NOAA SUVI 304 source` or `Fix: handle corrupted image data`.

## Reporting issues

Include your Python version, operating system, terminal type and size, the full error traceback and steps to reproduce.

## Background reading

- **SDO (Solar Dynamics Observatory):** NASA's solar observation mission.
- **HMI (Helioseismic and Magnetic Imager):** the SDO instrument behind the continuum and magnetogram images.
- **Sunspots:** dark regions of intense magnetic activity.
- **Solar flares:** sudden releases of magnetic energy.

## Code of conduct

Be respectful, keep feedback constructive and help others learn.
