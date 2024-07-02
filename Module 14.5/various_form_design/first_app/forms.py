from django import forms
from django.forms.widgets import NumberInput

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

Programming_Language_CHOICES =[
    ('c','C'),
    ('python','Python'),
    ('java','Java'),
    ('c++','C++'),
    ('javascript','JavaScript'),
]

Career_Options_CHOICES = [
    ('govt. job','Govt. Job'),
    ('bcs','Bcs'),
    ('banking sector','Banking sector'),
    ('nongovt. sector','NonGovt. sector'),
]


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=60, label="Your Name", widget = forms.TextInput(attrs={"placeholder": "Type your name here"}),help_text="Type your name between 60 characters",required=True)
    
    email = forms.EmailField(label="Your email address",required=True)
    
    birth_date = forms.DateField(label="Birth Date",widget=NumberInput(attrs={'type': 'date'}))
    
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    
    career_track = forms.ChoiceField(label="Choose Career Path", widget=forms.RadioSelect,choices=Career_Options_CHOICES, )

    language_you_know = forms.MultipleChoiceField(label="Choose Programming Languages", widget=forms.CheckboxSelectMultiple,choices=Programming_Language_CHOICES,)
    
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={"placeholder": "Type Your Message Here . . .", "rows": 3}
        ),
    )