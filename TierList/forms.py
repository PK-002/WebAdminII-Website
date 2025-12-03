from django import forms

from TierList.models import Image, Ranking

from django.contrib.auth.forms import UserCreationForm

class TierListForm(forms.Form):
    title = forms.CharField(max_length=100)

    class Meta:
        model = Ranking
        fields = ('title',)

class ImageUploadForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Image
        fields = ('image', )