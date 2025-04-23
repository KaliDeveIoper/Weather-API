let ciudad = document.getElementById("ciudad").value;
let fecha1 = document.getElementById("fecha1").value;
let fecha2 = document.getElementById("fecha2").value;


const btn = document.getElementById("btn-search");
btn.addEventListener("click",enviarDatos);

function getDatos(){
    ciudad = document.getElementById("ciudad").value;
    fecha1 = document.getElementById("fecha1").value;
    fecha2 = document.getElementById("fecha2").value;
}
function enviarDatos(){
    getDatos()
    consultaAPI(ciudad, fecha1, fecha2);
    
}

function consultaAPI(ciudad,fecha1,fecha2){
    // URL de la API
    const API_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:5000' 
    : 'https://weather-api-7vvp.onrender.com';
    let url = `${API_URL}/api/get_weather/${ciudad}`;
    

    if (fecha1 !== undefined && fecha1 !== "") {
        url += `/${fecha1}`;
        
        if (fecha2 !== undefined && fecha2 !== "") {
            url += `/${fecha2}`;
        }
    }

    console.log(url)
    // Realizamos la solicitud GET con fetch
    fetch(url)
    .then(response => response.json())  // Convertimos la respuesta a JSON
    .then(data => {
        const html = data.html// Mostramos la respuesta de la API
        document.getElementById('resultado').innerHTML = html;
    })
    .catch(error => {
        console.error('Error:', error);  // Si ocurre un error
    });


}