function openModal(type) {

    const contents = {

        erp: `
            <h3>Enterprise Management System (ERP)</h3>
            <p>Full-stack web application for comprehensive inventory and billing management.</p>
            <ul>
                <li>Modular architecture using Flask Blueprints</li>
                <li>User authentication and role system</li>
                <li>Stock control with validations</li>
                <li>Purchase and supplier management</li>
                <li>Dashboard with analytics (Chart.js & Matplotlib)</li>
                <li>Deployed on Render</li>
            </ul>
        `,

        juegos: `
            <h3>Interactive Gaming Platform – JCM</h3>
            <p>Real-time web platform featuring multiplayer games and dynamic logic.</p>
            <ul>
                <li>Real-time communication with Socket.IO</li>
                <li>Session and user management</li>
                <li>Persistent ranking system</li>
                <li>Modular Flask architecture</li>
                <li>Deployed on Linux VPS</li>
            </ul>
        `,

        ciber: `
            <h3>Log Analysis System – Cybersecurity</h3>
            <p>Automated engine for anomaly detection and suspicious pattern analysis.</p>
            <ul>
                <li>Mass log file processing</li>
                <li>Advanced regular expressions</li>
                <li>Access anomaly detection</li>
                <li>Metric and statistical generation</li>
                <li>Modular Python architecture</li>
            </ul>
        `,

        creacion_en: `
            <h3>Custom Web & Application Development</h3>
            <p>Development of complete web solutions for real businesses.</p>

            <ul>
                <li>Custom admin panel</li>
                <li>Process automation</li>
                <li>AI integration</li>
                <li>VPS deployment</li>
                <li>Mobile-friendly and production-ready</li>
            </ul>

            <p>
                Ideal for restaurants, events, and local businesses looking to digitize their operations.
            </p>

            <!-- 🔥 CTA -->
            <p style="margin-top:10px; font-weight:bold;">
                🚀 Need a custom solution for your business? Let’s talk.
            </p>

            <a href="https://creacion.jesuscmweb.com/" target="_blank" class="btn-proyecto">
                🌐 View project
            </a>
        `,

        burger: `
            <h3>Flask Web Application – Burger's</h3>
            <p>Production-ready web application deployed on a Linux VPS.</p>
            <ul>
                <li>User authentication system</li>
                <li>Database integration</li>
                <li>Dynamic content management</li>
                <li>Modular architecture</li>
                <li>Production deployment environment</li>
            </ul>
        `
    };

    document.getElementById("modalBody").innerHTML = contents[type];
    document.getElementById("modalProyecto").style.display = "flex";
}

function closeModal() {
    document.getElementById("modalProyecto").style.display = "none";
}


/* Close when clicking outside modal */
window.addEventListener("click", function(e) {
    const modal = document.getElementById("modalProyecto");
    if (e.target === modal) {
        closeModal();
    }
});

/* Close with ESC key */
document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
        closeModal();
    }
});
