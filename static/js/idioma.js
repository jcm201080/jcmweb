(function() {

    const savedLang = localStorage.getItem("preferredLanguage");

    // Si ya estamos en una ruta inglesa, no hacer nada
    if (window.location.pathname.startsWith("/en")) {
        return;
    }

    // Si hay idioma guardado
    if (savedLang === "en") {
        window.location.href = "/en";
        return;
    }

    // Detectar idioma del navegador
    const userLang = navigator.language || navigator.userLanguage;

    if (userLang && userLang.startsWith("en")) {
        window.location.href = "/en";
    }

})();