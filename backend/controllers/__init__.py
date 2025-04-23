from flask import request,jsonify,render_template
from backend.services.clima_controler import make_request
from backend.utils.helpers import diferencia_fechas, crearRangoDeFechas, get_today_date



def get_important_conditions(currentConditions):
    key_map = {
        'temp': 'temp',
        'sensacion_terminca': 'feelslike',
        'conditions': 'conditions',
        'humedad': 'humidity',
        'indiceUV': 'uvindex',
        'vel_vientos': 'windspeed',
        'vientos_raf': 'windgust',
        'precipitacion_prob': 'precipprob',
        'datetime': 'datetime'
    }

    return {new_key: currentConditions[orig_key] for new_key, orig_key in key_map.items()}


def procesar_datos_varios_dias(data,ciudad,date1=None,date2=None):

    return_data={
        "ciudad":ciudad
    }
    days_data=[]
    if data is None:
        return None, "No se pudo obtener la información del clima"
    else:
        days = data.get('days', [])

    
    if date1 is not None and date2 is not None:
        dias=diferencia_fechas(date1=date1,date2=date2)
        fechas=crearRangoDeFechas(date1,dias+1)
    else:
        if date1 is not None:
            hoy=date1
        else:
            hoy = get_today_date()
        fechas=crearRangoDeFechas(hoy,1)
        dias=0

    for dia in range(0,dias+1):
        day_data,error=procesar_data(days,fechas[dia],dia)
        
        if error:
            days_data.append({"error": error})
        else:   
            days_data.append(day_data)
    
    return_data["days_data"]=days_data

    return return_data,None
        
def procesar_data(days,fecha,dia=0,):
   
    
    
    currentConditions = days[dia].get('hours') if days and isinstance(days[dia], dict) else None
    
    if not currentConditions:
        return None, "No se pudo obtener la información del clima"
    
    important_conditions = [get_important_conditions(hour) for hour in currentConditions]
    
    general_data = {
        'dia':fecha,
        'sunrise': days[dia].get('sunrise', 'N/A'),
        'sunset': days[dia].get('sunset', 'N/A'),
        'data_for_hours': important_conditions
    }
    
    return general_data,None

def get_today_weather(ciudad):
    data = make_request(ciudad)
    final_data,error=procesar_datos_varios_dias(data,ciudad)
    
    if error:
        return jsonify({'error':error}),500
    
    html_content=render_template("plantillaTarjetasResultados.html",data=final_data)
    return jsonify({'html': html_content})

def get_weather_for_anydate(ciudad,date=None):
    data=make_request(ciudad,date)
    final_data,error=procesar_datos_varios_dias(data,ciudad)
    
    if error:
        return jsonify({'error':error}),500
    
    html_content=render_template("plantillaTarjetasResultados.html",data=final_data)
    return jsonify({'html': html_content})

def get_weather_for_period(ciudad,date1,date2):
    data=make_request(ciudad,date1=date1,date2=date2)
    final_data,error=procesar_datos_varios_dias(data,ciudad,date1=date1,date2=date2)
    if error:
        return jsonify({'error':error}),500
    html_content=render_template("plantillaTarjetasResultados.html",data=final_data)
    
    return jsonify({'html': html_content})
    #return jsonify(data)

def set_data():
    data=request.get_json()
    usuario=data['user']
    ciudad=data['ciudad']