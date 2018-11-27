from django import forms
from .models import Usuario, Rescatado

class RegistroUForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('correo','password','run','nombre','snombre','paterno','materno','fnac','telefono','region','ciudad','vivienda')

class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('run','password')


class RescatadoForm(forms.ModelForm):
	
	class Meta:
		model = Rescatado

		fields = [
			'foto',
			'nombre',
			'raza',
			'descr',
			'estado',
		]
		labels = {
			'foto' : 'Fotografia',
			'nombre' : 'Nombre',
			'raza' : 'Raza Predominante',
			'descr' : 'Descripcion',
			'estado' : 'Estado',
		}
		widgets = {
			'foto' : forms.FileInput(attrs={'class':'form-control'}),
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'raza' : forms.TextInput(attrs={'class':'form-control'}),
			'descr' : forms.Textarea(attrs={'class':'form-control'}),
			#'estado' : forms.ChoiceField(choices=(('Rescatado', 'Rescatado'),('Disponible', 'Disponible'),('Adoptado', 'Adoptado')))
		}

		

#class RegistrarMascotaForm(forms.Form):
#    foto=forms.ImageField(label="  Fotografía")
#    nombre=forms.CharField(widget=forms.TextInput(),label="  Nombre")
#    raza=forms.CharField(widget=forms.TextInput(), label=" Raza Predominante")
#    descr=forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':30}),label="  Descripcion",)
#    estado=forms.ChoiceField(choices=(('1', 'Rescatado'),('2', 'Disponible'),('3', 'Adoptado')),label="  Estado")

       