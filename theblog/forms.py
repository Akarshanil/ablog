from django import forms
from .models import post,category,Command

# choices =[('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices = category.objects.all().values_list('name','name')
choice_list=[]
for i in choices:
    choice_list.append(i)
class postform(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'title_tag', 'author', 'category', 'body' ,'snippet', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':choices}),  #placeholder all we can put
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':choice_list}),
            'snippet': forms.Textarea( attrs={'class': 'form-control'}),

        }
class Editform(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'title_tag', 'body','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  #placeholder all we can put
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }
class Editcommentform(forms.ModelForm):
    class Meta:
        model = Command
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  #placeholder all we can put
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
