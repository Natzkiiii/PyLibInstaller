# Python Library Installer (PyLibInst)
This repository contains a script to automatically install a list of required Python libraries using `pip`.

## Requirements

- Python 3.x
- `requirements.txt` file with the list of libraries to install

## Included Libraries

The `requirements.txt` file includes the following libraries, some with specific versions:

pyautogui

keyboard

requests==2.28.1

numpy>=1.21.0

pandas==1.3.5

scipy

matplotlib>=3.4.0

scikit-learn==0.24.2

flask

django>=3.2

beautifulsoup4==4.9.3

pillow>=8.0.0

tensorflow==2.6.0

torch==1.9.0

seaborn>=0.11.0

sqlalchemy>=1.4

pytest==6.2.4

jupyter

lxml==4.6.3

opencv-python>=4.5.1.48

## Usage

1. Clone the repository to your local machine: (i will add the .git file later lol)
    ```sh
    git clone https://github.com/Natzkiiii/
    ```

2. Navigate to the repository directory:
    ```sh
    cd PyLibInstaller/
    ```

3. Ensure you have Python 3.x installed. You can check your Python version with:
    ```sh
    python --version
    ```

4. Run the script to install the required libraries:
    ```sh
    python main.py
    ```

The script reads the `requirements.txt` file and installs all listed libraries.

## Contributing

If you want to add more libraries or update the existing ones, simply edit the `requirements.txt` file and add the necessary entries. Follow the format:

```
library_name==version

or

library_name>=minimum_version
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
