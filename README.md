# Social Media Driver

## Description

Social Media Driver is a Python-based automation tool designed to manage and schedule social media updates for your Etsy shop. By integrating with the social media management platform Buffer and utilizing a headless browser, this program aims to streamline your social media workflow, ensuring consistent and timely updates across various platforms.

## Features

- **Headless Browser Automation**: Automates the process of posting updates on social media through Buffer.
- **Schedule Management**: Enables scheduling of posts in advance, ensuring consistent updates.
- **Multi-Platform Support**: Manages multiple social media platforms through a single interface.
- **Etsy Shop Integration**: Fetches latest products and updates from your Etsy shop for sharing on social media.

## Getting Started

### Prerequisites

- Python 3.x
- A headless browser (e.g., Selenium WebDriver with Chrome or Firefox headless mode)
- Buffer account (Free tier or higher)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/blamb888/social_media_driver.git
    ```
2. Navigate to the project directory:
    ```bash
    cd social_media_driver
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Update the `config.py` file with your Buffer account credentials and other necessary configurations.
2. Set up your headless browser and specify the browser driver path in the `config.py` file.

### Usage

1. Run the script:
    ```bash
    python main.py
    ```

## Contributing

If you would like to contribute to the development of Social Media Driver, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
