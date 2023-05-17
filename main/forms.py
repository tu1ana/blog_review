from django import forms

from main.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'article')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'article':
                field.widget = forms.HiddenInput()
            field.widget.attrs['class'] = 'form-control'
