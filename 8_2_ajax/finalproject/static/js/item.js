var $form = '';
var base_modal_html = '';

$(function() {
  init();
});

function init(){
    $form = $('#item_form');
    base_modal_html = $('#itemt_modal').html();
}

function clear_errors() {
    $form.find('li.error').remove()
}

function clear_form() {
    console.log('clear form');
    clear_errors();
    $('input', $form).val('')
}

function show_errors(errors) {
    for (var error_name in errors) {
        for (var error in errors[error_name]){
            $('[name=' + error_name + ']', $form).closest('td').prepend('<li class="error">'+ errors[error_name][error].message + '</li>');
        }
        $('[name=' + error_name + ']', $form).parent().addClass('error');
    }

}

function update_page(new_html) {
    // console.log('new_html -->', new_html);
    $('#items_list').html(new_html)
}

function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}

function get_item_info(item_id){
    $.ajax({
        url: '/admin/get_item_info/' + item_id,
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", errors);
            } else {
                console.log("получен ответ", response);
                $('#item_form').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}



function send_new_item() {
    var id = $('#id').html();
    console.log('item_id = ', id);
    var prefix =  (id != undefined) ? id : '';
    var user_data = getFormData($form);
    $("#item_form").ajaxSubmit({url: '/admin/create/item/' + prefix, type: 'post',
    success: function (response) {
            console.log("response = ", response);
            if (response.errors) {
                var errors = JSON.parse(response.errors);
                //console.log("errors = ", errors);
                clear_errors();
                show_errors(errors);
            } else {
                clear_form();
                console.log("Очищаю форму");
                update_page(response.html);
                console.log("Обновляю страницу");
                clear_form();
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
});
}





/*
    var id = $('#id').html();
    console.log('item_id = ', id);
    var prefix =  (id != undefined) ? id : '';
    var user_data = getFormData($form);
    console.log('user_data = ', user_data);
    $.ajax({
        url: '/admin/create/item/' + prefix,
        type: 'POST',
        data: user_data,
        dataType: 'json',
        success: function (response) {
            console.log("response = ", response);
            if (response.errors) {
                var errors = JSON.parse(response.errors);
                //console.log("errors = ", errors);
                clear_errors();
                show_errors(errors);
            } else {
                clear_form();
                console.log("Очищаю форму");
                update_page(response.html);
                console.log("Обновляю страницу");
                clear_form();
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}
// function recover_base_form(){
//     $('#user_modal').html(base_modal_html);
//     $form = $('#user_form');
// }
*/
