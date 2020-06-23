import { Controller } from "stimulus"

export default class extends Controller {
    initialize() {
        var url = window.location.search
        $('div.pagination>ul>.pagination__bubble').removeClass('active')
        $('#' + url.replace('?page=', '')).addClass('active')
    }

    bubble(event) {
        Turbolinks.visit('/?page=' + event.target.id)
    }

    first() {
        Turbolinks.visit('/?page=1')
    }
}