from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ("S", "Stripe"),
    ("P", "PayPal"),
)


class CheckoutForm(forms.Form):

    r"""Checkout form
    # RadioSelect : only select One.
    # CheckboxInput : each can checking.
    """

    address_street = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "123 Street NY"})
    )
    address_apartment = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Apartment or suite address"})
    )
    countries = CountryField(blank_label="(select country)").formfield(
        required=False,
        widget=CountrySelectWidget(attrs={"class": "custom-select d-block w-100",}),
    )
    zip_code = forms.CharField(max_length=20, required=False)
    same_billing_address = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False,
    )
    save_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES
    )


class CouponForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Promo code",
                "aria-label": "Recipient's username",
                "aria-describedby": "basic-addon2",
            }
        )
    )


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))
    email = forms.EmailField()

