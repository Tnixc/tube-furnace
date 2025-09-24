# Path to your project folder
FOLDER := "chip"

# Serial device (adjust as needed)

# Copy project files to ESP32
deploy PORT:
	mpremote connect {{PORT}} fs cp -r {{FOLDER}}/* :/

# Run main.py on ESP32
run PORT:
	mpremote connect {{PORT}} run {{FOLDER}}/main.py

desktop:
    uv run desktop/main.py

