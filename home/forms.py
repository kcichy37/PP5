from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Reviews
        fields = ('rating', 'comment')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = 'Leave a review'
        self.fields['rating'].widget.attrs['placeholder'] = 'Rate us out of 5'
        self.user = user

    def save(self, commit=True):
        review = super().save(commit=False)
        review.user = self.user
        if commit:
            review.save()
        return review
