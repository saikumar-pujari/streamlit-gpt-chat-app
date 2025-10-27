
# Streamlit Application

## Overview
This is a simple Streamlit web application prototype created for testing purposes. The app demonstrates basic Streamlit components and serves as a foundation for further development.

## Project Structure
```
frontend/
├── env/
│   ├── main.py          # Main Streamlit application
│   ├── Scripts/         # Virtual environment executables
│   └── Lib/             # Python packages (streamlit, pandas, etc.)
└── README.md            # This file
```

## Prerequisites
- Python 3.x
- Virtual environment (`env`) with Streamlit installed

## Installation

1. **Activate the virtual environment:**
   ```bash
   # On Windows (CMD)
   env\Scripts\activate.bat
   
   # On Windows (PowerShell)
   env\Scripts\Activate.ps1
   ```

2. **Verify Streamlit is installed:**
   ```bash
   streamlit --version
   ```

## How to Run

### Method 1: Using Streamlit Command (Recommended)
From the `frontend` directory with the virtual environment activated:
```bash
streamlit run env\main.py
```

### Method 2: Using Python Module
```bash
python -m streamlit run env\main.py
```

### Method 3: Navigate to the env folder
```bash
cd env
streamlit run main.py
```

## Accessing the Application
Once the app is running, it will automatically open in your default web browser. If it doesn't, you can access it at:
- **Local URL:** http://localhost:8501
- **Network URL:** Will be displayed in the terminal

## Application Features
The current prototype includes:
- **Title:** Main heading for the application
- **Subheader:** Secondary heading with creator information
- **Text Display:** Static text content
- **Write Component:** Dynamic content display

## Troubleshooting

### Error: "File does not exist: main.py"
**Solution:** Make sure you're specifying the correct path. The file is located in the `env` folder, so use:
```bash
streamlit run env\main.py
```

### Error: "streamlit is not recognized"
**Solution:** Activate the virtual environment first:
```bash
env\Scripts\activate.bat
```

### Port Already in Use
If port 8501 is already in use, you can specify a different port:
```bash
streamlit run env\main.py --server.port 8502
```

## Stopping the Application
Press `Ctrl + C` in the terminal to stop the Streamlit server.

## Development
To modify the application, edit the `env/main.py` file. Streamlit automatically detects changes and will prompt you to rerun the app in your browser.

## Next Steps
- Add more Streamlit components (charts, dataframes, widgets)
- Implement data visualization features
- Add user input forms and interactivity
- Connect to external data sources or APIs

## Dependencies
Main packages installed in the virtual environment:
- streamlit
- pandas
- numpy
- altair
- pillow
- pyarrow

For a complete list, check the `env/Lib/site-packages` directory.

---

**Created:** October 2025  
**Status:** Prototype/Testing Phase

