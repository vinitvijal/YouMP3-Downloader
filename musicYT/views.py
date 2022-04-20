import mimetypes

from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
import os, shutil
# Create your views here.




def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        print(link)
        try :
            yt = YouTube(link)
            title = yt.title
            filename = nameConverter(title) + '.mp3'
            print(title)

            print(filename)

            stream = yt.streams.get_audio_only()
            clean()
            stream.download('media', filename)
            print('Successful')
            context = {
                'downloadLink' : '/media/' + filename,
                'filename' : title,
                'title' : title,
            }
            return render(request, 'index.html', context)
        except:
            context = {
                'Error': '!!! Please check and Retry. Thank You !!!',
            }
            return render(request, 'index.html', context)
    context ={
        'title': 'YouTube MP3 Converter - Code Vinu',
    }
    return render(request, 'index.html', context)



def download(request, filename):
    parent_dir = os.path.dirname(os.path.abspath('manage.py'))
    directory = '/media/' + filename
    path = os.path.join(parent_dir, directory)

    response = HttpResponse()
    response['X-File'] = path
    return response


def clean():
    directory = 'media'
    parent_dir = os.path.dirname(os.path.abspath('manage.py'))
    print(parent_dir)
    # Removing Folders
    path = os.path.join(parent_dir, directory)
    shutil.rmtree(path)
    # Create Folders
    os.mkdir(path)
    file = open(path + '/extra.txt', 'w')
    file.write('Hii File')
    file.close()

    print("Media Data is Cleared!!!!")


def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/media/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'index.html')

def nameConverter(title):
    a = title
    z = []

    for i in a:
        if i.isalnum():
            z.append(i)
        elif i == " ":
            z.append('_')
        elif i == "|":
            z.append('-')
        else:
            z.append('_')

    newTitle = ''.join(z) + '(codeVinu)'
    return newTitle
