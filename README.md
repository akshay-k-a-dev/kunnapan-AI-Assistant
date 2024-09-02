
# Kunnapan AI Assistant

Kunnapan AI Assistant is a Python-based voice assistant that leverages speech recognition and text-to-speech (TTS) to interact with users. The assistant captures audio input, processes the text, and responds with spoken output.

## Features

- **Speech Recognition**: Captures and converts spoken words into text using the `SpeechRecognition` library.
- **Text-to-Speech**: Converts text responses into spoken words using `gTTS`.
- **Text Cleaning**: Removes unwanted special characters from the captured text.
- **Google Gemini API Integration**: Sends cleaned text to the Google Gemini API for generating responses (API key removed for security purposes).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/akshay-k-a-dev/kunnapan-AI-Assistant.git
   cd kunnapan-AI-Assistant
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant:

   ```bash
   python assistant.py
   ```

## Usage

- The assistant will adjust for ambient noise and start listening for voice input.
- Speak clearly, and the assistant will recognize your words and respond.
- Press `q` and hit `Enter` at any time to quit the program.

## API Integration

This project utilizes the **Google Gemini API** for generating content based on the user's speech input. Please note that the API key has been removed from the code for security reasons. If you wish to use the Google Gemini API, you will need to add your own API key in the `send_to_api` function within `assistant.py`.

```python
api_key = "YOUR_API_KEY_HERE"
```

## Acknowledgments

- **Google Gemini API**: Special thanks to Google for providing the Gemini API, which enables the assistant to generate intelligent responses.
- **SpeechRecognition Library**: For providing the tools to capture and process speech input.
- **gTTS (Google Text-to-Speech)**: For enabling the assistant to convert text responses into spoken words.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcomed for bug fixes, enhancements, or new features. Make sure your contributions align with the GNU General Public License v3.0.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
