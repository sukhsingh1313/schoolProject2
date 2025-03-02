from django import forms

class SearchResultForm(forms.Form):
    roll_no = forms.CharField(label="Roll Number", max_length=20)
    exam_year = forms.IntegerField(label="Exam Year")
    exam_month = forms.CharField(label="Exam Month")
    exam_type = forms.CharField(label="Exam Type")
    year_sem = forms.CharField(label="Year/Semester")
