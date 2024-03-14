var positiveFeedback = document.getElementById("positive-feedback").value;
var negativeFeedback = document.getElementById("negative-feedback").value;
var neutralFeedback = document.getElementById("neutral-feedback").value;
console.log(`Positive feedback: ${positiveFeedback}, Negative feedback: ${negativeFeedback}, neutral feedback: ${neutralFeedback}`)

document.addEventListener("DOMContentLoaded", () => {
    echarts.init(document.querySelector("#feedbackDonutChart")).setOption({
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center'
        },
        series: [{
            name: 'Survey: How was the election?',
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
                    value: neutralFeedback,
                    name: "I'm not sure"
                },
                {
                    value: negativeFeedback,
                    name: 'Unfair',
                },
                {
                    value: positiveFeedback,
                    name: 'Fair'
                }
            ]
        }]
    })
})