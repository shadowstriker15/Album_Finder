import os
import glob
from django.http import HttpResponse
from django.contrib import messages
from .models import Song, Document
from .forms import RawSongForm, DocumentForm
from pathlib import Path
from .get_cover import find_cover
from .edit_song import editor
from .find_album import get_album
from .find_artist import get_artist

from django.shortcuts import render

filename_list = []


def home_view(request):
    if not request.user.is_authenticated:
        messages.info(request, f'Please register or login to upload file')

    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            if not request.user.is_authenticated:
                messages.error(request, f'Upload unsuccessful, you must be logged in')
            else:
                newdoc = Document(docfile=request.FILES['docfile'])
                name = form.cleaned_data['docfile'].name
                global filename_list
                filename_list.append(name)
                newdoc.owner = request.user
                newdoc.save()

                messages.info(request, f'Upload successful')
    else:
        form = DocumentForm()

    context = {'form': form}
    return render(request, 'RipperApp/index.html', context)


def song_edit_view(request):
    context = {
        'path_num': 1,
    }

    path_list = get_path_list(request)

    # Check to see if any downloaded mp3s
    global filename_list
    if len(filename_list) != 0:
        file_name = filename_list[0]
        context.update({"file_name": file_name})
        file_name = os.path.splitext(file_name)[0]

        # Remove text contained in parentheses
        if '(' and ')' in file_name:
            end_index = file_name.find('(')
            file_name = file_name[:end_index]
        # Find artist and title from file name
        if '-' in file_name:
            file_name = file_name.split(' - ', 1)
            song_form = RawSongForm(initial={'artist': file_name[0], 'title': file_name[1]})
        else:
            artist = get_artist(file_name)
            song_form = RawSongForm(initial={'artist': artist, 'title': file_name})
        context.update({'song_form': song_form})
    else:
        context.update({'path_num': 0})
        messages.info(request, f'No more uploaded songs')

    if request.method == "POST":
        song_form_post = RawSongForm(request.POST)

        if song_form_post.is_valid():
            artist = song_form_post.cleaned_data['artist']
            title = song_form_post.cleaned_data['title']
            genre = song_form_post.cleaned_data['genre']

            album, cover_link = get_album(artist, title)

            if album == "Invalid":
                album = None
                messages.error(request, f'Could not set album name and cover')
                album_path = None
            else:
                album_path = find_cover(cover_link, request.user)

            editor(artist, title, album, genre, path_list, album_path)
            Song.objects.create(**song_form_post.cleaned_data)

            response = HttpResponse(open(path_list[0], 'rb').read())
            response['Content-Type'] = 'audio/mpeg'
            file_name = title + '.mp3'
            response['Content-Disposition'] = "attachment; filename=\"" + file_name + "\""
            return response

    return render(request, 'RipperApp/song_edit.html', context)


# Used to find mp3s in user's upload folder
def get_path_list(request):
    home = str(Path.home())
    user_folder = 'user_' + str(request.user.id)
    path = os.path.join(home, 'media', 'Users', user_folder, '*mp3')
    return glob.glob(path)


def next_page(request):
    global filename_list
    path_list = get_path_list(request)
    filename_list = filename_list[1:]
    os.remove(path_list[0])
    return song_edit_view(request)


# Used to prevent next_page getting called
def download_view(request):
    return song_edit_view(request)


def about_view(request):
    return render(request, 'RipperApp/about.html')
