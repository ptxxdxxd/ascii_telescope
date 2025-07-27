Contributing to Neural ASCII Telescope
Thank you for your interest in contributing! This project welcomes contributions from developers, astronomers, and space enthusiasts.
Getting Started

Fork the repository on GitHub
Clone your fork locally
Create a new branch for your feature/fix
Make your changes
Test thoroughly
Submit a pull request

Development Setup
bash# Clone your fork
git clone https://github.com/yourusername/neural-ascii-telescope.git
cd neural-ascii-telescope

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the telescope
python telescope.py
Code Style

Follow PEP 8 Python style guidelines
Use meaningful variable names
Add docstrings to functions
Keep functions focused and small
Handle errors gracefully

Feature Ideas
High Priority

 Color support for different solar features
 Configuration file support
 Better error messages and user feedback
 Performance optimizations

Medium Priority

 Historical image playback mode
 Multiple wavelength support (171Å, 193Å, 211Å)
 Solar flare detection and alerts
 Export frames to image files

Low Priority

 Web interface version
 Real-time solar weather data overlay
 Interactive controls (zoom, pan)
 Sound alerts for solar events

Data Sources
When adding new data sources, ensure:

Images are publicly available
Proper attribution is included
Error handling for source failures
Consistent image format handling

Testing
Before submitting:

Test with different terminal sizes
Verify network error handling
Check memory usage during long runs
Test on different operating systems if possible

Submitting Changes

Create descriptive commit messages
Add: New NOAA solar data source
Fix: Handle corrupted image data gracefully  
Update: Improve ASCII character mapping

Update documentation

Update README.md if adding features
Add docstrings to new functions
Update requirements.txt if adding dependencies


Test thoroughly

Run the telescope for at least one full cycle
Test error conditions (network failures, bad data)
Verify ASCII output quality



Issue Reporting
When reporting issues, include:

Python version
Operating system
Terminal type/size
Error messages (full traceback)
Steps to reproduce

Astronomy Knowledge
While astronomy knowledge isn't required, understanding these concepts helps:

Solar Dynamics Observatory (SDO) - NASA's solar observation mission
HMI (Helioseismic and Magnetic Imager) - Instrument measuring solar magnetic fields
Solar granulation - Convective cells visible on solar surface
Sunspots - Dark regions of intense magnetic activity
Solar flares - Explosive releases of magnetic energy

Code of Conduct

Be respectful and inclusive
Focus on constructive feedback
Help others learn and contribute
Follow scientific accuracy when possible

Questions?
Feel free to open an issue for:

Feature requests
Bug reports
General questions
Astronomy discussions

Happy stargazing! 🌞
