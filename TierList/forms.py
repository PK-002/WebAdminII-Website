from django import forms

class TierListForm(forms.Form):
    title = forms.CharField(max_length=100)
    ranking_data = forms.JSONField()