from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PersonalInfoForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Salvar e continuar')


class ExperienceForm(FlaskForm):
    job_title = StringField('Cargo', validators=[DataRequired()])
    company = StringField('Empresa', validators=[DataRequired()])
    # Outros campos para experiência profissional
    submit = SubmitField('Salvar e Continuar')


class EducationForm(FlaskForm):
    degree = StringField('Grau Acadêmico', validators=[DataRequired()])
    institution = StringField('Instituição', validators=[DataRequired()])
    # Outros campos para educação
    submit = SubmitField('Salvar e Continuar')