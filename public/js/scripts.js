
// PROJECT CARDS

document.addEventListener("DOMContentLoaded", () => {
    // Выбираем все элементы, чьи классы начинаются с "card"
    const cards = document.querySelectorAll('[class^="card"]');

    cards.forEach(card => {
        const cardLink = card.querySelector(".card_link");

        if (cardLink) {
            card.addEventListener("mouseenter", () => {
                cardLink.classList.add("show");
            });

            card.addEventListener("mouseleave", () => {
                cardLink.classList.remove("show");
            });
        }
    });
});