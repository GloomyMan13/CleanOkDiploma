let floatNav = document.querySelector('.header__container');
let floatBtn = document.querySelector('.intro__btn-float');
window.addEventListener('scroll', function (e) {
    e.preventDefault();
	let scrollCount = document.documentElement.scrollTop;
    if (scrollCount > 60) {
        floatNav.classList.add('fixed');
        floatBtn.classList.remove('hidden');
    } else {
        floatNav.classList.remove('fixed');
        floatBtn.classList.add('hidden');
    }
floatNav.getAnimations({
                        behavior: 'smooth' });
        });