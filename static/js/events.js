    function selectCategory(value) {

        var categorySelected = value;
        categorySelected = "." + categorySelected;
        $(".event").hide();
        $(categorySelected).show();

    }