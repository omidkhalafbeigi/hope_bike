$(document).ready(function(){
    $('#profile').mouseenter(function(){
        $(this).css('background-color' , "rgb(255, 154, 216)");
    })
    $('#edit').mouseleave(function(){
        $(this).css('background-color' , "rgb(113, 202, 231)");
    })

    $('#edit').mouseenter(function(){
        $(this).css('background-color' , "rgb(255, 154, 216)");
    })
    $('#profile').mouseleave(function(){
        $(this).css('background-color' , "rgb(113, 202, 231)");
    })

    $('#favorit').mouseenter(function(){
        $(this).css('background-color' , "rgb(255, 154, 216)");
    })
    $('#favorit').mouseleave(function(){
        $(this).css('background-color' , "rgb(113, 202, 231)");
    })

    $('#orderhistory').mouseenter(function(){
        $(this).css('background-color' , "rgb(255, 154, 216)");
    })
    $('#orderhistory').mouseleave(function(){
        $(this).css('background-color' , "rgb(113, 202, 231)");
    })
    /*-------*/
    $('#profinfo'  ).toggle();
    $('#editinfo').toggle();
    $('#faveinfo').toggle();
    $('#orderinfo').toggle();
    /*-------*/
    $('#profile').click(function(){
        $('#profinfo').toggle(200);
    })
    $('#edit').click(function(){
        $('#editinfo').toggle(200);
    })
    $('#favorit').click(function(){
        $('#faveinfo').toggle(200);
    })
    $('#orderhistory').click(function(){
        $('#orderinfo').toggle(200);
    })
})