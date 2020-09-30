var pcart = document.querySelector("#pcart");
var ptotal = document.querySelector("#ptotal");

// add Pizza
function addPizza(pid) {

    // get Pizza name
    pizzaId = "#piz" + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    // get Pizza price
    var radio = 'pizza' + pid;
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

    buttonTotal = '<div class="del" onclick="removePizza(' + cartSize + ')">x</div>';
    ptotal.innerHTML = 'Total: ' + total + ' $';
    pcart.innerHTML += '<li>' + name + ' ' + size + ': ' + price + ' $' + buttonTotal + '</li>';
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSiZe = orders.length;

    pcart.innerHTML = '';

    for (let i = 0; i < cartSiZe; i++) {
        button = '<div class="del" onclick="removePizza(' + i + ')">x</div>';
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ': ' + orders[i][2] + ' $' + button + '</li>';
    }
    ptotal.innerHTML = 'Total: ' + total + ' $';
}

pshoppingCart();

function removePizza(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppingCart();
}