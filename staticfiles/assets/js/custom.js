
$(window).load(function () {
    if (sessionStorage.getItem("slide") === null) {
        sessionStorage.setItem("slide", 1);
        sessionStorage.setItem("max_val", 1);
        var a = sessionStorage.getItem("slide");
        var b = sessionStorage.getItem("max_val");
        console.log("else part slide value: ", a);
        console.log("else part max_val value: ", b);
    }
    else {
        var c = sessionStorage.getItem("slide");
        console.log("else part slide value: ", c);
        restore_status();
    }

    // calculate_total();
});

function calculate_total() {
    console.log("inside total calulate")
    $.ajax({
        url: "/calculate_total/",
        data: { 'calculate': 'dummy' },
        dataType: false,
        success: function (res) {
            console.log("successfully called calculate");
            // $("#checkout_table").load(location.href + " #checkout_table");
        },
    });

}

function step2(box_id) {
    var sld = 2;
    console.log("inside box selection process function, sld valie: ", sld);

    //  saving box /////////////////////////////////////////////////////////////////////////////
    sessionStorage.setItem("box_id", box_id);

    var box_type = {}
    if (sessionStorage.getItem("box_list") === null) {
        var box_list = {};
    }
    else {
        var box_list = JSON.parse(sessionStorage.getItem("box_list"));
    }

    // saving products 
    box_type['box_id'] = box_id;

    box_list = box_type;

    if (typeof (Storage) !== "undefined") {
        // Store
        sessionStorage.setItem("box_list", JSON.stringify(box_type));
        console.log(JSON.stringify(box_list),'/////////////////////////////////////////////');

    }
    else {
        alert("Sorry, your browser does not support Session Storage...");
    }

    sessionStorage.setItem("slide", sld);
    var max_val = parseInt(sessionStorage.getItem("max_val"));
    console.log("max value in step2 :", max_val);
    if (max_val < sld) {
        sessionStorage.setItem("max_val", sld);
    }
    var max_val = parseInt(sessionStorage.getItem("max_val"));
    var sld_val = parseInt(sessionStorage.getItem("slide"));
    console.log("slide value in step2: ", sld_val);
    console.log("max value in step2: ", max_val);



    var current = document.getElementById("step1");
    var new_step = document.getElementById("step2");
    current.className = "step0";
    new_step.className = "active step0";

    var cards = document.getElementsByClassName("card1");
    cards[0].className = "card1 b-0";
    cards[1].className = "card1 b-0 show";

    console.log("end of step2 func");
}



function step3(prod_title, prod_id, qty, img_url, price) {

    // saving products /////////////////////////////////////////////////////////////////////////////////////
    var p_list = {}
    if (sessionStorage.getItem("product_list") === null) {
        var prod_list = {};
        var p_key = 0;
    }
    else {
        var prod_list = JSON.parse(sessionStorage.getItem("product_list"));
        var p_key = parseInt(sessionStorage.getItem("key_val"));
    }
    // saving products 
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
        console.log('prod_list:', JSON.stringify(prod_list));
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



function step4(card_id) {
    // sessionStorage.setItem("max_val", 2);
    // sessionStorage.setItem("slide", 3);
    // //  saving card /////////////////////////////////////////////////////////////////////////////
    // sessionStorage.setItem("card_id", card_id);


    var card_type = {}
    if (sessionStorage.getItem("card_list") === null) {
        var card_list = {};
    }
    else {
        var card_list = JSON.parse(sessionStorage.getItem("card_list"));
    }
    
    var sender = document.getElementById("sender-"+card_id).value;
    var receip = document.getElementById("recipient-"+card_id).value;
    var card_frnt = document.getElementById("card-front-"+card_id).value;
    var card_bck = document.getElementById("card-back-"+card_id).value;
    
   console.log("valkueee: ",sender);
    card_list['card_id'] = card_id;
    card_list['sender'] = sender;
    card_list['recipient'] = receip;
    card_list['card_front'] = card_frnt;
    card_list['card_back'] = card_bck;

     
    sessionStorage.setItem("card_list",JSON.stringify(card_list));

   

    if (typeof (Storage) !== "undefined") {
        // Store
        
        console.log(JSON.stringify(card_list),'/////////////////////////////////////////////');

    }
    else {
        alert("Sorry, your browser does not support Session Storage...");
    }



    // var current = document.getElementById("step3");
    // var new_step = document.getElementById("step4");
    // current.className = "step0";
    // console.log("insie step 4");
    // new_step.className = "active step0";
    // console.log("insie step 5");

    // var cards = document.getElementsByClassName("card1");
    // cards[2].className = "card1 b-0";
    // cards[3].className = "card1 b-0 show";

    
   
    $('.modal-backdrop').remove();
    instep(4,1);
}




function instep(val, flag) {
    // flag =1, val = 1
    var max_val = parseInt(sessionStorage.getItem("max_val"));
    var slide = parseInt(sessionStorage.getItem("slide"));
    console.log("type of val: ", typeof (val), val);
    console.log("type of maxval: ", typeof (max_val), max_val);
    if (flag == 1 && val > max_val) {
        sessionStorage.setItem("max_val", val);
    }

    if (val <= max_val || flag == 1) {
        console.log("before restore status");
        sessionStorage.setItem("slide", val);

        restore_status();
    }

}
function load_cart(){
    $("#cart_page").load(location.href + " #cart_page");
}

function send_data(data_list) {
    console.log("inside send data", data_list)
    $.ajax({
        url: "/product/build-a-box/",
        data: { 'cart_items': data_list },
        dataType: false,
        success: function (res) {
            console.log("successfully sent to view")
            sessionStorage.removeItem('product_list');
            sessionStorage.removeItem('card_list');
            sessionStorage.removeItem('box_list');
            $("#checkout_table").load(location.href + " #checkout_table");
            load_cart();
          
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
        cards[parseInt(mem - 1)].className = "card1 b-0 show";

        if (sessionStorage.product_list || sessionStorage.card_list || sessionStorage.box_list) {
            var data_list= {};
            data_list['product_list'] = sessionStorage.product_list;
            data_list['card_list'] = sessionStorage.card_list;
            data_list['box_list'] = sessionStorage.box_list;

            var card_count = document.getElementsByClassName("card1").length;
            console.log("befor send data", card_count, (parseInt(mem)));
            if (card_count == (parseInt(mem))) {
                console.log("calling send data-- datalist:",data_list);
                send_data(JSON.stringify(data_list));
            }
        }
        
    }
}
