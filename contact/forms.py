from django.forms import ModelForm

from contact.models import ContactUs


class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
