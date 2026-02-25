from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class CompraForm(FlaskForm):
    nombre = StringField('Nombre del Titular', validators=[DataRequired()])
    correo = StringField('Correo para recibir boletos', validators=[DataRequired()])
    cantidad = IntegerField('Cantidad de Boletos ($12 c/u)', default=1, validators=[
        DataRequired(), 
        NumberRange(min=1, max=7, message="Por políticas, el límite es de 7 boletos.")
    ])
    tarjeta_cineco = BooleanField('¿Tienes tarjeta CINECO? (Aplica 10% extra)')
    submit = SubmitField('Comprar Boletos')