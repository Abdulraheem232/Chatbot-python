
# My Chatbot 2.0

This is a chatbot built with **Flet**, an easy-to-use framework for creating modern, cross-platform apps with Python. The chatbot uses Google's generative AI model (Gemini 1.5) to generate responses based on user input.

## Features

- **Cross-platform support**: Works seamlessly on Web, Linux, macOS, Windows, iOS, and Android.
- **Generative AI**: Powered by Google's **Gemini-1.5-flash-002** model to create AI-driven chatbot interactions.
- **Modern UI**: Clean, responsive user interface built with Flet for an enhanced user experience.
- **Dark Mode Support**: Toggle between light and dark themes for improved usability.
- **Efficient Loading**: Displays a progress ring while waiting for AI responses.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Abdulraheem232/Chatbot-python
   cd Chatbot-python
   ```

2. Install the required dependencies:

   ```bash
   pip install flet google-generativeai python-dotenv
   ```

3. Create a `.env` file in the root directory and add your Google API key like this:

   ```bash
   APIKEY=your_google_api_key_here
   ```

4. Run the app:

   ```bash
   python main.py
   ```

## How It Works

- The app allows users to input a prompt and generates a response using Google's **Generative AI** model.
- The input text and the response from the AI are displayed in a chat-like format.
- The UI features an input box, a submit button, and a dynamic chat area that updates with each new interaction.
- Users can toggle between light and dark modes for a personalized experience.

## Compatibility

This app is fully compatible with:

- **Linux**
- **macOS**
- **Windows**
- **iOS**
- **Android**
- **Web**

With Flet’s cross-platform capabilities, you can run this app on virtually any platform, ensuring a consistent user experience.

## UI Features

- **Flet** provides a powerful UI library that offers out-of-the-box features for creating modern user interfaces.
- The app features a well-designed `AppBar` and chatbot interaction flow with support for interactive controls like buttons, text fields, and progress indicators.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Flet**: The framework that powers the UI.
- **Google Generative AI**: For providing the powerful Gemini 1.5 model used to generate responses.

## Contact

If you have any questions or feedback, feel free to open an issue or reach out to me via email abdulraheemabdullah859@gmail.com or kamran1513@gmail.com.
