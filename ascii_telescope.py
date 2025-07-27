#!/usr/bin/env python3
"""
Neural ASCII Telescope
Real-time solar observations in ASCII art

Display live solar images from NASA's Solar Dynamics Observatory
directly in your terminal using ASCII character mapping.

Usage: python telescope.py
"""

import io
import time
import sys
from typing import Optional, Dict, Any

import cv2
import numpy as np
import requests
from PIL import Image

# Configuration - Multiple sources for reliability
SOURCES = [
    {
        'name': 'NASA SDO HMI Continuum',
        'url': 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_hmiic.jpg',
        'type': 'jpg'
    },
    {
        'name': 'NASA SDO HMI Magnetogram', 
        'url': 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_hmib.jpg',
        'type': 'jpg'
    },
    {
        'name': 'SpaceWeatherLive HMI',
        'url': 'https://services.swpc.noaa.gov/images/animations/suvi/primary/171/latest.png',
        'type': 'png'
    }
]

REFRESH_SEC = 300
WIDTH = 80  
HEIGHT = 24
ASCII_CHARS = " .:-=+*#%@"

def clear_screen():
    """Clear terminal screen"""
    print("\033[2J\033[H", end="")

def fetch_latest_image() -> Optional[tuple[np.ndarray, str]]:
    """Fetch the latest solar image from available sources"""
    
    for source in SOURCES:
        try:
            print(f"Trying {source['name']}...")
            
            # Add headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(source['url'], timeout=30, headers=headers)
            response.raise_for_status()
            
            # Handle different image formats
            if source['type'] in ['jpg', 'jpeg', 'png']:
                # Load image using PIL
                image = Image.open(io.BytesIO(response.content))
                # Convert to grayscale numpy array
                if image.mode != 'L':
                    image = image.convert('L')
                data = np.array(image, dtype=np.float32)
                
            else:
                print(f"Unsupported format: {source['type']}")
                continue
            
            # Validate image data
            if data is None or data.size == 0:
                print(f"No valid image data from {source['name']}")
                continue
                
            # Handle any NaN values
            data = np.nan_to_num(data, nan=0.0)
            
            # Crop to central square to avoid artifacts
            h, w = data.shape
            side = min(h, w)
            y0, x0 = (h - side) // 2, (w - side) // 2
            cropped = data[y0:y0 + side, x0:x0 + side]
            
            print(f"Successfully loaded from {source['name']}")
            return cropped, source['name']
            
        except requests.RequestException as e:
            print(f"Network error with {source['name']}: {e}")
            continue
        except Exception as e:
            print(f"Error processing {source['name']}: {e}")
            continue
    
    print("All sources failed!")
    return None

def image_to_ascii(image: np.ndarray) -> str:
    """Convert image to ASCII art"""
    try:
        # Resize image
        resized = cv2.resize(image, (WIDTH, HEIGHT))
        
        # Normalize to 0-1 range
        img_min, img_max = resized.min(), resized.max()
        if img_max > img_min:
            normalized = (resized - img_min) / (img_max - img_min)
        else:
            normalized = np.zeros_like(resized)
        
        # Convert to ASCII
        ascii_image = []
        for row in normalized:
            ascii_row = ""
            for pixel in row:
                char_index = int(pixel * (len(ASCII_CHARS) - 1))
                char_index = max(0, min(char_index, len(ASCII_CHARS) - 1))
                ascii_row += ASCII_CHARS[char_index]
            ascii_image.append(ascii_row)
        
        return "\n".join(ascii_image)
        
    except Exception as e:
        print(f"Error converting to ASCII: {e}")
        return "Error processing image"

def run_stream():
    """Main streaming loop"""
    print("=== Neural ASCII Telescope ===")
    print("Displaying live solar observations from multiple sources")
    print("Press Ctrl+C to exit\n")
    
    current_source = "Unknown"
    
    while True:
        try:
            # Fetch and process image
            result = fetch_latest_image()
            
            if result is not None:
                image, source_name = result
                current_source = source_name
                ascii_art = image_to_ascii(image)
                
                # Clear screen and display
                clear_screen()
                print("=== NEURAL ASCII TELESCOPE - LIVE SOLAR OBSERVATION ===")
                print(f"Source: {current_source}")
                print("=" * 60)
                print(ascii_art)
                print("=" * 60)
                print(f"Updated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
                print(f"Next refresh in {REFRESH_SEC} seconds")
                print("Press Ctrl+C to exit")
            else:
                print("Failed to fetch image from all sources, retrying in 60 seconds...")
                time.sleep(60)
                continue
                
        except KeyboardInterrupt:
            print("\nShutting down telescope...")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Retrying in 30 seconds...")
            time.sleep(30)
            continue
        
        # Wait before next update
        try:
            time.sleep(REFRESH_SEC)
        except KeyboardInterrupt:
            print("\nShutting down telescope...")
            sys.exit(0)

if __name__ == "__main__":
    # Check dependencies
    try:
        import cv2
        import numpy as np
        import requests
        from PIL import Image
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install opencv-python numpy requests pillow")
        sys.exit(1)
    
    run_stream()
