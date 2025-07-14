const selectImage = document.querySelector('.select-image');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-area');

selectImage.addEventListener('click', function () {
	inputFile.click();
})

inputFile.addEventListener('change', function () {
	const image = this.files[0]
	if(image.size < 2000000) {
		const reader = new FileReader();
		reader.onload = ()=> {
			const allImg = imgArea.querySelectorAll('img');
			allImg.forEach(item=> item.remove());
			const imgUrl = reader.result;
			const img = document.createElement('img');
			img.src = imgUrl;
			imgArea.appendChild(img);
			imgArea.classList.add('active');
			imgArea.dataset.img = image.name;
		}
		reader.readAsDataURL(image);
	} else {
		alert("Image size more than 2MB");
	}
})

.css-selector {
    background: linear-gradient(140deg, #e7fff9, #40f9d0, #a9caff);
    background-size: 600% 600%;

    -webkit-animation: AnimationName 43s ease infinite;
    -moz-animation: AnimationName 43s ease infinite;
    -o-animation: AnimationName 43s ease infinite;
    animation: AnimationName 43s ease infinite;
}

@-webkit-keyframes AnimationName {
    0%{background-position:17% 0%}
    50%{background-position:84% 100%}
    100%{background-position:17% 0%}
}
@-moz-keyframes AnimationName {
    0%{background-position:17% 0%}
    50%{background-position:84% 100%}
    100%{background-position:17% 0%}
}
@-o-keyframes AnimationName {
    0%{background-position:17% 0%}
    50%{background-position:84% 100%}
    100%{background-position:17% 0%}
}
@keyframes AnimationName {
    0%{background-position:17% 0%}
    50%{background-position:84% 100%}
    100%{background-position:17% 0%}
}