import { Controller } from "stimulus"

export default class extends Controller {
    expand(event) {
        var target = $(event.target);
        var item = target.parent();
        var input = item.find(".filter-input");
        var icon = target.find(".filter-icon");
        if (!target.hasClass("open") &&
            !item.hasClass("open") &&
            !input.hasClass("open") &&
            !icon.hasClass("rotate")) {
            target.addClass("open");
            target.removeClass("bounce");
            item.addClass("open");
            input.addClass("open");
            icon.addClass("rotate");
            input.prop("disabled", false);
        } else {
            target.removeClass("open");
            target.addClass("bounce");
            item.removeClass("open");
            input.removeClass("open");
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