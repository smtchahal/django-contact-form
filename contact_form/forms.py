from django.forms import ModelForm, Textarea, Select

from contact_form.models import ContactFormSubmission

_subject_choices = (
    'Account',
    'Payment',
    'General feedback',
    'Other',
)


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = '__all__'
        widgets = {
            'subject': Select(choices=((c, c) for c in _subject_choices)),
            'message': Textarea(),
        }
