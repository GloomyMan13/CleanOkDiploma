
	let position = 0;
	const slidesToShow = 4;
	const slidesToScroll = 1;
	const container =  document.querySelector(".slider-container");
	const track = document.querySelector(".slider-track");
	const items = document.querySelectorAll(".slider-item");
	const btnPrev = document.querySelector(".btn-prev");
	const btnNext = document.querySelector(".btn-next");
	const itemsCount = items.length;
	const itemWidth = 263;
	const gap = 40;
	const movePosition = slidesToScroll * itemWidth;

	items.forEach((item) => {
		item.style.minWidth = `${itemWidth}px`;
		// alert(itemsCount);
		// alert(itemWidth);
	});

	
	btnNext.addEventListener("click", () => {
		// const itemsLeft = itemsCount - (Math.abs(position) + slidesToShow * itemWidth) / itemWidth;
		// alert(itemsLeft);
		position -= movePosition  + gap;
		setPosition();
		checkBtns ();
	});

	btnPrev.addEventListener("click", () => {
		// const itemsLeft = Math.abs(position) / itemWidth;
		position += movePosition + gap;
		
		setPosition();
		checkBtns ();
		
	});

	const setPosition = () => {
		track.style.transform = `translateX(${position}px)`;
		
	};

	const checkBtns = () => {
		btnPrev.disabled = position === 0;
		btnNext.disabled = position<= - (itemsCount - slidesToShow) * itemWidth;
		
	};

	checkBtns ();
