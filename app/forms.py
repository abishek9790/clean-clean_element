from django import forms


def for_a_pass(value):
    if value[0]!='ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        raise forms.ValidationError('first letter uppercase')


class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(),validators=[])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcapture=forms.CharField(max_length=100,widget=forms.HiddenInput(),required=False)


    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_enter_email']
        if e!=re:
            raise forms.ValidationError("sorry valid")
    
    def clean_botcapture(self):
        s=self.cleaned_data['botcapture']
        if len(s)>0:
            raise forms.ValidationError("invalid")


