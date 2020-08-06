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
}