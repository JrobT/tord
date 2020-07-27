import { Controller } from "stimulus"

export default class extends Controller {
    blog() {
        Turbolinks.visit("/blog")
    }

    projects() {
        Turbolinks.visit("/blog")
    }
}