
$(window).load(function() {
    if(sessionStorage.getItem("slide") === null)
    {
    sessionStorage.setItem("slide",1);
    sessionStorage.setItem("max_val",1);
    var a=sessionStorage.getItem("slide");
    var b=sessionStorage.getItem("max_val");
    console.log("else part slide value: ",a);
    console.log("else part max_val value: ",b);
    }
    else
    {
    var c = sessionStorage.getItem("slide");
    console.log("else part slide value: ",c);
    restore_status();
    }
    
    if(sessionStorage.getItem("product_list") === null)
    {
    var prod_list = {};
    var p_key = 0;
    }
    else
    {
    var prod_list = JSON.parse(sessionStorage.getItem("product_list"));
    var p_key = parseInt(sessionStorage.getItem("key_val"));
    }
    });
    
    function step2(box_id) {
         var sld=2;
         console.log("inside box selection process function, sld valie: ",sld);
         sessionStorage.setItem("box_id", box_id);
         sessionStorage.setItem("slide",sld);
         var max_val = parseInt(sessionStorage.getItem("max_val"));
         console.log("max value in step2 :", max_val);
         if (max_val < sld)
         {
            sessionStorage.setItem("max_val", sld);
         }
         var max_val = parseInt(sessionStorage.getItem("max_val"));
         var sld_val = parseInt(sessionStorage.getItem("slide"));
         console.log("slide value in step2: ",sld_val);
         console.log("max value in step2: ",max_val);
    
    
    
        var current = document.getElementById("step1");
        var new_step = document.getElementById("step2");
        current.className = "step0";
        new_step.className = "active step0";
    
        var cards = document.getElementsByClassName("card1");
        cards[0].className = "card1 b-0";
        cards[1].className = "card1 b-0 show";
    
        console.log("end of step2 func");
    }
    
    function step3(prod_title,prod_id,qty,img_url, price) {
    
        var p_list = {}
        if(sessionStorage.getItem("product_list") === null)
        {
            var prod_list = {};
            var p_key = 0;
        }
        else
        {
            var prod_list = JSON.parse(sessionStorage.getItem("product_list"));
            var p_key = parseInt(sessionStorage.getItem("key_val"));
        }
    
        p_list['title'] = prod_title;
        p_list['product_id'] = prod_id;
        p_list['quantity'] = qty;
        p_list['image_url'] = img_url;
        p_list['price'] = price;
    
        prod_list[p_key] = p_list;
        p_key = p_key + 1;
        sessionStorage.setItem("key_val", p_key);
    
        if (typeof (Storage) !== "undefined") {
            // Store
            sessionStorage.setItem("product_list", JSON.stringify(prod_list));
            console.log(JSON.stringify(prod_list));
            sessionStorage.setItem("slide", 2);
            sessionStorage.setItem("max_val", 2);
        }
        else {
            alert("Sorry, your browser does not support Session Storage...");
        }
    
    
        $('#closemodal').click(function () {
            $('#modalwindow').modal('hide');
        });
        $('.modal-backdrop').remove();
    
        
    }
    
    function instep(val, flag) {
    // flag =1, val = 1
        var max_val = parseInt(sessionStorage.getItem("max_val"));
        var slide = parseInt(sessionStorage.getItem("slide"));
        console.log("type of val: ", typeof (val), val);
        console.log("type of maxval: ", typeof (max_val), max_val);
        if (flag == 1 && val>max_val) {
            sessionStorage.setItem("max_val", val);
        }
        
        if (val <= max_val || flag == 1) {
            console.log("before restore status");
            sessionStorage.setItem("slide", val);
    
            restore_status();
        }
    
    }
    
    function send_data(data_list){
        console.log("inside send data", data_list)
        $.ajax({
            url: "/build-a-box/",
            data: {'cart_items':data_list },
            dataType: false,
            success: function (res) {
                console.log("successfully sent to view")
                $("#checkout_table").load(location.href + " #checkout_table");
            },
        });
    
    }
    
    
    function restore_status() {
    
        var mem = sessionStorage.getItem("slide");
        console.log("restore status slide value: ", mem);
        if (mem === null) {
            console.log("restore slide value is null");
        }
        else {
    
            console.log("restore slide mem: ", mem);
            var new_step = document.getElementById("step" + (parseInt(mem)));
            //current.className = "step0";
            console.log("restoring status");
    
    
    
            var cards = document.getElementsByClassName("card1");
            for (var k = 0; k < cards.length; k++) {
                $("#progressbar").children()[k].className = "step0";
                cards[k].className = "card1 b-0";
            }
    
            new_step.className = "active step0";
            cards[parseInt(mem-1)].className = "card1 b-0 show";
    
    
    
            if(sessionStorage.product_list)
            {
                var data = sessionStorage.product_list;
    
                var card_count = document.getElementsByClassName("card1").length;
                console.log("befor send data",card_count,(parseInt(mem)+1));
                if(card_count==(parseInt(mem)+1))
                {
                    console.log("calling send data");
                    send_data(data);
                }
            }
        }
    }
    
    
    function step4(box_id) {
        sessionStorage.setItem("max_val", 2);
        sessionStorage.setItem("slide", 3);
        var current = document.getElementById("step3");
        var new_step = document.getElementById("step4");
        current.className = "step0";
        console.log("insie step 4");
        new_step.className = "active step0";
        console.log("insie step 5");
    
        var cards = document.getElementsByClassName("card1");
        cards[2].className = "card1 b-0";
        cards[3].className = "card1 b-0 show";
    }
    

// console.log('inside custom js')
// // first validation
// function validate1(val) {
//     // flag1 = true
//     var box_Id = $(".box-id").val();
//     if (val >= 1 || val == 0) {
//         if (box_Id == "") {
//             flag1 = false;
//         }
//         else {
//             flag1 = true;
//         }
//     }
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
//     flag = flag1;
//     return flag1;
// }

// function validate2(val) {
//     // flag2 = true
//     var product_Id = $(".product-id").val();
//     if (val >= 1 || val == 0) {
//         if (product_Id == "") {
//             flag2 = false;
//         }
//         else {
//             flag2 = true;
//         }
    // }
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
//     flag = flag2
//     return flag;
// }

// function validate3(val) {
//     var card_Id = $(".card-id").val();
//     if (val >= 1 || val == 0) {
//         if (card_Id == "") {
//             flag3 = false;
//         }
//         else {
//             flag3 = true;
//         }
//     }
//     flag =flag3;
//     return flag;
// }

// $(document).on('click', ".next", function () {
//     str1 = "next1";
//     str2 = "next2";
//     str3 = "next3";
//     console.log('next clicked')
//     if (!str1.localeCompare($(this).attr('id')) && validate1(0) == true) {
//         val1 = true;
//     }
//     else {
//         val1 = false;
//     }

//     if (!str2.localeCompare($(this).attr('id')) && validate2(0) == true) {
//         val2 = true;
//     }
//     else {
//         val2 = false;
//     }

//     if (!str3.localeCompare($(this).attr('id')) && validate3(0) == true) {
//         val3 = true;
//     }
//     else {
//         val3 = false;
//     }

//     if ((!str1.localeCompare($(this).attr('id')) && val1 == true) || (!str2.localeCompare($(this).attr('id')) && val2 == true) || (!str3.localeCompare($(this).attr('id')) && val3 == true)) {
//         current_fs = $(this).parent().parent().parent();
//         next_fs = $(this).parent().parent().parent().next();

//         $(current_fs).removeClass("show");
//         console.log(current_fs)
//         console.log(next_fs)
//         $(next_fs).addClass("show");

//         $("#progressbar li").eq($(".card1").index(next_fs)).addClass("active");

//         current_fs.animate({}, {
//             step: function () {

//                 current_fs.css({
//                     'display': 'none',
//                     'position': 'relative'
//                 });

//                 next_fs.css({
//                     'display': 'block'
//                 });
//             }
//         });
//     }
// });




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