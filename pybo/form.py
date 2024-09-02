from django import forms
from pybo.models import Question,Answer,Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {

            'subject' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows':8}),
        }
        labels = {
            
            'subject' :'제목',
            'content' :'내용',
        }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','parent']

        labels ={
            'content': '내용',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'parent': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
         self.parent_comment = kwargs.pop('parent_comment', None)
         super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.parent_comment:
            comment.parent = self.parent_comment
        if commit:
            comment.save()
        return comment