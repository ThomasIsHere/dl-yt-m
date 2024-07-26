from django.shortcuts import render
from django.http import FileResponse, Http404

import os

from .forms import SimpleForm
from .utils import dl, deletemp3


def simple_form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            videoId = form.cleaned_data['videoId']
            video_url = 'https://www.youtube.com/watch?v=' + videoId  
            output_path = './temp_medias/'
            audio_only = True

            videoName = dl.download_youtube_video(video_url, output_path, audio_only)

            file_directory = os.path.join(output_path)
            file_path = os.path.join(file_directory, videoName + '.mp3')

            if not os.path.exists(file_path):
                raise Http404("The requested file does not exist")
            
            response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'

            deletemp3.deleteMp3File.after_response(file_path)

            return response
    else:
        form = SimpleForm()

    return render(request, 'home/form.html', {'form': form})