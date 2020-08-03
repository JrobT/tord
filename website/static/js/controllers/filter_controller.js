import { Controller } from "stimulus"

export default class extends Controller {
    menu(event) {
        var target = $(".sidebar");
        var content = $(".post-content");
        if (!target.hasClass("filter-open")) {
            target.addClass("filter-open");
            content.addClass("filter-open");
            $("#filter-open").style.display = "none";
        } else {
            target.removeClass("ilter-open");
            content.removeClass("filter-open");
        }
    }

    expand(event) {
        var target = $(event.target);
        var input = target.parent().find(".filter-input");
        var icon = target.find(".filter-icon");
        if (!target.hasClass("open") &&
            !input.hasClass("open") &&
            !icon.hasClass("rotate")) {
            target.addClass("open");
            input.addClass("open");
            icon.addClass("rotate");
            input.prop("disabled", false);
        } else {
            target.removeClass("open");
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