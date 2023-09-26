from django import forms
from .models import Pet

class CreateCarForm(forms.Form):
    def validate_year(value):       
        if len(str(value)) != 4:
            raise "O ano não possui 4 dígitos!"        
        
        if int(value) < 1990 and int(value) > 2077:
            raise "O ano é inválido"
        

    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control mb-2"

    manufacturer = forms.CharField(
        label="Fabricante",
        max_length=100,
    )
    model = forms.CharField(label="Modelo", max_length=80)
    color = forms.CharField(label="Cor", max_length=50)
    year = forms.IntegerField(label="Ano", validators=[validate_year])


class CreatePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.fields.values()
        for field in fields:
            field.widget.attrs.update({'class': 'form-control mb-2'})
        fields.mapping['name'].label = 'Nome'
        fields.mapping['age'].label = 'Idade'
