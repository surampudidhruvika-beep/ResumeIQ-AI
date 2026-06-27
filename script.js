// ======================================
// Smooth Scroll
// ======================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener('click', function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({

            behavior:'smooth'

        });

    });

});

// ======================================
// Navbar Shadow
// ======================================

window.addEventListener("scroll",()=>{

    const nav=document.querySelector("nav");

    if(window.scrollY>40){

        nav.style.boxShadow="0 10px 35px rgba(0,0,0,.08)";

    }

    else{

        nav.style.boxShadow="none";

    }

});

// ======================================
// Fade Animation
// ======================================

const observer=new IntersectionObserver(entries=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add("show");

}

});

});

document.querySelectorAll(".feature-card,.step,.upload-card").forEach(el=>{

observer.observe(el);

});

// ======================================
// Counter Animation
// ======================================

const counters=document.querySelectorAll(".stats h2");

counters.forEach(counter=>{

let target=counter.innerText;

let number=parseInt(target);

let count=0;

let interval=setInterval(()=>{

count++;

counter.innerText=count+(target.includes("%")?"%":"+");

if(count>=number){

counter.innerText=target;

clearInterval(interval);

}

},20);

});

// ======================================
// Upload File Name
// ======================================

const fileInput=document.querySelector("input[type=file]");

if(fileInput){

fileInput.addEventListener("change",function(){

if(this.files.length>0){

alert("Selected Resume : "+this.files[0].name);

}

});

}

// ======================================
// Floating Upload Card
// ======================================

const card=document.querySelector(".upload-card");

let moveX=0;

let moveY=0;

document.addEventListener("mousemove",(e)=>{

moveX=(e.clientX/window.innerWidth-0.5)*15;

moveY=(e.clientY/window.innerHeight-0.5)*15;

card.style.transform=`translate(${moveX}px,${moveY}px)`;

});