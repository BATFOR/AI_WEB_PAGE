$(function(){
    //菜单点击
    $(".J_menuItem").on('click',function(event){
        event.preventDefault()
        var url = $(this).attr('href');
        $("#J_iframe").attr('src',url);
        return false;
    });
});