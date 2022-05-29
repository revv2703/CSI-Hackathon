$(function(){
    $('#button').click(function(){
        $(function(){
    $(function(){
        $('#h2').text('Input Received : ')
        setTimeout(() => {$('#h3').text('searching'+'.') }, 600);
        setTimeout(() => {$('#h3').text('NOT FOUND') }, 3500);
        $('#h3').text(' '+($('#input').val()))
        var x = $('#input').val()
        // console.log(x);
        // window.alert(x);
    })
    })
    })
})
function myFunction(){
    let input = {'input':x}
    //const input = document.getElementById("input");
    const s = JSON.stringify(input);
    console.log(s); // Prints the variables to console window, which are in the JSON format
    window.alert(s);
    $.ajax({
        url:"/index.html",
        type:"POST",
        contentType: "application/json",
        data: JSON.stringify(s)});
}
