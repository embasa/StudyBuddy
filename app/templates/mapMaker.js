// This java script file creates a google map with markers
var map;
var inforWindow;
var markers = [
	       { 
		   lat: 36.9740497,
		   lng: -122.0260089,
		   name: "study sesh1",
		   address1: "Santa Cruz Coffee Roasters",
		   address2: "Pac Ave",
		   postalCode:"95060"
	       },
	       {
		   lat: 36.976349,
		   lng: -122.0292952,
		   name: "study sesh2",
		   address1: "Lulu Carpenters",
		   address2: "Pac Ave",
		   postalCode:"95060"
	       },
	       {      
		   lat: lng, 37.000353,
		   lng:-122.0631443,
		   name: "study sesh3",
		   address1: "Jack Baskin",
		   address2: "UC Santa Cruz",
		   postalCode:"95064"
	       }
	       ];

function initiliazeMap() {
    var mapOps = {
        center: new google.maps.LatLng(36.976349,-122.0292952),
        zoom: 8,
        mapTypeId: 'roadmap',
    };
    
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOps);
    infoWindow = new google.maps.InfoWindow();
    // Closes infoWin after a click on map
    google.maps.event.addListener(map, 'click', function() {
	    infoWindow.close();
        });
    
    // DISPLAY THEM                                                                                                                                                                  
    displayMarkers();
}
google.maps.event.addDomListener(window, 'load', initializeMap);


function displayMarkers(){
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0; i< markers.length; i++){
	var latlng = new google.maps.LatLng(markers[i].lat, markers[i].lng);
	var name = markers[i].name;
	var add1 = markers[i].address1;
	var add2 = markers[i].address2;
	var pCode = markers[i].postalCode;
	createMarker(latlng, name, add1, add2, pCode);
	bounds.extend(latlng);
    }
    map.fitBounds(bounds);
}

function createMarker(latlng, name, add1, add2, pCode){
    var marker = new google.maps.Marker({
	    map: map,
	    position: latlng,
	    title: name
	});
    
    google.maps.event.addListener(marker, 'click', function() {	    
	    var iwContent = '<div id="iw_container">' +
		'<div class="iw_title">' + name + '</div>' +
		'<div class="iw_content">' + add1 + '<br />' +
		add2 + '<br />' +
		pCode + '</div></div>';
	    //includes content in infoWindow
	    infoWindow.setContent(iwContent);
	    infoWindow.open(map, marker); // open in map at marker loc
	});
}
