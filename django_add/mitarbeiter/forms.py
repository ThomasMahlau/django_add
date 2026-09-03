from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Mitarbeiter

class MitarbeiterRegisterForm(UserCreationForm):
    name = forms.CharField()
    vorname = forms.CharField()
    strasse = forms.CharField()
    plz = forms.CharField()
    ort = name = forms.CharField()
    geburtsdatum = forms.DateField()
    #widget=forms.DateInput(attrs={"type": "date"})
    #widget=forms.DateInput(attrs={"type": "date"})
    einstellungsdatum = forms.DateField()
    telefonnummer = forms.CharField()
    
    class Meta: 
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "name",
            "vorname",
            "strasse",
            "plz",
            "ort",
            "geburtsdatum",
            "einstellungsdatum",
            "telefonnummer",
        ]
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
    
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.save()
        
        mitarbeiter = Mitarbeiter(
            benutzer=user,
            name=self.cleaned_data["name"],
            vorname=self.cleaned_data["vorname"],
            strass=self.cleaned_data["strasse"],
            plz=self.cleaned_data["plz"],
            ort=self.cleaned_data["ort"],
            geburtsdatum=self.cleaned_data["geburtsdatum"],
            einstellungsdatum=self.cleaned_data["einstellungsdatum"],
            telefonnummer=self.cleaned_data["telefonnummer"],
        )
        if commit:
            mitarbeiter.save()
            
        return user
    
class MitarbeiterForm(forms.ModelForm):
    class Meta:
        model = Mitarbeiter
        fields = "__all__"
        
        """
        widgets = {
            "geburtsdatum": forms.DateInput(attrs={"type": "date"}),
            "einstellungsdatum": forms.DateInput(attrs={"type": "date"}),
            "telefonnummer": forms.CharField(attrs={"type": "date"}),
        }
        """

class EigeneUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].label = 'Benutzername'
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].label = 'Passwort wiederholen'
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].label = 'Email'