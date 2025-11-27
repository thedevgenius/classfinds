
$(document).ready(function () {
    document.getElementById("year").textContent = new Date().getFullYear();

    $(".modal-btn").click(function () {
        var modalType = $(this).data("modal-id");
        $("#" + modalType).removeClass("hidden");
    });

    $(".close-btn").click(function () {
        $(this).closest(".modal").addClass("hidden");
    });

    const modal = document.querySelector('.modal');
    const modalBox = document.querySelector('.modal-content');

    modal.addEventListener('click', (e) => {
        if (!modalBox.contains(e.target)) {
            modal.classList.add('hidden');  // hide modal
        }
    });

    $(".loc-btn").click(function () {
        $("#locsearch").focus();
    });

    //Location Select2 Dropdown
    $('.locselect').select2({
        placeholder: "Select Location...",
        // minimumInputLength: 1,
        // allowClear: true
        selectionCssClass: 'loc-select'

    });

    const savedValue = localStorage.getItem('selectedLocation');
    if (savedValue) {
        $('.locselect').val(JSON.parse(savedValue).id);
        $('.locselect').trigger('change');
        $('.locName').text(JSON.parse(savedValue).name);
    }

    $('.locselect').on('change', function () {
        const selectedValue = $(this).val();
        
        $.ajax({
            type: "GET",
            url: "/select-location/",
            data: {
                'location_id': selectedValue
            },
            dataType: "json",
            success: function (response) {
                const locationData = {
                    id: selectedValue,
                    name: response.name,
                };
                localStorage.setItem("selectedLocation", JSON.stringify(locationData));
                if (JSON.parse(savedValue).id != selectedValue) {
                    window.location.reload();
                }
            }
        });
    });

    

    //Search Modal
    $(".search-btn").click(function () {
        $("#search_input").focus();
    });
}); 