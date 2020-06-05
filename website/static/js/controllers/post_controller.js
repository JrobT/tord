import { Controller } from "stimulus"

export default class extends Controller {
    detail(event) {
        Turbolinks.visit(event.target.id)
    }

    edit() {
        Turbolinks.visit("/update/" + event.target.id)
    }
}