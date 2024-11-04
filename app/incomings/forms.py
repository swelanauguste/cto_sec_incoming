from django import forms

from . import models


class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = models.ChangeStatus
        fields = ["status", "date", "note", "file"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class IncomingForm(forms.ModelForm):
    class Meta:
        model = models.Incoming
        fields = "__all__"
        exclude = ["slug", "ref"]
        widgets = {
            "received_on": forms.DateInput(attrs={"type": "date"}),
            "letter_dated": forms.DateInput(attrs={"type": "date"}),
        }
