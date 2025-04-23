from flask import Blueprint
from backend.controllers import get_today_weather,get_weather_for_anydate,get_weather_for_period,set_data

consultarClima=Blueprint("consultar_clima",__name__)
configurarDatos=Blueprint("configura_datos",__name__)


consultarClima.route("/get_weather/<ciudad>",methods=['get'])(get_weather_for_anydate)
consultarClima.route('/get_weather/<ciudad>/<date>',methods=['GET'])(get_weather_for_anydate)
consultarClima.route('/get_weather/<ciudad>/<date1>/<date2>',methods=['GET'])(get_weather_for_period)

    
configurarDatos.route('/set_data',methods=['POST'])(set_data)

