(function (window, google, $) {

    "use strict";

    var geocoder, map;

    var zeroPoint = '5328 Newcastle Ave Encino CA 91316';

    function addZeroPoint(address1, icon1) {

        geocoder.geocode({ 'address': address1}, function (results, status) {

            if (status === google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);

                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location,
                    icon: icon1
                });

            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }

    function initialize() {

        geocoder = new google.maps.Geocoder();
        var latlng = new google.maps.LatLng(37.4828, -122.2361);
        var mapOptions = {
                zoom: 10,
                center: latlng
            };
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

        addZeroPoint(zeroPoint, "zero.png");

        $.getJSON('data/company.json', function (data) {

            for (var i in data.companies) {

            	//console.log(i);

            /*
            var output= "<li>"
            + data.jobs[i].employer + "<br/>"
            + data.jobs[i].address + "<br/>";

            for (var p in data.jobs[i].positions)
                {
                    output +=  "<a href='" + data.jobs[i].positions[p].url + "' target='_blank'>" + data.jobs[i].positions[p].position + "</a>";

                    //output += "<ul>";
                    for (var k in data.jobs[i].positions[p].keywords)
                        {
                            output += "<li>";
                            output += data.jobs[i].positions[p].keywords[k];
                            output += "</li>";
                        }
                    //output += "</ul>";


                }

            output += "</li>";
            console.log(output);
            */
            //addMarker(data.jobs[i].address, output)
            console.log(data.companies[i].name);
            //console.log(c.lat);
            if(data.companies[i].lat && data.companies[i].lng)
            	{
            	//console.log(data.companies[i].name + " *** ");
            	addMarker2(data.companies[i].lat, data.companies[i].lng, data.companies[i].name, '');
            	}

            }
        });

    }

    function addMarker2(lat, lng, title1, info1) {

     var latlng = new google.maps.LatLng(lat, lng);

          var marker = new google.maps.Marker({
              map: map,
              position: new google.maps.LatLng(lat, lng), //latlng,
              title: title1
              //icon:icon1
              });

          //google.maps.event.addListener(marker, 'click', function() {
          //  infowindow.open(map,marker);
          //    });
          /*
          google.maps.event.addListener(marker, 'mouseover', function() {
            console.log('mouseover: ' + title1);
            marker.setTitle(title1);
            });
          google.maps.event.addListener(marker, 'mouseout', function() {
            marker.setTitle('');
            });
          */
    }


    google.maps.event.addDomListener(window, 'load', initialize);

}(window, google, $));
