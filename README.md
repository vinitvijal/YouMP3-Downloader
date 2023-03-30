

# YouMP3-Downloader


YouMP3-Downloader is a Django web application that allows users to download YouTube videos as MP3 files with ease. Simply paste the video URL and the app takes care of the rest, providing a seamless user experience for downloading high-quality audio tracks from YouTube videos.

## Installation
* Clone this repository: git clone https://github.com/vinitvijal/YouMP3-Downloader.git
* Navigate to the project directory: cd YouMP3-Downloader
* Install the dependencies: pip install -r requirements.txt
* Run the server: python manage.py runserver
* Open a web browser and go to http://localhost:8000 to access the app.
## Usage
* Enter the URL of the YouTube video you want to download in the input field.
* Click the "Download" button to download the video as an MP3 file.
* The app will display the progress of the download and provide a link to download the finished MP3 file.
## Contributing
If you would like to contribute to the development of YouMP3-Downloader, please feel free to fork the repository and submit a pull request. All contributions are welcome!

License
YouMP3-Downloader is licensed under the MIT License. See LICENSE for more information.
## Deployment

* Create Virtual environment :

```bash
  python3 -m venv venv 
```
* Activate Virtual environment :

```bash
  source venv/bin/activate 
```

* Install the dependencies for project :

```bash
  pip install -r requirement.txt
```

* Start Production Server :
```bash
  gunicorn YouMusicVinu.wsgi:application
```

## Authors

- [@vinitvijal](https://www.github.com/vinitvijal)

