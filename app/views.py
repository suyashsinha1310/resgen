from django.shortcuts import render
from django.http import HttpResponse
from fpdf import FPDF

def home(request):
    return render(request, 'index.html')

def generate_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        education = request.POST.get('education')
        experience = request.POST.get('experience')
        projects = request.POST.get('projects')
        skills = request.POST.get('skills')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)

        pdf.cell(200, 10, txt="Resume", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font('Arial', '', 12)
        pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
        pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
        pdf.ln(10)

        pdf.set_font('Arial', 'B', 14)
        pdf.cell(200, 10, txt="Education", ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, txt=education)
        pdf.ln(5)

        pdf.set_font('Arial', 'B', 14)
        pdf.cell(200, 10, txt="Experience", ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, txt=experience)
        pdf.ln(5)

        pdf.set_font('Arial', 'B', 14)
        pdf.cell(200, 10, txt="Projects", ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, txt=projects)
        pdf.ln(5)

        pdf.set_font('Arial', 'B', 14)
        pdf.cell(200, 10, txt="Skills", ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, txt=skills)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        
        response.write(pdf.output(dest='S').encode('latin1'))
        return response

    return render(request, 'index.html')
