import { Controller } from "stimulus"

export default class extends Controller {
    expand(event) {
        var target = $(event.target);
        var input = target.parent().find(".filter-input");
        var icon = target.find(".filter-icon");
        if (input.hasClass("close")) {
            input.removeClass("close");
            input.addClass("open");
            icon.addClass("rotate");
            input.prop("disabled", false);
        } else {
            input.removeClass("open");
            input.addClass("close");
            icon.removeClass("rotate");
            input.prop("disabled", true);
        }
    }

    tag(event) {
        var target = $(event.target);
        var chk = target.next();
        if (chk.is(":disabled")) {
            chk.prop("disabled", false);
            target.addClass("toggled");
        } else {
            chk.prop("disabled", true);
            target.removeClass("toggled");
        }
    }
}