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

$(".sendRequest").click(function( e ){
    if($(".rightselection").children().is("div.selected")){
        $(".subscribedWrapper").toggleClass('subscribedWrapper').toggleClass('wordSearchWrapper')
 $(".wordSearchWrapper").children().toggleClass('subscribed').toggleClass('wordSearch').toggleClass('subscribe').toggleClass('wordS')
    }else{
        if($(".bodyWrapper").children().is("div.wordSearchWrapper")){
            $(".wordSearchWrapper").toggleClass('subscribedWrapper').toggleClass('wordSearchWrapper')
            $(".subscribedWrapper").children().toggleClass('subscribed').toggleClass('wordSearch').toggleClass('subscribe').toggleClass('wordS')
            
        }
    }
});