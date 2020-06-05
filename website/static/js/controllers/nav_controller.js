import { Controller } from "stimulus"

export default class extends Controller {
    static targets = ["home", "about"]

    initialize() {
        var url = window.location.pathname
        if (url == "/") {
            this.homeTarget.classList.add("active")
            this.aboutTarget.classList.remove("active")
        } else if (url == "/about") {
            this.homeTarget.classList.remove("active")
            this.aboutTarget.classList.add("active")
        } else {
            this.homeTarget.classList.remove("active")
            this.aboutTarget.classList.remove("active")
        }
    }

    home() {
        Turbolinks.visit("/")
    }

    about() {
        Turbolinks.visit("/about")
    }
}