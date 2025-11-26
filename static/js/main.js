
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
        minimumInputLength: 1,
        // allowClear: true
        selectionCssClass: 'loc-select'

    });

    $('.locselect').on('change', function () {
        const selectedValue = $(this).val();
        localStorage.setItem('selectedLocation', selectedValue);
    });

    const savedValue = localStorage.getItem('selectedLocation');
    if (savedValue) {
        $('.locselect').val(savedValue).trigger('change');
    }

    //Search Modal
    $(".search-btn").click(function () {
        $("#search_input").focus();
    });
}); 