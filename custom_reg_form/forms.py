from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['express_consent'].error_messages = {
            "required": u"This field is required.",
            "invalid": u"This field is required.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('express_consent', 'marketing_opt_in')
