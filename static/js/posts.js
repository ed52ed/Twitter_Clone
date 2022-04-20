//

//

$(function() {
    // Excuted when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : next to div.js-menu-icon. namely div.menu
       // toggle() : swithc show and hide
        $(this).next().toggle();
    })
})