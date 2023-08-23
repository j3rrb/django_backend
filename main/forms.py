from django import forms


class CreateCarForm(forms.Form):
    def validate_year(value):
        if not value.isnumeric():
            raise "Valor não-numérico!"
        
        if len(value) != 4:
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
