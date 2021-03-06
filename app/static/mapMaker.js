//This java script file creates a google map with markers!
//Here is a sample call, which adds a study session pin point
//on the map at latude = args[0] and longitude = args[1]
//intialize(36.9765546,-122.0323493,"Breakfast at?","The Abbey");
function initializeMyShit(listings2){
var map;
var infoWindow;
var testArray = [];
var adjustment = 0.02;
for(j = 0;j<listings2.length;j+=3){
    testArray.push({
		   lat: 36.9740497 + adjustment,
		   lng: -122.0260089 + adjustment,
		   name: listings2[j],
		   address1: listings2[j+1],
		   address2: listings2[j+2],
		   postalCode:"95060"
    });
    adjustment += 0.02;
}
var listings = testArray;
//(36.9765546,-122.0323493,"Breakfast at?","The Abbey");
// Clears listings
function clear() {
    listings = [ ];
}
//Initializes map 
function initializeMap() {
    var mapOps = {
        center: new google.maps.LatLng(36.976349,-122.0292952),
        zoom: 8,
        mapTypeId: 'roadmap',
    };   
    map = new google.maps.Map(document.getElementById('map'), mapOps);
    infoWindow = new google.maps.InfoWindow();
    // Closes infoWin after a click on map
    google.maps.event.addListener(map, 'click', function() {
	    infoWindow.close();
        });
    displayMarkers();
}
//Initializes gooel api/maps. must be here!
google.maps.event.addDomListener(window, 'load', initializeMap);

//Displays the currently active study sessions, aka listings.
function displayMarkers(){
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0; i< listings.length; i++){
	var latlng = new google.maps.LatLng(listings[i].lat, listings[i].lng);
	var name = listings[i].name;
	var add1 = listings[i].address1;
	var add2 = listings[i].address2;
	var pCode = listings[i].postalCode;
	createMarker(latlng, name, add1, add2, pCode);
	bounds.extend(latlng);
    }
    map.fitBounds(bounds);
}
//Creates an individual marker object(inherts some properties of listing)
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

//All script calls go here.//
//if c ==0 is passed, clear listings!
//This is the normal running procedure, posts for all sessions.
//listings.push(args[0],args[1],args[2],args[3],"The Abbey","Santa Cruz");

/*
  lat: 37.000353,
  lng: -122.0631443,
  name: "study sesh3",
  address1: "Jack Baskin",
  address2: "UC Santa Cruz",
  postalCode:"95064"
*/
//if args[0] ==0, clear();
//}else{
    //}
}
