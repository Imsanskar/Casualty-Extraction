
var monthNames = [ "January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December" ];


function setMonth(month){
	month_dom = document.getElementById("month")
	console.log(typeof(month))
	month_dom.textContent = monthNames[month]
	return monthNames[month]
}

function selectedItem(death, injury, day, month, year, vehicle, vehicleNumber, location, link){
	deathDom = document.getElementById("deathcount")
	injuryDom = document.getElementById("injuredcount")
	vehicleDom = document.getElementById("vehicle")
	vehicleNumberDom = document.getElementById("vehicle_number")
	locationDom = document.getElementById('location')
	linkDom = document.getElementById("link")
	dateDom = document.getElementById("date")
	

	deathDom.textContent = death
	injuryDom.textContent = injury
	// vehicleDom.textContent = vehicle
	vehicleNumberDom.textContent = vehicleNumber
	locationDom.textContent = location
	linkDom.textContent = link
	dateDom.textContent = `${day} ${month}, ${year}`
	console.log(dateDom.textContent)
}

