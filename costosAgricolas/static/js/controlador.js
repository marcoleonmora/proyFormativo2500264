//************ FUNCIONES AUXILIARES ************************************************************** */

/**
 * Consulta AJAX al servidor por método POST
 * @param {string} urlserver :Direccion de envio
 * @param {string} datos     :Data en formato JavaScript object
 * @param {function} callBackFunction : Funcion de retorno
 */
function mensajeAjax(urlserver, datos, callBackFunction) {
    const csrftoken = getCookie('csrftoken');
    fetch(urlserver, {
        method: 'post',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(datos) //JavaScript object of data to POST
    })
        .then(response => response.json())  //Convierte la respuesta JSON en data
        .then(data => {
            callBackFunction(data)
        })
        .catch((error) => {
            console.error('Error:', JSON.stringify(error));
        });
}

/**
 * Lee la Cookie del navengador para validar el token de seguridad
 * @param {*} name Nombre de la cookie
 * @returns el contenido de la cookie
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//********************************************************************************/

window.onload = (event) => {
    if (document.getElementById('id_categoria') !== null) {
        document.getElementById('id_categoria').addEventListener('change', consultarCategHora, false)
    }
};

//Manejadores de eventos ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function consultarCategHora() {
    let id = document.getElementById('id_categoria').value;
    if (id != '0') {
        let url = "http://localhost:8000/apAdmin/hora/";
        let datos = {
            'id': id,
        };
        mensajeAjax(url, datos, consultarCategHoraResp);
    } else {
        document.getElementById('id_descripCategHora').value = '';
        document.getElementById('id_recargo').value = '';
    }
}

function consultarCategHoraResp(data) {
    document.getElementById('id_descripCategHora').value = data['descripCategHora'];
    document.getElementById('id_recargo').value = data['recargo'];
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

function mostrarDescrip() {
    let id = document.getElementById('insumo_id').value;
    let url = "http://localhost:8000/apAdmin/insumos/";
    let datos = {
        'id': id,
    };
    mensajeAjax(url, datos, mostrarDescripResp);
}

function mostrarDescripResp(data) {
    document.getElementById('descripInsumo').value = data['descripInsumo'];
    document.getElementById('categ_id').value = data['categMaterial'];
    document.getElementById('unidad_id').value = data['unidadMedida'];
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//global

function filtrarInsumos() {
    let idCateg = document.getElementById('categ_id').value;
    let idUnidad = document.getElementById('unidad_id').value;
    let listaOpciones = document.getElementById('insumo_id').options;

    let caso = 0
    if (idCateg > '0') caso += 1;
    if (idUnidad > '0') caso += 2;
    
    //Primero deja todo visible
    for (let i = 1; i < listaOpciones.length; i++) {
        listaOpciones[i].removeAttribute("hidden");
    }

    switch (caso) {
        case 1:         //Unidad en cero, categ > 0: Filtrar solo por categ
            for (let i = 1; i < listaOpciones.length; i++) {
                if (listaOpciones[i].dataset.categ != idCateg) {
                    listaOpciones[i].setAttribute("hidden", "hidden");
                } 
            }
            break;

        case 2:         //caso = 2: Categ en cero,, unidad > 0: Filtrar solo por unidad
            for (let i = 1; i < listaOpciones.length; i++) {
                if (listaOpciones[i].dataset.unidad != idUnidad) {
                    listaOpciones[i].setAttribute("hidden", "hidden");
                } 
            }
            break;
        case 3:         //caso = 3: Unidad > 0, categ > 0: Filtrar solo por categ
            for (let i = 1; i < listaOpciones.length; i++) {
                if (listaOpciones[i].dataset.unidad != idUnidad  || listaOpciones[i].dataset.categ != idCateg) {
                    listaOpciones[i].setAttribute("hidden", "hidden");
                } 
            }
            break;
    }
}


//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function filtrarUnidad() {

}