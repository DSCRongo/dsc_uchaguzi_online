var registeredVoters = document.getElementById("casted-votes").value;
var castedVotes = document.getElementById("registered-voters").value;


document.addEventListener("DOMContentLoaded", () => {
    echarts.init(document.querySelector("#turnoutDonutChart")).setOption({
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center'
        },
        series: [{
            name: 'Voter turnout',
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
                    value: registeredVoters,
                    name: 'Registered voters'
                },
                {
                    value: castedVotes,
                    name: 'Casted votes',
                },
                
            ]
        }]
    })
})