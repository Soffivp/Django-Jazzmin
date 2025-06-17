from django.contrib import admin

# Register your models here.
from app01.models import *



class InscripcionInline(admin.TabularInline):
	model = Inscripcion
	extra = 1
	verbose_name =  "Inscripcion"
	verbose_name_plural =  "Inscripciones"


class CursoAdmin(admin.ModelAdmin):
	list_display = ('titulo','departamento','instructor')
	list_filter = ('departamento','instructor')
	search_fields = ['titulo']
	inlines = (InscripcionInline,)



admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea)
admin.site.register(Entrega)
