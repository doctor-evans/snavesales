

$(document).on('submit', '#contact-form-ajax', function (e) {
    e.preventDefault()
    let full_name = $("#full_name").val()
    let email = $("#email").val()
    let mobile = $("#mobile").val()
    let subject = $("#subject").val()
    let message = $("#message").val()

    $.ajax({
        url: "/user/ajax-contact",
        data: {
            'full_name': full_name,
            'email': email,
            'mobile': mobile,
            'subject': subject,
            'message': message
        },
        dataType: 'json',
        beforeSend: function () {
            console.log("Sending to server")
        },
        success: function () {
            console.log('back from server')
            $("#contact-form-ajax").html('<h5>Message sent successfully.</h5>')
        }
    })
})


$(document).on('submit', '.account-detail-update', function (e) {
    e.preventDefault()
    let user_id = $(this).attr("data-userid")
    let first_name = $("#user_firstname").val()
    let last_name = $("#user_lastname").val()
    let email = $("#user_email").val()
    let username = $("#user_username").val()

    console.log("this user has an id of: ", user_id)

    $.ajax({
        url: "/user/account-update",
        data: {
            'first_name': first_name,
            'email': email,
            'last_name': last_name,
            'username': username,
            'user_id': user_id
        },
        dataType: 'json',
        beforeSend: function () {
            console.log("Sending to server")
        },
        success: function (response) {
            alert('Account Updated Successfully');
            $("#account-update").html(response.data)

        }
    })
})

$(document).on('click', '.contact-vendor', function () {
    let contact = $(this).attr("data-contact")
    let url = $("#url").attr("data-url")

    let uri = `https://wa.me/${contact}?text=${url}`
    const encoded = encodeURI(uri)
    window.open(encoded, '_blank')
})