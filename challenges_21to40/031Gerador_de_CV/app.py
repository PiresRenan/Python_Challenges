from flask import Flask, render_template, request, redirect, url_for
from forms import PersonalInfoForm, ExperienceForm, EducationForm
from utils.pdf_generator import PdfGenerator

app = Flask(__name__)
app.secret_key = "aplicativoDemoCVCreator2024"

pdf_file = PdfGenerator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    form = PersonalInfoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pdf_file.generate_pdf(form.data)
            return redirect(url_for('experience'))
    return render_template('personal_info.html', form=form)


@app.route('/experience', methods=['GET', 'POST'])
def experience():
    form = ExperienceForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pdf_file.generate_pdf(form.data)
            return redirect(url_for('education'))
    return render_template('experience.html', form=form)


@app.route('/education', methods=['GET', 'POST'])
def education():
    form = EducationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            pdf_file.generate_pdf(form.data)
            return pdf_file.finish_pdf()
    return render_template('education.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
