console.log('inside custom js')
// first validation
function validate1(val) {
    // flag1 = true
    var box_Id = $(".box-id").val();
    if (val >= 1 || val == 0) {
        if (box_Id == "") {
            flag1 = false;
        }
        else {
            flag1 = true;
        }
    }
    // v1 = document.getElementsByName("add-box");
    // console.log(v1);
    // // v2 = document.getElementById("email");
    // flag1 = true;
    // flag2 = true;
    // if (val >= 1 || val == 0) {
    //     if (v1.value == "") {
    //         v1.style.borderColor = "red";
    //         flag1 = false;
    //     }
    //     else {
    //         v1.style.borderColor = "white";
    //         flag1 = true;
    //     }
    // }
    // if (val >= 2 || val == 0) {
    //     if (v2.value == "") {
    //         v2.style.borderColor = "red";
    //         flag2 = false;
    //     }
    //     else {
    //         v2.style.borderColor = "white";
    //         flag2 = true;
    //     }
    // }
    // flag = flag1 && flag2;
    flag = flag1;
    return flag1;
}

function validate2(val) {
    // flag2 = true
    var product_Id = $(".product-id").val();
    if (val >= 1 || val == 0) {
        if (product_Id == "") {
            flag2 = false;
        }
        else {
            flag2 = true;
        }
    }
    // v1 = document.getElementById("web-title");
    // v2 = document.getElementById("desc");

    // flag1 = true;
    // flag2 = true;

    // if (val >= 1 || val == 0) {
    //     if (v1.value == "") {
    //         v1.style.borderColor = "red";
    //         flag1 = false;
    //     }
    //     else {
    //         v1.style.borderColor = "white";
    //         flag1 = true;
    //     }
    // }

    // if (val >= 2 || val == 0) {
    //     if (v2.value == "") {
    //         v2.style.borderColor = "red";
    //         flag2 = false;
    //     }
    //     else {
    //         v2.style.borderColor = "white";
    //         flag2 = true;
    //     }
    // }

    // flag = flag1 && flag2;
    flag = flag2
    return flag;
}

function validate3(val) {
    var card_Id = $(".card-id").val();
    if (val >= 1 || val == 0) {
        if (card_Id == "") {
            flag3 = false;
        }
        else {
            flag3 = true;
        }
    }
    flag =flag3;
    return flag;
}

$(document).on('click', ".next", function () {
    str1 = "next1";
    str2 = "next2";
    str3 = "next3";
    console.log('next clicked')
    if (!str1.localeCompare($(this).attr('id')) && validate1(0) == true) {
        val1 = true;
    }
    else {
        val1 = false;
    }

    if (!str2.localeCompare($(this).attr('id')) && validate2(0) == true) {
        val2 = true;
    }
    else {
        val2 = false;
    }

    if (!str3.localeCompare($(this).attr('id')) && validate3(0) == true) {
        val3 = true;
    }
    else {
        val3 = false;
    }

    if ((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val2 == true) || (!str3.localeCompare($(this).attr('id')) && val3 == true)) {
        current_fs = $(this).parent().parent().parent();
        next_fs = $(this).parent().parent().parent().next();

        $(current_fs).removeClass("show");
        console.log(current_fs)
        console.log(next_fs)
        $(next_fs).addClass("show");

        $("#progressbar li").eq($(".card1").index(next_fs)).addClass("active");

        current_fs.animate({}, {
            step: function () {

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });

                next_fs.css({
                    'display': 'block'
                });
            }
        });
    }
});




// $(document).ready(function () {

//     var current_fs, next_fs, previous_fs;

//     $(".next").click(function () {
//         console.log($(this).attr('id'))
//         str1 = "next1";
//         str2 = "next2";
//         str3 = "next3";

//         if (!str1.localeCompare($(this).attr('id')) && validate1(0) == true) {
//             val1 = true;
//         }
//         else {
//             val1 = false;
//         }

//         if (!str2.localeCompare($(this).attr('id')) && validate2(0) == true) {
//             val2 = true;
//         }
//         else {
//             val2 = false;
//         }

//         if (!str3.localeCompare($(this).attr('id')) && validate3(0) == true) {
//             val3 = true;
//         }
//         else {
//             val3 = false;
//         }

//         if ((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val2 == true) || (!str3.localeCompare($(this).attr('id')) && val3 == true)) {
//             current_fs = $(this).parent().parent().parent();
//             next_fs = $(this).parent().parent().parent().next();

//             $(current_fs).removeClass("show");
//             console.log(current_fs)
//             console.log(next_fs)
//             $(next_fs).addClass("show");

//             $("#progressbar li").eq($(".card1").index(next_fs)).addClass("active");

//             current_fs.animate({}, {
//                 step: function () {

//                     current_fs.css({
//                         'display': 'none',
//                         'position': 'relative'
//                     });

//                     next_fs.css({
//                         'display': 'block'
//                     });
//                 }
//             });
//         }
//     });

//     $(".prev").click(function () {

//         current_fs = $(this).parent();
//         previous_fs = $(this).parent().prev();

//         $(current_fs).removeClass("show");
//         $(previous_fs).addClass("show");

//         $("#progressbar li").eq($(".card1").index(next_fs)).removeClass("active");

//         current_fs.animate({}, {
//             step: function () {

//                 current_fs.css({
//                     'display': 'none',
//                     'position': 'relative'
//                 });

//                 previous_fs.css({
//                     'display': 'block'
//                 });
//             }
//         });
//     });

// });