const modalWindow = document.querySelector(".modal");
const modalButton = document.querySelector(".nav__burger");

function showModal() {
    modalWindow.classList.toggle("hidden");
}

modalButton.addEventListener("click", showModal);