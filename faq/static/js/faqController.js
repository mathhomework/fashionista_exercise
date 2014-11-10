(function(){
    var faqController = function($scope){
        $scope.paid_info = false;
        $scope.schedule_info = false;
        $scope.qualifications_info = false;
        $scope.p_sign = "+";
        $scope.s_sign = "+";
        $scope.q_sign = "+";
        var check_signs = function(){
            $scope.p_sign = $scope.paid_info? "-": "+";
            $scope.s_sign = $scope.schedule_info? "-": "+";
            $scope.q_sign = $scope.qualifications_info? "-": "+";
        };
        $scope.paid = function(){
            $scope.paid_info = !$scope.paid_info;
            $scope.schedule_info = false;
            $scope.qualifications_info = false;
            check_signs();
        };
        $scope.schedule = function(){
            $scope.schedule_info = !$scope.schedule_info;
            $scope.paid_info = false;
            $scope.qualifications_info = false;
            check_signs();
        };

        $scope.qualifications = function(){
            console.log("YAAYA");
            $scope.qualifications_info = !$scope.qualifications_info;
            $scope.paid_info = false;
            $scope.schedule_info = false;
            check_signs();


        };
    };
    faqController.$inject = ['$scope'];
    angular.module('faqApp').controller('faqController', faqController);
}());