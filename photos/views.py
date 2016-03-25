import logging

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import PermissionDenied

#from django.http import HttpResponse

from rest_framework import serializers
from rest_framework import viewsets 

#from pystagram.middlewares import HelloWorldError
from .models import Photo
from .models import Like
from .models import Comment
from .forms import PhotoEditForm

logger = logging.getLogger('django')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'content', 'created_at',)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


def toppage(request):
    messages.info(request, '글 목록에 접속')
    logger.warning('toppage입')
    #raise HelloWorldError('으악 뭔가 이상해')
    #return HttpResponse('hello world')

    edit_form = PhotoEditForm()
    photos = Photo.objects.order_by('-updated_at')
    ctx = {
        'object_list': photos,
        'form':edit_form,
    }

    return render(request, 'toppage.html', ctx)


def view_photo(request, pk):
    messages.info(request, '글 목록에 접22222속')
    photo = get_object_or_404(Photo, pk=pk)
    ctx = {
            'photo': photo,
    }
    return render(request, 'view_photo.html', ctx)

def create_photo(request):
    print('create_photo진입')

    if request.method == 'POST':
        edit_form = PhotoEditForm(request.POST, request.FILES)
        print('edit_form진입')

        if edit_form.is_valid():
            
            new_photo = edit_form.save(commit=False)
            new_photo.user = request.user
            new_photo.save()

            print('edit_form.save() ddfdf')
            return redirect('photos:toppage')

def delete_photo(request, pk):
    the_photo = get_object_or_404(Photo,pk=pk)
    if request.user.id != the_photo.user.id:
        raise PermissionDenied
    if request.method == 'POST':
        the_photo.delete()    
        return redirect('photos:toppage')

    return redirect('photos:toppage')

    

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    like, is_created = Like.objects.get_or_create(
        user=request.user,
        photo=photo,
        defaults={
            'user': request.user,
            'photo': photo,
            'status': True,
        }
    )

    if is_created is False:
        like.status = not like.status
        like.save()
        if like.status is True:
            messages.info(request, '좋아요를 누름')
        else:
            messages.info(request, '좋아요 취소')
    else:
        messages.info(request, '좋아요 누름름 함')

    return redirect('photos:view_photo',pk=photo.pk)


def add_comment(request):
    print('add_comment')
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.content = request.POST.get('content')

        photo_id = request.POST.get('photo_id')
        the_photo = get_object_or_404(Photo,pk=photo_id)
        new_comment.photo = the_photo
        new_comment.user = request.user
        new_comment.save()

    return redirect('photos:view_photo',pk=photo_id)

def delete_comment(request):
    print('delete_comment')
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.id = request.POST.get('comment_id')

        print(new_comment.id)

        photo_id = request.POST.get('photo_id')
        the_photo = get_object_or_404(Photo,pk=photo_id)

        new_comment.delete()

    return redirect('photos:view_photo',pk=photo_id)




