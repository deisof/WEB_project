import requests
from data import db_session
from data.jobs import Jobs


def sort_address_jobs(address):
    try:
        db_session.global_init("db/jobs.db")
        session = db_session.create_session()
        jobs = session.query(Jobs).all()

        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": address,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            coodrinates = toponym["Point"]["pos"]

            sp = [(job, ((float(job.coords.split()[0]) - float(coodrinates.split()[0])) ** 2 + (
                    float(job.coords.split()[1]) - float(coodrinates.split()[1])) ** 2) ** 0.5) for job in jobs]
            return [el[0] for el in sorted(sp, key=lambda x: x[1])]
    except Exception:
        return None


def sort_date_jobs(position):
    try:
        db_session.global_init("db/jobs.db")
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        sp = [(job, job.id) for job in jobs]
        if position == 'up':
            return [el[0] for el in sorted(sp, key=lambda x: x[1])]
        return [el[0] for el in sorted(sp, key=lambda x: x[1])][::-1]
    except Exception:
        return None
