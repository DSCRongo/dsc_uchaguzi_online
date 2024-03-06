const MaleRegisteredVoters = document.getElementById("males").value;
const FemaleRegisteredVoters = document.getElementById("females").value;

// Male Registered Voters
if (MaleRegisteredVoters == 0) {
	var chartLabelForMales = ''
	var colorMaleLabel = '#fff'
}
else {
	var chartLabelForMales = 'Males'
	var colorMaleLabel = '#09ac52'

}

// Female Registered Voters
if (FemaleRegisteredVoters == 0) {
	var chartLabelForFemales = ''
	var colorFemaleLabel = '#fff'
}
else {
	var chartLabelForFemales = 'Females'
	var colorFemaleLabel = '#ec0b0b'
}


document.addEventListener("DOMContentLoaded", () => {
new Chart(document.querySelector('#votersChart'), {
	type: 'doughnut',
	data: {
	labels: [
		chartLabelForMales, chartLabelForFemales
	],
	datasets: [{
		label: 'Registered Voters',
		data: [
			MaleRegisteredVoters, FemaleRegisteredVoters, 
		],
		backgroundColor: [
			colorMaleLabel,
			colorFemaleLabel,
		],
		hoverOffset: 4
	}]
	}
});
});
