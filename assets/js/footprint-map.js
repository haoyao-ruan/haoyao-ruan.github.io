(function () {
  var el = document.getElementById('footprint-map');
  var data = document.getElementById('footprint-data');
  if (!el || !data || !window.L) return;

  var places = JSON.parse(data.textContent);
  var map = L.map(el, { scrollWheelZoom: false });
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 12,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var points = places.map(function (p) {
    var box = document.createElement('div');
    box.className = 'footprint-popup';
    var heading = document.createElement('strong');
    heading.textContent = p.place;
    box.appendChild(heading);
    var list = document.createElement('ul');
    p.items.forEach(function (text) {
      var li = document.createElement('li');
      li.textContent = text;
      list.appendChild(li);
    });
    box.appendChild(list);
    var pin = document.createElement('span');
    pin.className = 'footprint-pin';
    pin.textContent = p.emoji;
    L.marker([p.lat, p.lng], { icon: L.divIcon({ html: pin, className: '', iconSize: [0, 0] }), title: p.place, alt: p.place })
      .bindTooltip(p.place, { direction: 'top', offset: [0, -16] })
      .bindPopup(box, { offset: [0, -10] })
      .addTo(map);
    return [p.lat, p.lng];
  });

  function fit() {
    map.invalidateSize();
    map.fitBounds(points, { padding: [40, 40] });
  }
  fit();
  // A page opened in a background tab can start with a zero-size map.
  if (window.ResizeObserver) new ResizeObserver(fit).observe(el);
})();
