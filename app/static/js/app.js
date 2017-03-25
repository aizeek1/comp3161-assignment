/* global $ */
$(document).ready(function(){
    //handle sidebar clicks
    $('ul#sidenav li a').click(function(){
        var page = $(this).attr('href');
        //alert(page);
        $('#sidecontent').load(page);
        return false;
    });
});