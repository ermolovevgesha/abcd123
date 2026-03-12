$(document).ready(function() {
    var map = L.map('map').setView([53.902278, 27.568981], 10);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    map.on('click', function(point) {
        var lat = point.latlng.lat;
        var lng = point.latlng.lng;

        $.ajax({
            url: '/points/',
            method: 'POST',
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': window.CSRF_TOKEN
            },
            data: JSON.stringify({lat: lat, lng: lng}),
            success: function(data) {
                if (data.status === 'ok') {
                    L.marker([lat, lng]).addTo(map);
                }
            },
            error: function(xhr, status, error) {
                console.error('Ошибка сохранения:', error);
            }
        });
    });
});

