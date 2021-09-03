
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';



function setPieChart(ctx, labels, data) {
	var ctx = document.getElementById("myPieChart");
	let colors = []

	for(let i = 0; i < data.length; i++){
		r = Math.floor(Math.random() * 150 + 60 * i * Math.random());
		g = Math.floor(Math.random() * 150 + 50 * i * Math.random());
		b = Math.floor(Math.random() * 150 + 70 * i * Math.random());
		color = 'rgb(' + r + ', ' + g + ', ' + b + ')';
		colors.push(color)
	}

	var myPieChart = new Chart(ctx, {
		type: 'pie',
		data: {
			labels: labels,
			datasets: [{
				data: data,
				backgroundColor: colors,
			}],
		},
	});
}
