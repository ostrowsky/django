'use strict';
let items = document.getElementsByClassName('item');
$('#isJobsChecked').click(function() {
    if (document.getElementById('isJobsChecked').checked) {
        for (let i = 3; i < items.length; i++) {
            $(`.item:eq(${i})`).hide();
        }
    } else {
        for (let i = 3; i < items.length; i++) {
            $(`.item:eq(${i})`).show();
        }
    }
});
