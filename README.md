# Linux System Control Application  

This project is a **Linux System Control Application** built using PyQt5. It provides a graphical user interface (GUI) to manage various aspects of a Linux system, such as display brightness, battery status, network settings, system monitoring, package management, and file system browsing.  

---

## **Features**  

### **Tabs**
1. **Power Tab**  
   - Displays battery information (status, capacity, voltage, etc.) by reading from `/sys/class/power_supply/BAT0/`.  

2. **Network Tab**  
   - Provides an interface to view and manage network connections (future implementation planned).  

3. **Monitor Tab**  
   - Displays CPU, memory, and disk usage in real-time (future implementation planned).  

4. **Package Manager Tab**  
   - Provides a basic interface for managing installed packages on your Linux system (e.g., updates and removals).  

5. **File System Tab**  
   - Allows browsing and managing files in the system (future implementation planned).  

6. **Display Tab**  
   - Adjusts the screen brightness using `brightnessctl`.  
   - Brightness slider operates in 10% increments for precision.  

---

## **Prerequisites**  

### **System Requirements**
- Linux-based OS  
- Python 3.7 or higher  

### **Dependencies**
1. **PyQt5**  
   Install PyQt5 using:  
   ```bash
   pip install PyQt5
   ```
   
2. **brightnessctl**  
   Install `brightnessctl` for brightness control:  
   ```bash
   sudo apt install brightnessctl
   ```

---

## **Installation**  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/linux-system-control.git
   cd linux-system-control
   ```

2. Install Python dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**  

1. **Run the Application**:  
   ```bash
   python main.py
   ```

2. **Keyboard Shortcut**:  
   - **Ctrl+Q**: Exit the application.  

3. **Tabs Overview**:  
   - Use the tabs to navigate between functionalities.  

---

## **Project Structure**  

```
linux-settings/
├── main.py                   # Entry point for the application
├── ui/
│   ├── main_window.py        # Main window logic
│   ├── main_window.ui        # Main window UI design
│   └── tabs/                 # Directory for individual tab implementations
│       ├── power_tab.py      # Power/Battery management
│       ├── network_tab.py    # Network settings (future feature)
│       ├── monitor_tab.py    # System monitor (future feature)
│       ├── package_tab.py    # Package manager interface (future feature)
│       ├── file_system_tab.py# File system browser (future feature)
│       └── display_tab.py    # Display brightness control
├── controllers/              # Directory for backend controllers (business logic)
│   ├── audio_controller.py   # Controls system audio settings
│   ├── base_controller.py    # Base class for reusable controller methods
│   ├── display_controller.py # Manages display-related actions like brightness
│   ├── network_controller.py # Handles network configurations and queries
│   ├── power_controller.py   # Manages power and battery-related operations
│   ├── system_monitor.py     # Collects system resource data (CPU, memory, etc.)
│   └── user_management.py    # Placeholder for user management operations
├── resources/                # Directory for additional project resources
│   └── icons/                # Icons used in the application
│       ├── light_mode.png    # Icon for light mode
│       ├── dark_mode.png     # Icon for dark mode
│       └── other icons...    # Additional UI icons
├── README.md                 # Project documentation
├── LICENSE                   # License information
└── requirements.txt          # Python dependencies
```

---

## **Display Brightness Control**  

The **Display Tab** uses `brightnessctl` for managing screen brightness.  
- The brightness slider operates in **steps of 10%**.  
- You can adjust the brightness dynamically and apply changes with the **Set Brightness** button.  
- The **Refresh** button syncs the slider with the current system brightness.  

---

## **Battery Management**  

The **Power Tab** displays full battery information by reading files in `/sys/class/power_supply/BAT0/`. It includes:  
- Battery status (charging, discharging, or full).  
- Capacity, voltage, and power usage.  
- Manufacturer details (if available).  

---

## **Contributing**  

Contributions are welcome! Here’s how you can help:  
1. Fork the repository.  
2. Create a new branch for your feature.  
3. Submit a pull request.  

---

## **License**  

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## **Future Enhancements**  
- **Network Management**: View and configure network connections.  
- **System Monitoring**: Real-time monitoring of CPU, memory, and disk usage.  
- **Package Management**: Seamless integration with package managers (e.g., apt, dnf, pacman).  
- **File System Exploration**: Add functionality for browsing and managing files.  

Feel free to suggest additional features or open issues for bugs.  

--- 

## **Screenshots**  

![Main Window](screenshot_main_window.png)  
*Example of the main window with all tabs.*  

![Display Tab](screenshot_display_tab.png)  
*Brightness control using the Display tab.*  

---

## **Support**  

If you encounter any issues or have questions, feel free to reach out via GitHub Issues.