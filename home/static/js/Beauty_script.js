// Main slider
let slide = document.querySelectorAll('.slide');
let lbtn = document.querySelector('.lbtn');
let rbtn = document.querySelector('.rbtn');
let totalImages = slide.length;
let counter = 0;

slide.forEach((slide, i) => {
    slide.style.left = `${i * 100}%`;
});

function slideImage() {
    slide.forEach((slide) => {
        slide.style.transform = `translateX(-${counter * 100}%)`;
    });
}

// Left Button - Move to previous slide
lbtn.addEventListener('click', () => {
    if (counter > 0) {
        counter--;
    }
    slideImage();
});

// Right Button - Move to next slide
rbtn.addEventListener('click', () => {
    if (counter < totalImages - 1) {
        counter++;
    } else {
        counter = 0;
    }
    slideImage();
});

// Auto-Slide
function nextImage() {
    counter++;
    if (counter >= totalImages) {
        counter = 0; 
    }
    slideImage();
}

setInterval(nextImage, 2500);
