import { Controller } from "stimulus"

export default class extends Controller {
    static targets = ["text"]

    text() {
        var query = $(this.textTarget).val();
        $.ajax({
            url: "/",
            method: 'GET',
            data: {
                text: query
            }
        });
    }

    archive(event) {
        var query = $(event.target.id).val();
        $.ajax({
            url: "/",
            method: 'GET',
            data: {
                text: query
            }
        });
    }
}