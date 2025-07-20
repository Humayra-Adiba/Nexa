#  Nexa - Your Nexa Voice Assistant 

Nexa is a modular, cross-platform Python voice assistant that can perform various tasks through natural voice commands. Built with a clean, maintainable architecture for easy extension and customization.

## Features

### Core Functionality
- **Voice Recognition** - Advanced speech-to-text processing
- **Text-to-Speech** - Natural voice responses
- **Memory System** - Remember and recall information
- **Time & Date** - Get current time and date
- **Volume Control** - Adjust system volume

### Search & Information
- **Google Search** - "search google about..."
- **YouTube Search** - "play a song..."
- **Wikipedia** - "tell me about..."

### Application Control
- **Launch Apps** - "open chrome", "open terminal", "open files"
- **Close Apps** - "close chrome", "close tab"
- **Minimize Windows** - "minimize window"

### Memory & Reminders
- **Save Memories** - "remember that I have a meeting tomorrow"
- **Recall Memories** - "what do you remember"

## Project Structure

```
Nexa/
├── nexa.py                 # Main application entry point
├── config/
│   └── settings.py         # Configuration and settings
├── modules/
│   ├── apps/
│   │   └── launchapp.py    # Application launching/control
│   ├── search/
│   │   └── search.py       # Web search functionality
│   ├── memory/
│   │   └── memory_manager.py # Memory/reminder system
│   ├── speech/
│   │   └── speech_manager.py # Speech recognition/TTS
│   └── system/
│       └── system_utils.py  # System utilities
├── data/
│   └── Remember.txt        # Stored memories
├── tests/
├── utils/
└── nexa_env/              # Virtual environment
```

## Installation

### Prerequisites
- Python 3.7+
- Linux/Windows/macOS
- Microphone and speakers

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Nexa
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv nexa_env
   source nexa_env/bin/activate  # Linux/Mac
   # or
   nexa_env\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Nexa:**
   ```bash
   python nexa.py
   ```

## Usage

### Wake Up Nexa
Say any of these wake words:
- **"wake up"**
- **"hey nexa"**
- **"nexa"**

### Voice Commands

#### Application Control
```
"open chrome"          # Launch Google Chrome
"open terminal"        # Open terminal
"open files"           # Open file manager
"open calculator"      # Launch calculator
"close tab"            # Close browser tab
"minimize window"      # Minimize current window
```

#### Search & Information
```
"search google about artificial intelligence"
"play a song by Taylor Swift"
"tell me about Python programming"
"what time is it"
```

#### Memory System
```
"remember that I have a meeting at 3 PM"
"what do you remember"
```

#### System Control
```
"increase volume"
"decrease volume"
"finally sleep"        # Exit Nexa
```

## Configuration

Edit `config/settings.py` to customize:
- App dictionary for different applications
- Audio settings (language, timeout)
- File paths and directories
- Wake words and sleep commands

## Development

### Adding New Features

1. **Create a new module** in the appropriate `modules/` subdirectory
2. **Update imports** in `nexa.py`
3. **Add command handling** in the main loop
4. **Update configuration** if needed

### Module Structure
Each module should follow this pattern:
```python
class ModuleName:
    def __init__(self):
        # Initialize module
        pass
    
    def method_name(self, query):
        # Handle specific functionality
        return success, message
```

## Troubleshooting

### Common Issues

1. **Audio Issues:**
   - Check microphone permissions
   - Verify speakers/headphones are working
   - Install `pulseaudio` on Linux if needed

2. **Module Import Errors:**
   - Ensure you're running from the project root
   - Check virtual environment is activated
   - Verify all dependencies are installed

3. **App Launch Issues:**
   - Update app dictionary in `config/settings.py`
   - Check if applications are installed
   - Verify application command names

## Requirements

- `speech_recognition`
- `gtts`
- `playsound`
- `pyautogui`
- `pywhatkit`
- `wikipedia`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.

---

**Enjoy using Nexa! **
