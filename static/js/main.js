(function() {
	"use strict";

	// Easy selector helper function
	const select = (el, all = false) => {
		el = el.trim()
		if (all) {
			return [...document.querySelectorAll(el)]
		} else {
			return document.querySelector(el)
		}
	}

	// Easy event listener function
	const on = (type, el, listener, all = false) => {
		if (all) {
			select(el, all).forEach(e => e.addEventListener(type, listener))
		} else {
			select(el, all).addEventListener(type, listener)
		}
	}

	// Easy on scroll event listener 
	const onscroll = (el, listener) => {
		el.addEventListener('scroll', listener)
	}

	// sidebar toggle
	if (select('.toggle-sidebar-btn')) {
		on('click', '.toggle-sidebar-btn', function(e) {
			select('body').classList.toggle('toggle-sidebar')
		})
	}

	// Search bar toggle
	if (select('.search-bar-toggle')) {
		on('click', '.search-bar-toggle', function(e) {
			select('.search-bar').classList.toggle('search-bar-show')
		})
	}

	// Toggle .header-scrolled class to #header when page is scrolled
	let selectHeader = select('#header')
	if (selectHeader) {
		const headerScrolled = () => {
			if (window.scrollY > 100) {
				selectHeader.classList.add('header-scrolled')
			} else {
				selectHeader.classList.remove('header-scrolled')
			}
		}
		window.addEventListener('load', headerScrolled)
		onscroll(document, headerScrolled)
	}

	// back to top button
	let backtotop = select('.back-to-top')
	if (backtotop) {
		const toggleBacktotop = () => {
		if (window.scrollY > 100) {
			backtotop.classList.add('active')
		} else {
			backtotop.classList.remove('active')
		}
		}
		window.addEventListener('load', toggleBacktotop)
		onscroll(document, toggleBacktotop)
	}

	// Preloader
	let preloader = select('#preloader');
	if (preloader) {
		setTimeout(() => {
			preloader.remove();
		}, 1000)	// preloader timeout: 1s
		
		const showPreloader = () => {
            preloader.style.display = 'block';
        };
        const hidePreloader = () => {
            preloader.style.display = 'none';
        };

        document.body.addEventListener('htmx:configRequest', showPreloader);
        document.body.addEventListener('htmx:responseEnd', hidePreloader);
        document.body.addEventListener('htmx:afterRequest', hidePreloader);
	}

	// countdown timer
	let countdown = select('.countdown');
	const output = countdown.innerHTML;
  
	const countDownDate = function() {
		let timeleft = new Date(countdown.getAttribute('data-count')).getTime() - new Date().getTime();
	
		let days = Math.max(Math.floor(timeleft / (1000 * 60 * 60 * 24)), 0);
		let hours = Math.max(Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)) - 3, 0);
		let minutes = Math.max(Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60)), 0);
		let seconds = Math.max(Math.floor((timeleft % (1000 * 60)) / 1000), 0);
	
		countdown.innerHTML = output.replace('%d', days).replace('%h', hours).replace('%m', minutes).replace('%s', seconds);

		// Check if the countdown has reached 0:0:00:00
		if (days <= 0 && hours <= 0 && minutes <= 0 && seconds <= 0) {
			// Countdown has reached zero, display the message
			countdown.innerHTML = "Voting is now open! Refresh page to see changes.";
			clearInterval(interval);
		} else {
			// Update the countdown display
			countdown.innerHTML = output.replace('%d', days).replace('%h', hours).replace('%m', minutes).replace('%s', seconds);
		}
	}
	countDownDate();
	const interval = setInterval(countDownDate, 1000);

})();