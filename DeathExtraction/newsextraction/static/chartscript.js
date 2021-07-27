let chart = document.getElementById("charts").getContext("2d");

let casultyChart = new Chart(chart, {
    type: 'bar',
    data:{
        labels:['bike', 'car' ,'bus','truck'],
        datasets:[{
            label:'accident',
            data:[
                100,
                4000,
                500,
                6000
            ]
        }]
    },
    options:{},

})