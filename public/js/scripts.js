
// PROJECT CARDS

document.addEventListener("DOMContentLoaded", () => {


    const form = document.querySelector('.order_form')

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            let formData = {
                name: form.name.value.trim(),
                email: form.email.value.trim(),
                phone: form.phone.value.trim()
            }

            fetch('http://localhost:8000/api/v1/statement_add', {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Ошибка отправки данных")
                }
                return response.json();
            })
            .then((data) => {
                console.log("Ответ:", data)
                alert("Заявка успешно отправлена")
            })
            .catch((error) => {
                console.error("Ошибка:", error)
                alert('Произошла ошибка при отправке данных')
            })
        });



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
}});