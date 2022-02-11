from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length = 100,
        widget = forms.TextInput(
            attrs = {'class' : 'form-control', 'placeholder' : 'Enter what you will be doing today', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}
        )
    )
    