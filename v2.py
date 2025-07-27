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
import os
from datetime import datetime
from typing import Optional, Dict, Any

import cv2
import numpy as np
import requests
from PIL import Image

# Configuration - Multiple sources for reliability
SOURCES = [
    {
        'name': 'SOHO_EIT_195',
        'url': 'https://soho.nascom.nasa.gov/data/realtime/eit_195/512/latest.jpg',
        'type': 'jpg'
    },
    {
        'name': 'SOHO_EIT_171',
        'url': 'https://soho.nascom.nasa.gov/data/realtime/eit_171/512/latest.jpg',
        'type': 'jpg'
    },
    {
        'name': 'SOHO_EIT_304',
        'url': 'https://soho.nascom.nasa.gov/data/realtime/eit_304/512/latest.jpg',
        'type': 'jpg'
    },
    {
        'name': 'NASA_SDO_HMI',
        'url': 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_hmiic.jpg',
        'type': 'jpg'
    }
]

REFRESH_SEC = 300
WIDTH = 80
HEIGHT = 24
ASCII_CHARS = " .:-=+*#%@"

# Photo saving options
SAVE_PHOTOS = True  # Set to False to disable photo saving
PHOTOS_DIR = "solar_photos"  # Directory to save photos


def clear_screen():
    """Clear terminal screen"""
    print("\033[2J\033[H", end="")


def setup_photos_directory():
    """Create directory for saving photos"""
    if SAVE_PHOTOS and not os.path.exists(PHOTOS_DIR):
        os.makedirs(PHOTOS_DIR)
        print(f"Created photos directory: {PHOTOS_DIR}")


def save_original_photo(image_data: np.ndarray, source_name: str) -> str:
    """Save the original solar photo with timestamp"""
    if not SAVE_PHOTOS:
        return ""

    try:
        # Create timestamp filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        clean_name = source_name.replace(' ', '_').replace('/', '_')
        filename = f"solar_{timestamp}_{clean_name}.jpg"
        filepath = os.path.join(PHOTOS_DIR, filename)

        # Save the image
        cv2.imwrite(filepath, image_data)
        return filepath

    except Exception as e:
        print(f"Error saving photo: {e}")
        return ""


def fetch_latest_image() -> Optional[tuple[np.ndarray, str, str]]:
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

                # Also keep original for saving
                original_image = Image.open(io.BytesIO(response.content))
                original_data = np.array(original_image)

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

            # Save original photo
            saved_path = save_original_photo(original_data, source['name'])

            print(f"Successfully loaded from {source['name']}")
            if saved_path:
                print(f"Original photo saved: {saved_path}")

            return cropped, source['name'], saved_path

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
    if SAVE_PHOTOS:
        print(f"Original photos will be saved to: {PHOTOS_DIR}/")
    print("Press Ctrl+C to exit\n")

    # Setup photos directory
    setup_photos_directory()

    current_source = "Unknown"

    while True:
        try:
            # Fetch and process image
            result = fetch_latest_image()

            if result is not None:
                image, source_name, saved_path = result
                current_source = source_name
                ascii_art = image_to_ascii(image)

                # Clear screen and display
                clear_screen()
                print("=== NEURAL ASCII TELESCOPE - LIVE SOLAR OBSERVATION ===")
                print(f"Source: {current_source}")
                if saved_path:
                    print(f"Photo saved: {os.path.basename(saved_path)}")
                print("=" * 60)
                print(ascii_art)
                print("=" * 60)
                print(f"Updated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
                print(f"Next refresh in {REFRESH_SEC} seconds")
                if SAVE_PHOTOS:
                    print(f"Photos saved in: {PHOTOS_DIR}/")
                print("Press Ctrl+C to exit")
            else:
                print("Failed to fetch image from all sources, retrying in 60 seconds...")
                time.sleep(60)
                continue

        except KeyboardInterrupt:
            print("\nShutting down telescope...")
            if SAVE_PHOTOS:
                print(f"Your solar photos are saved in: {PHOTOS_DIR}/")
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
            if SAVE_PHOTOS:
                print(f"Your solar photos are saved in: {PHOTOS_DIR}/")
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
