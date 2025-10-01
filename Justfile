# Copy project files to ESP32
deploy PORT:
	uv run mpremote connect {{PORT}} fs cp -r chip/* :/ && uv run mpremote connect {{PORT}} fs cp -r common :/

desktop:
    uv run desktop/main.py

