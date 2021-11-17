
// const anchors = document.querySelectorAll('a[href*="#"]');
// for (let anchor of anchors) {
//   anchor.addEventListener('click', function (e) {
//     e.preventDefault();
    
//     const blockID = anchor.getAttribute('href').substr(1);
    
//     document.getElementById(blockID).scrollIntoView({
//       behavior: 'smooth',
//       block: 'start'
//     });
//   });
// }

document.querySelectorAll('a[href*="#"]').forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();

        const href = this.getAttribute('href').substr(1);
        const scrollTarget = document.getElementById(href);
        const topOffset = 180;
        const elementPosition = scrollTarget.getBoundingClientRect().top;
        const offsetPositiom = elementPosition - topOffset;

        window.scrollBy({
            top: offsetPositiom,
            behavior: 'smooth'
        })
    })
})