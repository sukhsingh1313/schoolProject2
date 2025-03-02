import csv
import json
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import StudentResult
from .forms import SearchResultForm


def upload_csv(request):
    if request.method == "POST" and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        # Check if it's a valid CSV file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, "File is not a CSV type")
            return render(request, 'Results/upload_csv.html')

        # Process CSV
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            subject_details = json.loads(row['subject_details'])  # Parse JSON string from CSV
            StudentResult.objects.update_or_create(
                roll_no=row['roll_no'],
                defaults={
                    'name': row['name'],
                    'father_name': row['father_name'],
                    'mother_name': row['mother_name'],
                    'year_sem': row['year_sem'],
                    'exam_month': row['exam_month'],
                    'exam_year': row['exam_year'],
                    'exam_type': row['exam_type'],
                    'subject_details': subject_details,
                    'percentage': row['percentage'],
                    'result_status': row['result_status']
                }
            )

        messages.success(request, "CSV file uploaded successfully!")
    return render(request, 'Results/upload_csv.html')

def search_result(request):
    if request.method == "POST":
        form = SearchResultForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            exam_year = form.cleaned_data['exam_year']
            exam_month = form.cleaned_data['exam_month']
            exam_type = form.cleaned_data['exam_type']
            year_sem = form.cleaned_data['year_sem']

            # Fetch result
            result = get_object_or_404(
                StudentResult,
                roll_no=roll_no,
                exam_year=exam_year,
                exam_month=exam_month,
                exam_type=exam_type,
                year_sem=year_sem
            )
            return render(request, 'Results/result.html', {'result': result})

    else:
        form = SearchResultForm()

    return render(request, 'Results/search.html', {'form': form})