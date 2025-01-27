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

//cont1 slider
// let h_scroll=document.querySelectorAll('.h_scroll_img')
// let scroller=document.querySelectorAll('.scroller')
// let lbtn1=document.querySelector('.lbtn1')
// let rbtn1=document.querySelector('.rbtn1')
// let counter1=0
// h_scroll.forEach((h_scroll,i)=>{
//     h_scroll.style.left=`${i*100}%`
// })
// lbtn1.addEventListener('click',()=>{
//     if(counter1>0){
//         counter1--;
//     }
//     slideImage1();
// })
// rbtn1.addEventListener('click',()=>{
//     if(counter1<4){
//         counter1++;
//     }
//     else if(counter>=4){
//         counter1=0;
//     }
//     slideImage1();
// })
// function slideImage1(){
//     h_scroll.forEach((h_scroll)=>{
//         h_scroll.style.transform=`translateX(-${counter1*100}%)`
//     });
// }
// document.addEventListener('wheel',(e)=>{
//     if(math.abs(e.deltaX)>math.abs(e.deltaY)){
//         e.preventDefault();
//     }
//     else if(e.shiftkey && math.abs(e.deltaX)>math.abs(e.deltaY)){
//         e.preventDefault();
//     }
// },{passive:false});

const scroller = document.querySelector('.scroller');
const leftButton = document.querySelector('.lbtn1');
const rightButton = document.querySelector('.rbtn1');

// Add event listeners to the buttons to scroll the container
leftButton.addEventListener('click', () => {
  scroller.scrollBy({
    left: -200,  // Scroll 200px to the left
    behavior: 'smooth'  // Smooth scroll
  });
});

rightButton.addEventListener('click', () => {
  scroller.scrollBy({
    left: 200,  // Scroll 200px to the right
    behavior: 'smooth'  // Smooth scroll
  });
});

//cont2 slider
let h_scroll1=document.querySelectorAll('.h_scroll1_img')
let lbtn2=document.querySelector('.lbtn2')
let rbtn2=document.querySelector('.rbtn2')
let counter2=0
let totalscroll1=h_scroll1.length;
h_scroll1.forEach((h_scroll1,i)=>{
    h_scroll1.style.left=`${i*100}%`
})
lbtn2.addEventListener('click',()=>{
    if(counter2>0){
        counter2--;
    }
    else if(counter>=4){
        counter1=0;
    }
    slideImage2();
})
rbtn2.addEventListener('click',()=>{
    if(counter2<totalscroll1-6){
        counter2++;
    }
    else if(counter>=4){
        counter1=0;
    }
    slideImage2();
})
function slideImage2(){
    h_scroll1.forEach((h_scroll1)=>{
        h_scroll1.style.transform=`translateX(-${counter2*100}%)`
    });
}
document.addEventListener('wheel',(e)=>{
    if(math.abs(e.deltaX)>math.abs(e.deltaY)){
        e.preventDefault();
    }
    else if(e.shiftkey && math.abs(e.deltaX)>math.abs(e.deltaY)){
        e.preventDefault();
    }
},{passive:false});

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