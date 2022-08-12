from .models import Feedback
from django.forms import ModelForm


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message', 'email', 'first_name', 'file']
        # permissions = (("can_mark", ),)