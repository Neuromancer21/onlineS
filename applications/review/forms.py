from django import forms

from ..review.models import Review


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'description', 'rating')


class UpdateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'description', 'rating')