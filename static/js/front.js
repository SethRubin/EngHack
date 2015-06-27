
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

$(".newSubWord").click(function(e){
    $(".wordList").append($(".addNewWord").val()+"<br>");
    
    $(".addNewWord").val("");
});