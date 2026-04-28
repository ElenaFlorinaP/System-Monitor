# System Monitor with Discord Alerts

A lightweight, standalone desktop application built in Python that monitors system resources (CPU, RAM) and network status, sending automated real-time alerts directly to a Discord server via Webhooks.

## Features

* **Resource Monitoring:** Tracks CPU and RAM usage in real-time.
* **Alerts:** Automatically sends a Discord message if CPU or RAM usage exceeds the 85% threshold.
* **Network Tracking:** Detects network failures and safely handles them. Sends a "Reconnected" alert when the internet comes back online.
* **User-Friendly GUI:** An easy-to-use interface built with Tkinter that allows users to input their Discord Webhook URL.
* **Standalone Executable:** Fully packed into a `.exe` file. Users can run the app instantly without needing to install Python or any dependencies.

## How to Use (For Regular Users)

1. Download the executable file (` .exe`).
2. Run the application.
3. Paste your Discord Webhook URL into the text box.
4. Click **START**.
5. The app will run in the background and notify you on Discord if your PC needs attention!

## How to Use (For Developers)

If you want to view or modify the code, follow these steps:

1. Clone this repository.
2. Install the required Python libraries:
    ```bash
    pip install psutil requests
    ```
3. Run the graphical interface
    ```bash
    python gui.py
    ```

## Built with

* **Python**
* **Tkinter (Graphical User Interface)**
* **psutil (Hardware monitoring)**
* **requests (Discord Webhook integration)**
* **PyInstaller (Executable generation)**
