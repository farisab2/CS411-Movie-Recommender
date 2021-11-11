$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#edit-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const movieID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        modal.find('.modal-title').text('Edit Movie Score ' + movieID)
        $('#score-form-display').attr('movieID', movieID)


        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })

    $('#submit-change').click(function () {
        const movieID = $('#score-form-display').attr('movieID');

        console.log($('#edit-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url:'/edit',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'score': $('#edit-modal').find('.form-control').val(),
                'movieID': movieID
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'movieID': remove.data('source'),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});