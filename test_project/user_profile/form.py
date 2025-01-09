from django.forms import ModelForm
from .models import Profile

class tableform(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'email', 'username', 'short_intro', 'bio', 'profile_img', 'social_git', 'social_x', 'social_lin', 'social_yt']