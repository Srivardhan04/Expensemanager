const comboCtx = document.getElementById("incomeExpenseChart").getContext("2d");

const incomeGradient = comboCtx.createLinearGradient(0,0,0,400);
incomeGradient.addColorStop(0,"#22C55E");
incomeGradient.addColorStop(1,"#10B981");

const expenseGradient = comboCtx.createLinearGradient(0,0,0,400);
expenseGradient.addColorStop(0,"#EF4444");
expenseGradient.addColorStop(1,"#F87171");

new Chart(comboCtx, {
  data: {
    labels: {{ months|safe }},
    datasets: [
      {
        type:"bar",
        label:"Expense",
        data: {{ month_totals|safe }},
        backgroundColor: expenseGradient,
        borderRadius: 12
      },
      {
        type:"line",
        label:"Income",
        data: {{ income_totals|safe }},
        borderColor:"#22C55E",
        backgroundColor:"rgba(34,197,94,.15)",
        tension:.4,
        fill:true,
        pointRadius:5
      }
    ]
  },
  options:{
    responsive:true,
    maintainAspectRatio:false,
    animation:{ duration:1500 },
    scales:{
      y:{ beginAtZero:true }
    },
    plugins:{
      legend:{ position:"bottom" }
    }
  }
});