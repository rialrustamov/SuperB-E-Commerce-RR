from django import forms

from product.models import Review

class ReviewRequestForm(forms.Form):
    CHOICES=[('1',' '),
             ('2',' '),
             ('3',' '),
             ('4',' '),
             ('5',' '),
    ]
    price_rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={
        'type' :"radio", 
        'id' : "Price", 
        'name' : "ratings",
        'class' : "radio",
        'value' : ""
    }))
    value_rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={
        'type' :"radio", 
        'id' : "Value", 
        'name' : "ratings",
        'class' : "radio",
        'value' : ""
    }))
    quality_rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={
        'type' :"radio", 
        'id' : "Quality", 
        'name' : "ratings",
        'class' : "radio",
        'value' : ""
    }))
    nickname = forms.CharField(max_length=50, help_text='Max 50 character', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "nickname_field", 
        'name' : "nickname",
        'class' : "input-text"}))
    summary = forms.CharField(max_length=50, help_text='Max 50 character', widget=forms.TextInput(attrs={
        'type' :"text", 
        'id' : "summary_field", 
        'name' : "title",
        'class' : "input-text"}))
    review = forms.CharField(max_length=1000, required=True ,widget=forms.Textarea(attrs={
        'type' :"text", 
        'name' : "detail",
        'id' : "review_field", 
        'class' : "input-text ",
        'cols' : "50",
        'rows' : "30"}))

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = (
            # 'price_review',
            # 'value_review',
            # 'quality_review',
            'nickname',
            'summary',
            'review'
        )
        widgets = {
            # 'price_review' : forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect),
            # 'value_review' : forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect),
            # 'quality_review' : forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect),
            'nickname' : forms.TextInput(attrs={
                                        'type' :"text", 
                                        'id' : "nickname_field", 
                                        'name' : "nickname",
                                        'class' : "input-text"}),
            'summary' : forms.TextInput(attrs={
                                        'type' :"text", 
                                        'id' : "summary_field", 
                                        'name' : "title",
                                        'class' : "input-text"}),
            'review' : forms.Textarea(attrs={
                                        'type' :"text", 
                                        'name' : "detail",
                                        'id' : "review_field", 
                                        'class' : "input-text ",
                                        'cols' : "50",
                                        'rows' : "30"})
        }