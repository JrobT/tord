import { Controller } from "stimulus"

export default class extends Controller {
    initialize() {
        var param = getUrlParam('page', 'Empty');
        $('.pagination li a').removeClass('active')
        $('#page-' + param).addClass('active')
    }

    page(event) {
        Turbolinks.visit('/blog/?page=' + event.target.id.replace('page-', ''))
    }
}

function getUrlVars() {
    var vars = {};
    window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

function getUrlParam(parameter, defaultvalue) {
    var urlparameter = defaultvalue;
    if (window.location.href.indexOf(parameter) > -1) {
        urlparameter = getUrlVars()[parameter];
    }
    return urlparameter;
}