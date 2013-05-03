$(document).ready(function() {
      $("#preferences").click(function(event){
          $('#content').load('/preferences/');
      });
      $("#listado").click(function(event){
          $('#content').load('/listado/');
      });
   });
