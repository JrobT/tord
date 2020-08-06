import { Controller } from "stimulus"

export default class extends Controller {
    initialize() {
        var param = getUrlParam("page", "Empty");
        if (param == "Empty") {
            param = 1
            document.location.search = "?page=" + param + "&" + document.location.search.substr(1);
        }
        $('.pagination li a').removeClass('active')
        $('#page-' + param).addClass('active')
    }

    page(event) {
        var params = document.location.search.replace("?page=", "").substr(1);
        Turbolinks.visit('/blog/?page=' + event.target.id.replace('page-', '') + params)
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