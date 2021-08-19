$(document).ready(function () {
  // execute
  (function () {
    let locations = [
      ["Bhaktapur", 27.671, 85.4298],
      ["Lalitpur", 27.6588, 85.3247],
      ["kathmandu", 27.7172, 85.324],
      ["pulchwok", 27.6782, 85.3169],
      ["baneshwor", 27.6915, 85.342],
      ["jhapa", 26.5455, 87.8942],
      ["ilam", 26.9112, 87.9237],
      ["panchthar", 27.1096, 87.8157],
      ["taplejung", 27.354, 87.668],
      ["morang", 26.6799, 87.4604],
      ["sunsari", 26.6276, 87.1822],
      ["bhojpur", 27.178, 87.0524],
      ["dhankuta", 26.9835, 87.3215],
      ["terhathum", 27.1998, 87.5791],
      ["sankhuwasabha", 27.6174, 87.3016],
      ["saptari", 26.6191, 86.7819],
      ["siraha", 26.6397, 86.1853],
      ["udayapur", 26.8518, 86.6611],
      ["khotang", 27.1838, 86.7819],
      ["okhaldhunga", 27.324, 86.5047],
      ["solukhumbu", 27.6992, 86.7416],
      ["dhanusa", 26.835, 86.0122],
      ["mahottari", 26.6943, 85.823],
      ["sarlahi", 26.9627, 85.5612],
      ["sindhuli", 27.2569, 85.9713],
      ["dolakha", 27.7784, 86.1752],
      ["dhading", 27.9711, 84.8985],
      ["kavre", 27.5285, 85.6435],
      ["nuwakot", 27.9194, 85.1661],
      ["rasuwa", 28.1755, 85.3963],
      ["sindhupalchok", 27.9512, 85.6846],
      ["bara", 27.1341, 85.0649],
      ["parsa", 27.219, 84.8151],
      ["rautahat", 26.9547, 85.3136],
      ["chitwan", 27.5291, 84.3542],
      ["Bhimsengola", 27.6996, 85.3427],
      ["Mahadevsthan", 27.6966, 85.3414],
      ["Anamnagar", 27.6977, 85.3298],
      ["Thapagaon", 27.6984, 85.373],
      ["Minbhavan", 27.6866, 85.3366],
      ["Shankhamul", 27.6853, 85.3317],
      ["Bhuddhanagar", 27.6867, 85.3304],
      ["shantinagar", 27.6915, 85.342],
      ["Hanumansthan", 27.6936, 85.3282],
      ["Singhadurbar", 27.698, 85.3239],
      ["Thapathali", 27.6894, 85.3227],
      ["Jwagal", 27.6858, 85.3233],
      ["Kupondole", 27.6862, 85.3149],
      ["makwanpur", 27.5546, 85.0233],
      ["gorkha", 28.2964, 84.8568],
      ["kaski", 28.2622, 84.0167],
      ["lamjung", 28.2765, 84.3542],
      ["syangja", 28.0197, 83.8049],
      ["tanahun", 27.9447, 84.2279],
      ["manang", 28.6667, 84.0167],
      ["kapilvastu", 27.5518, 83.0469],
      ["nawalparasi", 27.6572, 84.059],
      ["rupandehi", 27.533, 83.3789],
      ["arghakhanchi", 27.894, 83.122],
      ["gulmi", 28.0889, 83.2934],
      ["palpa", 27.8253, 83.6348],
      ["baglung", 28.2774, 83.5816],
      ["myagdi", 28.6029, 83.3362],
      ["parbat", 28.2246, 83.6987],
      ["dang", 28.0, 82.4753],
      ["pyuthan", 28.1017, 82.8533],
      ["rolpa", 28.3816, 82.6483],
      ["rukum", 28.6947, 82.4319],
      ["salyan", 28.4014, 82.1714],
      ["dolpa", 29.0539, 83.0791],
      ["humla", 30.0052, 81.9535],
      ["jumla", 29.2522, 82.1659],
      ["kalikot", 29.2089, 81.7349],
      ["mugu", 29.8086, 82.5186],
      ["banke", 28.1022, 81.8224],
      ["bardiya", 28.3102, 81.4279],
      ["surkhet", 28.5175, 81.7787],
      ["dailekh", 28.9262, 81.6473],
      ["jajarkot", 28.7396, 82.204],
      ["kailali", 28.8314, 80.8987],
      ["achham", 29.0396, 81.2519],
      ["doti", 29.2006, 80.8987],
      ["bajhang", 29.7767, 81.2519],
      ["bajura", 29.4201, 81.4279],
      ["kanchanpur", 28.8372, 80.3213],
      ["dadeldhura", 29.2188, 80.4994],
      ["baitadi", 29.5186, 80.4688],
      ["darchula", 29.9363, 80.8987],
      ["daunne", 27.51, 83.84],
      ["chabahil", 27.7166, 85.3485],
      ["sukedhara", 27.7286, 85.3456],
      ["dhumbarahi", 27.7252, 85.3433],
      ["maharajgunj", 27.1446, 83.5622],
      ["balaju", 27.7309, 85.2955],
      ["basundhara", 27.7418, 85.333],
      ["samakhusi", 27.7273, 85.3175],
      ["gongabu", 27.7493, 85.3214],
      ["Narayan gopal chowk ", 27.7404, 85.3375],
      ["New buspark ", 27.7324, 85.3081],
      ["machhapokhari", 27.7353, 85.3058],
      ["Sano bharyang", 27.7208, 85.2891],
      ["Thulo bharyang", 27.7197, 85.2867],
      ["banasthali", 27.7213, 85.2923],
      ["swoyambhu", 27.7148, 85.2904],
      ["chhauni", 27.7088, 85.2916],
      ["halchok", 27.7202, 85.2813],
      ["sitapaila", 27.717, 85.2735],
      ["tahachal", 27.7037, 85.291],
      ["syuchatar", 27.701, 85.2748],
      ["Old Naikap", 27.699094, 85.263192],
      ["New Naikap", 27.690405, 85.26578],
      ["kalimati", 27.7, 85.2891],
      ["kalanki", 27.6931, 85.2807],
      ["ravibhavan", 27.6951, 85.2949],
      ["kuleshwor", 27.69, 85.2955],
      ["sanepa", 27.6844, 85.3059],
      ["balkhu", 27.6863, 85.2949],
      ["tinthana", 27.6846, 85.2684],
      ["dhobighat", 27.677, 85.302],
      ["ekantakuna", 27.6678, 85.3104],
      ["baghdol", 27.6711, 85.2994],
      ["chobhar", 27.6664, 85.2904],
      ["nakhkhu", 27.6625, 85.3072],
      ["nayabasti", 27.085, 85.0883],
      ["kusunti", 27.5522, 85.3863],
      ["satdobato", 27.6515, 85.3278],
      ["khumaltar", 27.6485, 85.3253],
      ["gwarko", 27.6663, 85.333],
      ["koteshwor", 27.6756, 85.3459],
      ["subidhanagar", 27.685, 85.3453],
      ["tinkune", 27.6915, 85.2959],
      ["gairigaon", 27.6881, 85.3492],
      ["jagritinagar", 27.694, 85.3492],
      ["sinamangaal", 27.6991, 85.3511],
      ["gaucharan", 27.7037, 85.3575],
      ["airport", 27.6981, 85.3592],
      ["gaushala", 26.9112, 85.7974],
      ["battisputali", 27.7055, 85.344],
      ["siphal", 27.7134, 85.3408],
      ["boudha", 27.7215, 85.362],
      ["jorpati", 27.7278, 85.3782],
      ["makalbari", 27.7303, 85.3866],
      ["mulpani", 27.711, 85.3989],
      ["danchhi", 27.729, 85.4143],
      ["bhadrabas", 27.7366, 85.4234],
      ["sankhu", 27.5125, 85.3291],
      ["gaurighat", 27.7133, 85.3495],
      ["kumarigal", 27.7139, 85.3563],
      ["Old Baneshwor", 27.7025, 85.3414],
      ["New Baneshwor", 27.6915, 85.342],
      ["Chakupat", 27.68261, 85.32496],
      ["Imukhel", 27.678, 85.3257],
      ["Patandhoka", 27.6791, 85.3214],
      ["Mangalbazaar", 27.6749, 85.3278],
      ["Kumaripati", 27.6699, 85.3204],
      ["Manbhavan", 27.6687, 85.3175],
      ["Lagankhel", 27.666, 85.3227],
      ["Thasikhel", 27.6679, 85.3143],
      ["Imadol", 27.6564, 85.342],
      ["hattiban", 27.6504, 85.3369],
      ["shorakhutte", 27.6309, 85.306],
      ["kirtipur", 27.663, 85.2774],
      ["chandragiri", 13.5881, 79.3156],
      ["gurjudhara", 27.6863, 85.2415],
      ["satungal", 27.6825, 85.249],
      ["tinthana", 27.6846, 85.2684],
      ["thankot", 27.6868, 85.2024],
      ["nagarjun", 27.7325, 85.2567],
      ["ranibari", 27.7313, 85.3191],
      ["panipokhari", 27.7364, 85.3278],
      ["goldhunga", 27.7598, 85.2852],
      ["dharmasthali", 27.7603, 85.3007],
      ["manamaiju", 27.749, 85.311],
      ["mudkhu", 27.7604, 85.2713],
      ["bansbari", 27.8009, 85.5561],
      ["golfutar", 27.7459, 85.3485],
      ["mahankal", 27.7504, 85.3524],
      ["tokha", 27.7701, 85.3293],
      ["budhanilkantha", 27.7654, 85.3653],
      ["suntakhan", 27.7752, 85.3937],
      ["baluwa", 27.7721, 85.3911],
      ["bhangal", 27.763, 85.3582],
      ["chunikhel", 27.7569, 85.373],
      ["nayapati", 27.7581, 85.4092],
      ["kapan", 27.736, 85.3601],
      ["sundarijal", 27.7909, 85.4272],
      ["gokarna", 14.5479, 74.3188],
      ["chandol", 27.7323, 85.3369],
      ["baluwatar", 27.7255, 85.3298],
      ["bhatbhateni", 27.7212, 85.3324],
      ["naxal", 27.7159, 85.3278],
      ["lazimpat", 27.7215, 85.3201],
      ["lainchaur", 27.7213, 85.3149],
      ["thamel", 27.7154, 85.3123],
      ["narayanhiti", 27.7157, 85.32],
      ["Bulbule", 28.5814, 81.6198],
      ["Sano gaucharan", 27.7155, 85.3362],
      ["gyaneshwor", 27.7102, 85.333],
      ["hattisar", 27.7121, 85.3246],
      ["durbarmarg", 27.7101, 85.3172],
      ["kutubahal", 27.7156, 85.3414],
      ["maligaon", 26.1504, 91.696],
      ["kamaladi", 27.709, 85.3194],
      ["bagbazar", 27.7047, 85.3194],
      ["ghattekulo", 27.7021, 85.3311],
      ["putalisadak", 27.7029, 85.3223],
      ["Bhrikuti mandap", 27.701, 85.3201],
      ["tripureshwor", 27.695, 85.3149],
      ["bhotebahal", 27.6981, 85.3101],
      ["teku", 27.6954, 85.3039],
      ["ason", 27.7077, 85.312],
      ["indrachowk", 27.7061, 85.3094],
      ["nardevi", 27.7074, 85.3043],
      ["chhetrapati", 27.7112, 85.3088],
      ["dallu", 27.712, 85.2994],
      ["jhamsikhel", 27.6829, 85.302],
      ["jawalakhel", 27.6744, 85.3123],
      ["dakchhinkali", 27.6215, 85.2619],
      ["khusibun", 27.718, 85.302],
      ["tengal", 27.7101, 85.3065],
      ["Bishal bazar", 27.7041, 85.3096],
      ["sundhara", 27.7, 85.3117],
      ["khichapokhari", 27.7018, 85.3107],
      ["bhadrakali", 22.6754, 88.347],
      ["shreenagar", 27.7173, 85.3303],
      ["jyatha", 27.7118, 85.313],
      ["pakanajol", 27.715, 85.3085],
      ["dhobichaur", 27.7134, 85.3068],
      ["siddhitol", 27.7366, 85.3117],
      ["pragatinagar", 27.6799, 84.1804],
      ["lokanthali", 27.6738, 85.3595],
      ["kausaltar", 27.6755, 85.3659],
      ["gatthaghar", 27.6765, 85.3743],
      ["thimi", 27.6782, 85.3808],
      ["changunarayan", 27.7033, 85.4324],
    ];
	console.log(locationList)

	var locationMap = new Map()
	
	for(let i = 0; i < locations.length; i++){
		locationMap[locations[i][0].toLowerCase()] = [locations[i][1], locations[i][2]]
	}

    // map options
    let options = {
      zoom: 16,
      center: new google.maps.LatLng(27.7172, 85.324), // centered kathmandu
      mapTypeId: google.maps.MapTypeId.ROADMAP,
    };

    // init map
    let map = new google.maps.Map(
      document.getElementById("mapcontainer"),
      options
    );

    // set multiple marker
    for (let i = 0; i < locationList.length; i++) {
      // init markers
	  let position = locationMap[locationList[i].toLowerCase()]
      let marker = new google.maps.Marker({
		optimized: false,
        position: new google.maps.LatLng(position[0], position[1]),
        map: map,
        title: `
			Place: ${locationList[i]}\nDeath: ${countDeathNumber[locationList[i]]}\nInjury: ${countInjuryNumber[locationList[i]]}\nNo. of accident: ${countAccident[locationList[i]]}
		`,
      });
    }
  })();
});