$(document).ready(function()
{
    $('#main_pic1').toggle();
    $('#main_pic2').toggle();
    $('#main_pic3').toggle();
    $('#main_pic4').toggle();

    $('#pic1').click(function()
    {
        $('#main_pic').hide()
        $('#main_pic2').hide()
        $('#main_pic3').hide()
        $('#main_pic4').hide()
        $('#main_pic1').toggle();
    }
    )
    $('#pic2').click(function()
    {
        $('#main_pic').hide()
        $('#main_pic1').hide()
        $('#main_pic3').hide()
        $('#main_pic4').hide()
        $('#main_pic2').toggle();
    }
    )
    $('#pic3').click(function()
    {
        $('#main_pic').hide()
        $('#main_pic1').hide()
        $('#main_pic2').hide()
        $('#main_pic4').hide()
        $('#main_pic3').toggle();
    }
    )
    $('#pic4').click(function()
    {
        $('#main_pic').hide()
        $('#main_pic1').hide()
        $('#main_pic2').hide()
        $('#main_pic3').hide()
        $('#main_pic4').toggle();
    }
    )
})