import datetime
from datetime import date,datetime,timedelta
from dotenv import load_dotenv
import os

load_dotenv()
def get_key_api():
    return os.getenv('API_KEY')

def formatearFechas(date:date):
    formated_date=date.strftime("%Y-%m-%d")
    return formated_date

def get_today_date():
    todaydate=date.today()
    formated_date=formatearFechas(todaydate)

    return formated_date
def diferencia_fechas(date1,date2):
    date1=datetime.strptime(date1,"%Y-%m-%d").date()
    date2=datetime.strptime(date2,"%Y-%m-%d").date()

    diferencia=date1-date2
    return abs(diferencia.days)

def crearRangoDeFechas(fecha_inicial:str,numero_de_fechas):
    inicio = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fechas = [(inicio + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(numero_de_fechas)]  
    return fechas