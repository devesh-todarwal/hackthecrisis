Plotly.d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json', function(redjson) {

  Plotly.d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json', function(bluejson) {

    Plotly.newPlot('myDiv', [{
      type: 'scattermapbox',
      lat: [20.59],
      lon: [78.9]
    }], {
      title: "India COVID-19 cases",
      height: 600,
      width: 600,
      mapbox: {
        center: {
          lat: 20.59,
          lon: 78.9
        },
        style: 'light',
        zoom: 3.8,
        layers: [
          {
            sourcetype: 'geojson',
            source: redjson,
            type: 'fill',
            color: 'rgba(163,22,19,0.8)'
          },
          {
            sourcetype: 'geojson',
            source: bluejson,
            type: 'fill',
            color: 'rgba(40,0,113,0.8)'
          },
        ]
      }
    }, {
      mapboxAccessToken: 'pk.eyJ1IjoiZm9yZHByZWZlY3QiLCJhIjoiY2s4a21udThtMDJ0MDNlcDhvMDMyNHFlNCJ9.ychxrJnX9VtKcSFxPchc-g'
    });


});

});
