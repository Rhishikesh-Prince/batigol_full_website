// AOS animation
AOS.init({
	duration:1000,
	once:true
});


// Hero image slider

const slides = document.querySelectorAll(".slide");

let currentSlide = 0;

function showSlide(){

	slides.forEach(slide=>{
		slide.classList.remove("active");
	});

	currentSlide++;

	if(currentSlide >= slides.length){
		currentSlide = 0;
	}

	slides[currentSlide].classList.add("active");

}

setInterval(showSlide,3000);


// product cards 
$(document).ready(function(){

	$(".products-carousel").owlCarousel({

		loop:true,
		margin:30,
		autoplay:true,
		autoplayTimeout:3000,
		autoplayHoverPause:true,

		responsive:{
			0:{
				items:1
			},
			600:{
				items:2
			},
			1000:{
				items:3
			}
		}

	});

});
// testi 

$(document).ready(function(){

	$(".testimonials-carousel").owlCarousel({

		loop:true,
		margin:30,
		autoplay:true,
		autoplayTimeout:3000,
		autoplayHoverPause:true,

		responsive:{
			0:{
				items:1
			},
			600:{
				items:2
			},
			1000:{
				items:3
			}
		}

	});

});