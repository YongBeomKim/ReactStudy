var itemname = document.querySelector("#name");
var size = document.querySelector("#size");
var price = document.querySelector("#price");
var totalbill = document.querySelector("#total");
var remove = document.querySelector("#remove");


function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSiZe = orders.length;

    itemname.innerHTML = '<h3>Name</h3>';
    size.innerHTML = '<h3>Size</h3>';
    price.innerHTML = '<h3>Price</h3>';
    remove.innerHTML = '<h3>Remove</h3>';

    for (let i = 0; i < cartSiZe; i++) {
        remove.innerHTML += '<h4><button class="btn-danger" onclick="removeItem(' + i + ')">x</button></h4>';
        itemname.innerHTML += '<h4>' + orders[i][0] + '</h4>';
        size.innerHTML += '<h4>' + orders[i][1] + '</h4>';
        price.innerHTML += '<h4>' + orders[i][2] + '</h4>';
    }
    totalbill.innerHTML = 'Total: ' + total + ' $';
}

pshoppingCart();

function removeItem(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppingCart();
}

// Ajax
var messageNote = document.querySelector('#message')

function order() {

    // passing Data
    var message = messageNote.value;
    var orders = localStorage.getItem('orders');
    var total = localStorage.getItem('total');

    var urlink = "/food/order"
    var orderData = {};

    orderData['orders'] = orders;
    orderData['note'] = message;
    orderData['bill'] = total;

    $.ajax({
        url: urlink,
        type: 'POST',
        data: orderData,
        success: function (data) {
            window.location.replace('/food/success');
            console.log('sent Post Method');
        }
    })
}