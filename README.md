# QR-code-Generator

Modern QR Code Generator with a beautiful graphical user interface.

## Features

- Generate QR codes from URLs
- Modern and user-friendly interface
- Real-time QR code generation
- Save QR codes as PNG files
- High-quality QR code output
- Error correction support
- Responsive design
- Status feedback
- Input validation

## Requirements

- Python 3.8 or newer
- PySide6 (Qt for Python)
- qrcode library
- Pillow (PIL)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/szpuszi/szpuszi-QR-Generator.git
cd szpuszi-QR-Generator
```

2. Install required packages:
```bash
pip install PySide6
pip install qrcode
pip install Pillow
```

## Usage

1. Run the program:
```bash
python qr_generator.py
```

2. In the program interface:
   - Enter a URL in the input field
   - Click "Generate" to create the QR code
   - Click "Save" to save the QR code as a PNG file

## How It Works

1. The program creates a modern GUI using PySide6
2. When you enter a URL, it generates a QR code using the qrcode library
3. The QR code is displayed in the interface
4. You can save the generated QR code as a PNG file

## Technical Details

### QR Code Settings
- Version: 1 (automatically adjusts if needed)
- Error Correction: Level L (7% recovery)
- Box Size: 10 pixels
- Border: 4 boxes
- Colors: Black and white

### Interface Features
- Modern, clean design
- Responsive layout
- Input validation
- Status messages
- Error handling
- File save dialog
- High-quality image scaling

## Security Features

- Input validation
- Error handling
- Safe file operations
- Graceful error messages
- Resource cleanup

## Contributing

Feel free to submit issues and enhancement requests!

## Credits

Created by [szpuszi](https://github.com/szpuszi)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
