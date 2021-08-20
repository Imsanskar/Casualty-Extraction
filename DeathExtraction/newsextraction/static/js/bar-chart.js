// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example

function setBarChart(ctx, labels, values, title) {
	var myLineChart = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: labels,
			datasets: [{
				label: title,
				backgroundColor: "rgba(2,117,216,1)",
				borderColor: "rgba(2,117,216,1)",
				data: values,
			}],
		},
		options: {
			legend: {
				display: false
			},
			scales: {
				yAxes: [{
				ticks: {
					beginAtZero: true,
					min: 0
				}    
				}]
			}
		}
	});
}


