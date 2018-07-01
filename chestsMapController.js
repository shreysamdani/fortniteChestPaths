var Chests = angular.module('Chests', ['ngMaterial'])
.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default').dark();
});

Chests.controller('ChestCtrl', function($scope, $http) {



// initialize map
	var bounds = [[0,0], [850,850]];
	var options = {
		crs: L.CRS.Simple,
		maxZoom : 4,
		maxBounds : bounds
	}
	var map = L.map('chestMap',	options);
	var image = L.imageOverlay("images/StadiumMap.png", bounds).addTo(map);
	map.addControl(new L.Control.Fullscreen());
	map.fitBounds(bounds);

	$scope.numChests = 5;


	var currPath = [];
	var latlngs = [];
	var line = L.polyline(latlngs, {color: 'yellow'}).addTo(map);
	var currChests = new Array(2)
	var markers;

	$http.get("http://127.0.0.1:5000/locations").then(
		function(response) {
			markers = new Array(response.data.length)
			for (var i = 0; i < response.data.length; i++) {
				initializeMarker(response.data[i], i);
			}

		});

	var initializeMarker = function(location, index) {
		location = [location[1] / 2048 * 850, location[0] / 2048 * 850];
		var loc = L.icon({
					iconUrl: 'images/Chest.png',
					iconSize: [25,25]
				});

		markers[index] = L.marker(location, {icon: loc});
		markers[index].addTo(map);
		markers[index].on('mouseover', function(e) {
					this._icon.style.filter = 'drop-shadow(2px 2px 0 yellow) drop-shadow(-2px -2px 0 yellow)';
				});

		markers[index].on('mouseout', function(e) {
					if (this != markers[currChests[1]] && this != markers[currChests[0]]) {
						for (var i = 0; i < currPath.length; i++) {
							if (this == markers[currPath[i]])
								return;
						}
						this._icon.style.filter = '';
					}
				});
		markers[index].on('click', function(e) {

					if (currChests[0]) {
						currChests = new Array(2);
						clearPath()
					}	
					currChests[0] = currChests[1];
					currChests[1] = index;
					this._icon.style.filter = 'drop-shadow(2px 2px 0 yellow) drop-shadow(-2px -2px 0 yellow);'

					if (currChests[0]) {
						findPath(currChests);
					}
				});

	}
	

	$scope.selected = function(index) {
		return chests.includes(index);
	}


	var clearPath = function() {
		for (var i = 0; i < currPath.length; i++) {
			markers[currPath[i]]._icon.style.filter = '';
		}
		currPath = [];
		latlngs = [];
		line.setLatLngs(latlngs);

	}

    var findPath = function(chests) {
    	clearPath()
    	$http.get("http://127.0.0.1:5000/distance", {params: {'endpoints': chests, 'numChests': $scope.numChests}}).then(
		function(response) {
			currPath = response.data;
			for (var i = 0; i < currPath.length; i++) {
				markers[currPath[i]]._icon.style.filter = 'drop-shadow(2px 2px 0 yellow) drop-shadow(-2px -2px 0 yellow)';
				latlngs.push(markers[currPath[i]]._latlng);
			}
			line.setLatLngs(latlngs);
		});
    }


})