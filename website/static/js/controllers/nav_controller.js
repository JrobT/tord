import { Controller } from "stimulus"

export default class extends Controller {
    menu() {
        var target = $(".sidebar");
        if (!target.hasClass("filter-open")) {
            target.addClass("filter-open");
            $("#filter-open").css("display", "none");
        } else {
            target.removeClass("filter-open");
            $("#filter-open").css("display", "inline-block");
        }
    }

    blog() {
        Turbolinks.visit("/blog/?page=1")
    }

    projects() {
        Turbolinks.visit("/blog/?page=1")
    }
}