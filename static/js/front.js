var wordCount = 0;

//dumb implementation to change the look of the button.
$(".leftselection").click(function( e ){
    if($(".leftselection").children().is("div.unselected")){
        $(".rightselection").children().toggleClass('selected').toggleClass('unselected')
        $(".leftselection").children().toggleClass('selected').toggleClass('unselected')
    }
});

$(".rightselection").click(function( e ){
    if($(".rightselection").children().is("div.unselected")){
        $(".rightselection").children().toggleClass('selected').toggleClass('unselected')
        $(".leftselection").children().toggleClass('selected').toggleClass('unselected')
    }
});


//dumb way implementation to change the class whenever submit button is pressed based on initial set up
$(".sendRequest").click(function( e ){
    //TODO: make ajax call to grab json format files
    if($(".leftselection").children().is("div.selected")){       //if left is selected
        $(".subscribedWrapper").css('display','block');
        $(".wordSearchWrapper").css('display','none');
        $(".addNewWord").css('display','block');
        $(".newSubWord").css('display','block');
    }else{
        $(".subscribedWrapper").css('display','none');
        $(".wordSearchWrapper").css('display','block');
    }
});

// $(".subscribedWrapper").click(function (e) {
//         console.log($(".addNewWord").val());

// })

$(".newSubWord").click(function(e){
    var word = $(".addNewWord").val();
    var email = $(".addNewEmail").val();
    console.log(email);
    $.post("/add_subscription/", {'email': email, 'word': word}, function(data) {
        console.log(data);
    });
    if($(".addNewWord").val() != ""){
        ++wordCount;
        $(".subscribed").append("<div class = 'wordList' id='id"+wordCount+"'>" + $(".addNewWord").val() + "</div><div class = 'deleteWord' id='"+wordCount+"'></div>");
    }
    $(".addNewWord").val("");
});


$(document).on('click','.deleteWord', function(e) {
    var subWordID = "id"+e.target.id;
    $("#"+subWordID).remove();
    $(e.target).remove();
});


function inputFocus(i){
    if(i.value==i.defaultValue){i.value="";i.style.color="#000";}
}
function inputBlur(i){
    if(i.value==""){i.value=i.defaultValue;i.style.colr="#444" }
}