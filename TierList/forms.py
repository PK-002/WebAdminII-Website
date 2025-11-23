from django import forms

from TierList.models import Image

class TierListForm(forms.Form):
    title = forms.CharField(max_length=100)
    ranking_data = forms.JSONField()

class ImageUploadForm(forms.Form):
    class Meta:
        model = Image
        fields = ['ranking', 'image']