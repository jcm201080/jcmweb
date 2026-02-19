(function() {

    const savedLang = localStorage.getItem("preferredLanguage");

    if (savedLang) {
        if (savedLang === "en" && !window.location.pathname.includes("index-en")) {
            window.location.href = "index-en.html";
        }
        return;
    }

    const userLang = navigator.language || navigator.userLanguage;

    if (userLang.startsWith("en")) {
        window.location.href = "index-en.html";
    }

})();
