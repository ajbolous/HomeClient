var app = angular.module('myApp', ['ui.bootstrap','ngAnimate','toggle-switch']);

        app.controller('myCtrl', function($scope,$http,$timeout) {
            $scope.pins= {
            }

            $scope.alerts= [
            ]

             $scope.addAlert = function(msgdata) {
                $scope.alerts.push({type:'success', msg: msgdata});
              };

              $scope.closeAlert = function(index) {
                $scope.alerts.splice(index, 1);
              };

          $scope.$watchCollection('pins', function (newval,oldval) {
            angular.forEach($scope.pins, function (value, key) {
              if (oldval[key] != newval[key]) {
                $scope.changeLamp(key,newval[key])
              }
            });
          });

          $scope.getPins = function(){
                $http.get("/lamps").then(function(response) {
                    response.data.forEach(function(pin){
                        $scope.pins[('p' + pin.pin)] = (pin.val == 0 ? true:false);
                    });

                 });

          }

            $scope.changeLamp = function(pin,val){
            p = pin.replace('p','');
            val = (val == true? 0:1);
                         $http.get("/invoke?pin=" + p+ "&val=" + val)
                          .then(function(response) {
                          $scope.addAlert(response.data);
                           $timeout(function() {
                            $scope.closeAlert(0)
                        }, 2000);
                        });
            }

            $scope.getPins();

        });