var floatNav = document.querySelector('.header__container-float');
window.addEventListener('scroll', function () {
	var scrollCount = document.documentElement.scrollTop;
    if (scrollCount > 60) {
        floatNav.classList.remove('hidden');
    } else {
        floatNav.classList.add('hidden');
    }
    behavior: 'smooth';
});