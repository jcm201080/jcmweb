const boton = document.getElementById("ai-chat-boton")
const ventana = document.getElementById("ai-chat-ventana")
const cerrar = document.getElementById("ai-chat-cerrar")
const enviar = document.getElementById("ai-chat-enviar")
const input = document.getElementById("ai-chat-texto")
const mensajes = document.getElementById("ai-chat-mensajes")

boton.onclick = () => {
    ventana.style.display = "flex"
}

cerrar.onclick = () => {
    ventana.style.display = "none"
}

function agregarMensaje(texto, tipo){

    const div = document.createElement("div")

    div.style.marginBottom="8px"

    if(tipo === "user"){
        div.style.textAlign="right"
    }

    div.innerText = texto

    mensajes.appendChild(div)

    mensajes.scrollTop = mensajes.scrollHeight
}

async function enviarPregunta(){

    const texto = input.value.trim()

    if(!texto) return

    agregarMensaje(texto,"user")

    input.value=""

    const res = await fetch("/api/portafolio_ai",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({pregunta:texto})
    })

    const data = await res.json()

    agregarMensaje(data.respuesta,"bot")
}

enviar.onclick = enviarPregunta

input.addEventListener("keypress",function(e){
    if(e.key==="Enter"){
        enviarPregunta()
    }
})