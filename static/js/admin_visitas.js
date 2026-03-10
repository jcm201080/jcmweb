document.addEventListener("DOMContentLoaded", function () {

    if (!window.visitasData) return;

    const ctx = document.getElementById('graficaVisitas');

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: window.visitasData.fechas,
            datasets: [{
                label: 'Visitas',
                data: window.visitasData.totales,
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

});


// 📊 Gráfico por horas
const ctxHoras = document.getElementById('graficaHoras');

if (ctxHoras && window.horasData) {
    new Chart(ctxHoras, {
        type: 'bar',
        data: {
            labels: window.horasData.labels,
            datasets: [{
                label: 'Visitas',
                data: window.horasData.totales
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// 📊 Visitas por día de la semana
const ctxDias = document.getElementById('graficaDias');

if(ctxDias && window.diasData){
    new Chart(ctxDias,{
        type:'bar',
        data:{
            labels: window.diasData.labels,
            datasets:[{
                label:'Visitas',
                data: window.diasData.totales
            }]
        },
        options:{
            responsive:true,
            scales:{
                y:{ beginAtZero:true }
            }
        }
    });
}


// 📊 Visitas por mes
const ctxMeses = document.getElementById('graficaMeses');

if(ctxMeses && window.mesesData){
    new Chart(ctxMeses,{
        type:'bar',
        data:{
            labels: window.mesesData.labels,
            datasets:[{
                label:'Visitas',
                data: window.mesesData.totales
            }]
        },
        options:{
            responsive:true,
            scales:{
                y:{ beginAtZero:true }
            }
        }
    });
}