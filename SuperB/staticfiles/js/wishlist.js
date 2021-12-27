window.addEventListener("load", function () {
    productWishlist()
})

function productWishlist() {
    fetch(`${location.origin}/api/wishlist/`,
        {
            method: "GET",
            credentials: 'include',
            headers: {
                "Content-Type": "application/json",
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        }
    ).then(response => response.json()).then(data => {
        console.log(data);
        let my_wishlist = document.getElementById('my-wishlist')
        if (my_wishlist) {
            my_wishlist.innerHTML = ''
        }
        var array_wishlist = []
        for (let i = 0; i < data['product'].length; i++) {
            array_wishlist.push(parseInt(data['product'][i]['id']))
            if (my_wishlist) {
                my_wishlist.innerHTML += `
                    <tr id="item_31" class="first odd">
                        <td class="wishlist-cell0 customer-wishlist-item-image"><a title="${data['product'][i]['product']['title']}" href="#" class="product-image"> <img width="150" height="150" alt="${data['product'][i]['product']['title']}" src="${data['product'][i]['image'][0]['image']}"> </a></td>
                        <td class="wishlist-cell1 customer-wishlist-item-info"><h3 class="product-name"><a title="${data['product'][i]['product']['title']}" href="#">${data['product'][i]['product']['title']}</a></h3>
                        <div class="description std">
                            <div class="inner">${data['product'][i]['product']['description']}</div>
                        </div>
                        <td data-rwd-label="Price" class="wishlist-cell3 customer-wishlist-item-price"><div class="cart-cell">
                            <div class="price-box"> <span class="regular-price"> <span class="price">$${data['product'][i]['product']['discount_price']}</span> </span> </div>
                        </div></td>
                        <td class="wishlist-cell4 customer-wishlist-item-cart"><div class="cart-cell">
                            <button class="button btn-cart" data="${data['product'][i]['id']}" onmouseover='addToCart()' title="Add to Cart" type="button"><span><span>Add to Cart</span></span></button>
                        </div>
                        <td class="wishlist-cell5 customer-wishlist-item-remove last"><a class="remove-item" style="cursor: pointer;" onmouseover='removeWishlistItem()' data_id="${data['product'][i]['id']}" title="Clear Cart"><span><span></span></span></a></td>
                    </tr>`
            }
        }
        for (let i = 0; i < pro_add_wishlist.length; i++) {
            if (array_wishlist.includes(parseInt(pro_add_wishlist[i].getAttribute('data')))) {
                pro_add_wishlist[i].children[0].innerHTML = `<span>Remove from Wishlist</span>`;
                if (wishlist_click[i]) {
                    wishlist_click[i].style.background = 'red';
                }
                // console.log(wishlist_click[i].children[0]);
            }
            else {
                pro_add_wishlist[i].children[0].innerHTML = `<span>Add to Wishlist</span>`;
                // console.log(wishlist_click[i].children[0]);
                if (wishlist_click[i]) {
                    wishlist_click[i].style.background = '';
                }
            }
        }
    })
}

function goBack() {
    window.history.back();
}

var pro_add_wishlist = document.getElementsByClassName('pro-add-wishlist')

var wishlist_click = document.getElementsByClassName('added-wislist-html')



for (let i = 0; i < pro_add_wishlist.length; i++) {
    pro_add_wishlist[i].onclick = function () {
        const productId = this.getAttribute('data');
        WishLogic.productPostWishlist(productId);
    }
}


var WishLogic = {
    productPostWishlist(productId) {
        console.log(localStorage.getItem('token'));
        fetch(`${location.origin}/api/wishlist/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
            })
        }).then(response => response.json()).then(data => {
            productWishlist()
        });

    }
}


function removeWishlistItem() {
    var removeItemFromwishlist = document.getElementsByClassName('remove-item')
    for (let i = 0; i < removeItemFromwishlist.length; i++) {
        removeItemFromwishlist[i].onclick = function () {
            console.log(removeItemFromwishlist[i]);
            const productId = this.getAttribute('data_id');
            WishLogic.productPostWishlist(productId);
        }
    }
}


function addToCart() {
    var addToBasket = document.querySelectorAll('.btn-cart');
    addToBasket.forEach(item => {
        item.onclick = function () {
            const productId = this.getAttribute('data');
            const action = 'add'
            BasketLogic.addProduct(productId, action, quantity = 1);
        }
    })
}

