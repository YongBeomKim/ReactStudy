var pcart = document.querySelector("#bcart");
var ptotal = document.querySelector("#btotal");

// add Pizza
function addBurger(pid) {

    // get Pizza name
    var burgerId = "#bur" + pid;
    var name = document.querySelector(burgerId).innerHTML;
    // get Pizza price
    var radio = 'burger' + pid;
    var price = document.getElementsByName(radio);
    var size;
    if (price[0].checked) {
        price = price[0].value;
        size = 'M';
    } else {
        price = price[1].value;
        size = "L "
    }
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    //
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    buttonTotal = '<div class="del" onclick="removeBurger(' + cartSize + ')">x</div>';
    btotal.innerHTML = 'Total: ' + total + ' $';
    bcart.innerHTML += '<li>' + name + ' ' + size + ': ' + price + ' $' + buttonTotal + '</li>';
}

function bshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSiZe = orders.length;

    bcart.innerHTML

    for (let i = 0; i < cartSiZe; i++) {
        button = '<div class="del" onclick="removeBurger(' + i + ')">x</div>';
        bcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ': ' + orders[i][2] + ' $' + button + '</li>';
    }
    btotal.innerHTML = 'Total: ' + total + ' $';
}

bshoppingCart();

function removeBurger(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    bshoppingCart();
}