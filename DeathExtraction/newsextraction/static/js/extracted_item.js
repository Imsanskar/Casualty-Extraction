
var monthNames = [ "January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December" ];


function setMonth(month){
	month_dom = document.getElementById("month")
	console.log(typeof(month))
	month_dom.textContent = monthNames[month]
	return monthNames[month]
}

function selectedItem(obj, death, injury, day, month, year, vehicleNumber, location, link){
	deathDom = document.getElementById("deathcount")
	injuryDom = document.getElementById("injuredcount")
	vehicleNumberDom = document.getElementById("vehicle_number")
	vehicleDome = document.getElementById("vehicle")
	locationDom = document.getElementById('location')
	linkDom = document.getElementById("link")
	dateDom = document.getElementById("date")
	
	day = obj["day"]
	death = obj["death"]
	injury = obj["injury"]
	month = obj["month"]
	year = obj["year"]
	vehicleNumber = obj["vehicleNumber"]
	location = obj["location"]
	link = obj["link"]
	vehicleType = obj["vehicleType"]


	deathDom.textContent = death
	injuryDom.textContent = injury
	vehicleNumberDom.textContent = vehicleNumber
	locationDom.textContent = location
	linkDom.textContent = link
	vehicleDome.textContent = vehicleType
	dateDom.textContent = `${day} ${month}, ${year}`
	console.log(dateDom.textContent)
}

