from rest_framework import serializers
from web_misperris.models import Usuario, Rescatado

class RescatadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rescatado
		fields = ('foto', 'nombre', 'raza', 'descr', 'estado')
		
