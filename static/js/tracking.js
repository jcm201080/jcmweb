document.addEventListener("DOMContentLoaded", function() {

    fetch("https://juegos.jesuscmweb.com/api/track", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            ruta: "/",
            origen: "web_principal"
        })
    });

});
