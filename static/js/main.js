
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
}); 