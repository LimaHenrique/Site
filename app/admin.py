from django.contrib import admin
from app.models import Curso, Aluno
from django.contrib.auth.admin import UserAdmin
from django import forms

class NovoAlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = ('ra', 'nome','curso')

        def save(self, commit=True):
            user = super(NovoAlunoForm, self).save(commit=False)
            user.set_password('123')
            user.perfil = 'A'
            if commit:
                user.save()
            return user
class AlterarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'curso')

class AlunoAdmin(UserAdmin):
    form = AlterarAlunoForm
    add_form = NovoAlunoForm
    list_display = ('ra', 'nome', 'curso')
    list_filter = ('perfil',)
    fieldsets = ( (None, {'fields': ('ra', 'nome', 'curso','Password1')}),)
    add_fieldsets = ((None, { 'fields': ('ra', 'nome', 'curso')} ),)
    search_fields = ('ra',)
    ordering = ('ra',)
    filter_horizontal = ()

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno,AlunoAdmin)
