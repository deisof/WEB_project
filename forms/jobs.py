import requests
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError


class JobsForm(FlaskForm):
    def check_address(self, field):
        try:
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": field.data,
                "format": "json"}
            response = requests.get(geocoder_api_server, params=geocoder_params)
            if response:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"][
                    "featureMember"][0]["GeoObject"]["Point"]["pos"]
            else:
                raise ValidationError('invalid address')
        except:
            raise ValidationError('invalid address')

    description = StringField("Краткое описание работы", validators=[DataRequired()])
    employer = IntegerField("id обращающегося")
    address = TextAreaField("Адрес", validators=[DataRequired(), check_address])
    info = TextAreaField("Доп. информация")
    coords = TextAreaField("Координаты")
    date = TextAreaField("Когда нужно прийти (дата и время)", validators=[DataRequired()])
    is_finished = BooleanField("Выполнено ли обращение?")
    submit = SubmitField('Готово')


class AddressJob(FlaskForm):
    sorting = SelectField('Сортировать по', choices=[('date_sort_up', 'дате добавления (от старого к новому)'),
                                                     ('date_sort_down', 'дате добавления (от нового к старому)')])

    my_address = StringField('Ваш адрес')
    submit_address = SubmitField('Найти ближайшие обращение')
    submit_sort = SubmitField('Сортировать')


class Ready(FlaskForm):
    submit_ready = SubmitField('Готов приступить к обращению')
    submit_refuse = SubmitField('Отказаться')
