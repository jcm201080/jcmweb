function abrirModal(tipo) {

    const contenidos = {
        erp: `
            <h3>Sistema de Gestión Empresarial (ERP)</h3>
            <p>Aplicación web full-stack para gestión integral de inventario y facturación.</p>
            <ul>
                <li>Arquitectura modular con Blueprints</li>
                <li>Sistema de autenticación y roles</li>
                <li>Control de stock con validaciones</li>
                <li>Gestión de compras y proveedores</li>
                <li>Dashboard con métricas (Chart.js & Matplotlib)</li>
                <li>Deploy en Render</li>
                <li>Separación por Blueprints y capas</li>
                <li>Validaciones backend</li>
                <li>Gestión de sesiones segura</li>

            </ul>
        `,
        juegos: `
            <h3>Plataforma Interactiva Juegos JCM</h3>
            <p>Plataforma web con juegos multijugador y lógica en tiempo real.</p>
            <ul>
                <li>Socket.IO</li>
                <li>Gestión de sesiones</li>
                <li>Ranking persistente</li>
                <li>Arquitectura modular</li>
                <li>Deploy en VPS</li>
                <li>Gestión de salas dinámicas</li>
                <li>Sincronización estado servidor-cliente</li>

            </ul>
        `,
        ciber: `
            <h3>Sistema de Análisis de Logs – Ciberseguridad</h3>
            <p>Motor de detección de anomalías y patrones sospechosos.</p>
            <ul>
                <li>Procesamiento masivo de logs</li>
                <li>Expresiones regulares avanzadas</li>
                <li>Generación de métricas</li>
                <li>Arquitectura modular en Python</li>
                <li>Parsing estructurado de logs (Apache/Nginx)</li>
                <li>Detección de patrones sospechosos</li>
            </ul>
        `,
        burger: `
            <h3>Aplicación Web Flask – Burger's</h3>
            <p>Aplicación desplegada en entorno de producción.</p>
            <ul>
                <li>Autenticación de usuarios</li>
                <li>Integración con base de datos</li>
                <li>Gestión dinámica de contenidos</li>
                <li>Arquitectura modular</li>
                <li>Deploy en VPS Linux</li>
            </ul>
        `
    };

    document.getElementById("modalBody").innerHTML = contenidos[tipo];
    document.getElementById("modalProyecto").style.display = "flex";
}

function cerrarModal() {
    document.getElementById("modalProyecto").style.display = "none";
}


/* ------------------------------
   LISTENERS GLOBALES (solo una vez)
--------------------------------*/

window.addEventListener("click", function(e) {
    const modal = document.getElementById("modalProyecto");
    if (e.target === modal) {
        cerrarModal();
    }
});

document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
        cerrarModal();
    }
});
