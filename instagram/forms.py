from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'message',
            'is_public'
        ]

# form = PostForm(reqeust.POST)
# if forms.is_valid():
#     post.form.save(commit=False)
#     post.author = reqeust.user
#     post.ip = reqeust.META['REMOTE_ADDR']
#     post.save()
#
# serializer.is_valid()
# serializer.save(author=request.user, ip=request.META['REMOTE_ADDR'])
