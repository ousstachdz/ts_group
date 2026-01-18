/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState } from "owl";

export class ReviewsTable extends Component {
    setup() {
        this.docs = useState({});
        this.collapse = false;
        this.orm = useService("orm");
        this.reviews = [];
    }

    _getReviewData() {
        const records = this.env.model.root.data.review_ids.records;
        const reviews = [];
        for (let i = 0; i < records.length; i++) {
            reviews.push(records[i].data);
        }
        return reviews;
    }

    onToggleCollapse(ev) {
        const $panelHeading = $(ev.currentTarget).closest(".panel-heading");
        if (this.collapse) {
            $panelHeading.next("div#collapse1").hide();
        } else {
            $panelHeading.next("div#collapse1").show();
        }
        this.collapse = !this.collapse;
    }
}

// ATTENTION : clé simple + component
registry.category("fields").add("tier_validation", {
    component: ReviewsTable,
});
