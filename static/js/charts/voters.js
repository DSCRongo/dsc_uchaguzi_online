var MaleRegisteredVoters = document.getElementById("males").value;
var FemaleRegisteredVoters = document.getElementById("females").value;


document.addEventListener("DOMContentLoaded", () => {
    echarts.init(document.querySelector("#votersDonutChart")).setOption({
        tooltip: {
        trigger: 'item'
        },
        legend: {
        top: '5%',
        left: 'center'
        },
        series: [{
        name: 'Registered voters',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        label: {
            show: false,
            position: 'center'
        },
        emphasis: {
            label: {
            show: true,
            fontSize: '18',
            fontWeight: 'bold'
            }
        },
        labelLine: {
            show: false
        },
        data: [
            {
                value: FemaleRegisteredVoters,
                name: 'Female(s)'
            },    
            {
            value: MaleRegisteredVoters,
            name: 'Male(s)'
            },
        ]
        }]
    });
    });