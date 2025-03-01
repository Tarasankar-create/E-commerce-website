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


//cont4 slider
let h_scroll2=document.querySelectorAll('.h_scroll2_img')
let lbtn4=document.querySelector('.lbtn4')
let rbtn4=document.querySelector('.rbtn4')
let counter4=0
let totalscroll2=h_scroll2.length;
h_scroll2.forEach((h_scroll2,i)=>{
    h_scroll2.style.left=`${i*100}%`
})
lbtn4.addEventListener('click',()=>{
    if(counter4>0){
        counter4--;
    }
    else if(counter>=4){
        counter1=0;
    }
    slideImage4();
})
rbtn4.addEventListener('click',()=>{
    if(counter4<totalscroll2-3){
        counter4++;
    }
    else if(counter>=4){
        counter1=0;
    }
    slideImage4();
})
function slideImage4(){
    h_scroll2.forEach((h_scroll2)=>{
        h_scroll2.style.transform=`translateX(-${counter4*100}%)`
    });
}


window.addEventListener('wheel', (e) => {
    if(e.deltaX!==0 || e.shiftKey){
        e.preventDefault();
    }
},{passive:false});

window.addEventListener('touchmove', (e) => {
    if(math.abs(e.touches[0].clientx-e.touches[1]?.clientx)>0){
        e.preventDefault();
    }
},{passive:false});