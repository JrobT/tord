import { Controller } from "stimulus"

export default class extends Controller {
    detail(event) {
        var target = $(event.target);
        while (!target.is("section")) {
            target = target.parent()
        }
        Turbolinks.visit("/blog/" + target.attr("id"))
    }

    edit(event) {
        Turbolinks.visit("/blog/update/" + event.target.id)
    }

    expand(event) {
        var target = $(event.target);
        var replies = target.parent().find(".replies");
        if (!target.hasClass("open")) {
            target.addClass("open");
            replies.addClass("open");
        } else {
            target.removeClass("open");
            replies.removeClass("open");
        }
    }
}