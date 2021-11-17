let floatNav = document.querySelector('.header__container-float');
window.addEventListener('scroll', function (e) {
    e.preventDefault();
	let scrollCount = document.documentElement.scrollTop;
    if (scrollCount > 60) {
        floatNav.classList.remove('hidden');
    } else {
        floatNav.classList.add('hidden');
    }
   floatNav.getAnimations({
                        behavior: 'smooth' });
        });