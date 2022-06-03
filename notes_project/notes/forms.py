from django.forms import ModelForm
from .models import Notes


class NoteCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'form-control mb-3'}
            )

    class Meta:
        model = Notes
        fields = ['title', 'description']
