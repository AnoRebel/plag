console.log('Initialized..\nStart Plag - ing!');

const plag = document.querySelector('#plag');
const loader = document.querySelector('.loader');
const form = document.querySelector('.form');

const scrollBottom = window.scrollTo({
		behaviour: 'smooth',
		top: document.body.offsetHeight
	});

const scrollTop = window.scrollTo({
		behaviour: 'smooth',
		top: document.body.offsetTop
	});

plag.addEventListener('submit', () => {
	loader.classList.remove('hidden');
	form.classList.add('hidden');
});