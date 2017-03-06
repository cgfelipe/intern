$(document).ready(function() {
    $('input').addClass('form-control');
    $('select').addClass('form-control');
    $('textarea').addClass('form-control');
    $('body').scrollspy({ target: '#navbar-menu' });
    $('.errorlist li').addClass('alert alert-danger');
});