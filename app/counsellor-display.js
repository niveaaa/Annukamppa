const SHEET_ID = '1H7s8ONIxq9Fxk1ri8_u5y9x54w0Wsi-_SUC1x3u3Ygs';
const SHEET_NAME = '2024-7-11';

async function fetchData() {
    const response = await fetch(`https://docs.google.com/spreadsheets/d/${SHEET_ID}/gviz/tq?tqx=out:json&sheet=${SHEET_NAME}`);
    const text = await response.text();
    const json = JSON.parse(text.substring(47, text.length - 2));
    return json.table.rows.map(row => row.c.map(cell => cell ? cell.v : ''));
}

function createTable(data) {
    const headerRow = document.getElementById('header-row');
    const dataRows = document.getElementById('data-rows');

    data[0].slice(0, 2).forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });

    data.slice(1).forEach(row => {
        const tr = document.createElement('tr');
        row.slice(0, 2).forEach((cell, index) => {
            const td = document.createElement('td');
            td.textContent = cell;
            td.setAttribute('data-label', data[0][index]);
            tr.appendChild(td);
        });
        dataRows.appendChild(tr);
    });

    createChart(data);
}

function createChart(data) {
    const moods = data.slice(1).map(row => row[1]);

    const moodCounts = moods.reduce((acc, mood) => {
        acc[mood] = (acc[mood] || 0) + 1;
        return acc;
    }, {});

    const labels = Object.keys(moodCounts);
    const counts = Object.values(moodCounts);

    const ctx = document.getElementById('moodChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Number of Students',
                data: counts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Add event listener to download button
document.getElementById('downloadBtn').addEventListener('click', function() {
    const url = `https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?format=xlsx&id=${SHEET_ID}`;
    const link = document.createElement('a');
    link.href = url;
    link.download = 'Student_Report.xlsx';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

fetchData().then(data => {
    createTable(data);
}).catch(error => {
    console.error('Error fetching data:', error);
});
