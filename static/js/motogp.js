document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".gp-card");
    const today = new Date();

    let nextRace = null;
    let smallestDiff = Infinity;

    cards.forEach(card => {
        const startDate = new Date(card.dataset.start);
        const endDate = new Date(card.dataset.end);

        // Carrera en curso
        if (today >= startDate && today <= endDate) {
            card.classList.add("live");
            card.setAttribute("data-status", "LIVE");
        }

        // Próxima carrera
        if (startDate > today) {
            const diff = startDate - today;
            if (diff < smallestDiff) {
                smallestDiff = diff;
                nextRace = card;
            }
        }
    });

    if (nextRace) {
        nextRace.classList.add("next");
        nextRace.setAttribute("data-status", "NEXT");
    }

});