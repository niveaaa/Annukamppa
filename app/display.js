// scripts.js
function drawSheetName(sheetName, queryString) {
    var query = new google.visualization.Query(
        'https://docs.google.com/spreadsheets/d/1H7s8ONIxq9Fxk1ri8_u5y9x54w0Wsi-_SUC1x3u3Ygs/gviz/tq?sheet=' + sheetName + '&headers=1&tq=' + encodeURIComponent(queryString));
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        console.error('Error in query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }

    var data = response.getDataTable();
    
    // Create a new DataTable for the bar chart
    var moodCounts = new google.visualization.DataTable();
    moodCounts.addColumn('string', 'Mood');
    moodCounts.addColumn('number', 'Number of Students');
    
    // Aggregate the mood counts
    var moodMap = {};
    for (var i = 0; i < data.getNumberOfRows(); i++) {
        var mood = data.getValue(i, 1); // Get the mood value
        if (mood in moodMap) {
            moodMap[mood]++;
        } else {
            moodMap[mood] = 1;
        }
    }
    
    // Add rows to the new DataTable
    for (var mood in moodMap) {
        moodCounts.addRow([mood, moodMap[mood]]);
    }

    // Draw the table
    var table = new google.visualization.Table(document.getElementById('data'));
    table.draw(data, { showRowNumber: false, width: '100%', height: '100%' });
    
    // Adjust table width and center alignment
    var tableDiv = document.getElementById('data');
    tableDiv.style.width = '60  %'; // Set width to 40%
    tableDiv.style.margin = '0 auto'; // Center align the table

    // Draw the vertical bar chart
    var barChart = new google.visualization.BarChart(document.getElementById('chart_div')); // Use BarChart for vertical bars
    var chartOptions = {
        title: 'Number of Students for Each Mood',
        chartArea: { width: '60%'}, // Adjust chart area width
        hAxis: {
            title: 'Number of Students',
            minValue: 0
        },
        vAxis: {
            title: 'Mood',
            textStyle: { fontSize: 14 }
        },
        legend: { position: 'none' } // Hide legend
    };
    barChart.draw(moodCounts, chartOptions);
}

function init() {
    google.charts.load('current', { 'packages': ['corechart', 'table'] });
    google.charts.setOnLoadCallback(function() {
        // Use 'SELECT A, B' to get the columns
        drawSheetName('Sheet1', 'SELECT A, B');
    });
}

window.onload = init;
