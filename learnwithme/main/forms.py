from django import forms
from .models import Comment, ReplyComment

class CommentForm(forms.Form):
    class Meta:
        model = Comment

    name = forms.CharField(max_length=400, widget=forms.TextInput(
        attrs={'class' : 'white-text', 'id' : 'icon_prefix', 'data-length' : '50'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class' : 'white-text', 'id' : 'icon_email'}
    ))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class' : 'materialize-textarea white-text', 'id' : 'icon_message'}
    ))

class ReplyCommentForm(forms.Form):
    class Meta:
        model = ReplyComment
    
    name_reply = forms.CharField(max_length=400, widget=forms.TextInput(
        attrs={'id' : 'icon_prefix_reply'}
    ))

    text_reply = forms.CharField(widget=forms.Textarea(
        attrs={'class' : 'materialize-textarea', 'id' : 'icon_message_reply'}
    ))
