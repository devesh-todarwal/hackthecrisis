var color = d3.scale.category20();
jsnx.draw(G, {
    element: '#canvas',
    layoutAttr: {
        charge: -120,
        linkDistance: 20
    },
    nodeAttr: {
        r: 5,
        title: function(d) { return d.label;}
    },
    nodeStyle: {
        fill: function(d) {
            return color(d.data.group);
        },
        stroke: 'none'
    },
    edgeStyle: {
        fill: '#999'
    },
    edge_style: {
      'stroke': function(d) {
              return d.data.color|| '#AAA';
            },
      'stroke-width': 2
    }    
    withLabels: true,
    labels: 'label',
});
