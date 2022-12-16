from django import forms
from .models import Items


# creating a form
class ItemsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Items

        # specify fields to be used
        fields = [
            "item_name",
            "item_price",
            "item_stock",
            "item_image",
        ]
