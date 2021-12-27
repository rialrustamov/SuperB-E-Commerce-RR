window.addEventListener("load", function () {
	cartProduct()

})

function cartProduct() {
	fetch(`${location.origin}/api/card/`,
		{
			method: "GET",
			credentials: 'include',
			headers: {
				"Content-Type": "application/json",
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		}
	)
		.then(response => response.json()).then(data => {
			// let responseData = await response.json()
			console.log(data)
			let cardListSection = document.getElementById('cart-sidebar')
			cardListSection.innerHTML = ''
			let total_product = document.getElementById('total_product')
			total_product.innerText = data.length
			let total_product_side = document.getElementById('total_product_side')
			let total_product_cart_price = document.getElementById('total_product_cart_price')
			let overall_cart_price = document.getElementById('overall_cart_price')
			cardLeftList = document.getElementById("cart-sidebar-left")
			cardShoppingList = document.getElementById('shopping-cart-page')
			totalPrice = document.getElementById('total-price')
			
			try {
				for (let i of data) {
					console.log(i);
					cardListSection.innerHTML += `
					<li class="item first">
					<div class="item-inner"><a class="product-image"
					title="${i['product']['product']['title']}"
					href="${location.origin}/product/product-detail/${i['product']['id']}"><img alt="${i['product']['product']['title']}" 
					src="${i['product']['image'][0]['image']}"></a>
					<div class="product-details">
					<div class="access"><a class="btn-remove1 remove-item" onmouseover='removeItemCart()'  data_id="${i['product']['id']}"
					title="Remove This Item">Remove</a>
					</div>
					<!--access--> <strong>${i['quantity']}</strong> x <span
					class="price">$${i['product']['product']['discount_price']}</span>
					<p class="product-name"><a href="${location.origin}/product/product-detail/${i['product']['id']}">${i['product']['product']['title']}</a></p>
					</div>
					</div>
					</li>`
				}
			} catch {
				// i['product']['image'][0]['image']
			}
			if (cardLeftList != null) {
				cardLeftList.innerHTML = ''
				total_product_side.innerText = data.length
				total = 0
				for (let i of data) {
					total += parseFloat(i['product']['product']['discount_price'] * parseFloat(i['quantity']))
					cardLeftList.innerHTML += `
					<li class="item"> <a href="${location.origin}/product/product-detail/${i['product']['id']}" title="${i['product']['product']['title']}" class="product-image"><img
					src="${i['product']['image'][0]['image']}" alt="${i['product']['product']['title']}"></a>
					<div class="product-details">
					<div class="access"> <a title="Remove This Item" class="btn-remove1 remove-item" onmouseover='removeItemCart()' data_id="${i['product']['id']}"> <span
					class="icon"></span> Remove </a>
					</div>
					<strong>${i['quantity']}</strong> x <span class="price">$${i['product']['product']['discount_price']}</span>
					<p class="product-name"> <a href="${location.origin}/product/product-detail/${i['product']['id']}">${i['product']['product']['title']}</a> </p>
					</div>
					</li>`
				}
				totalPrice.innerText = `$${total.toFixed(2)}`
			}
			if (cardShoppingList != null) {
				total = 0
				cardShoppingList.innerHTML = ''
				for (let i of data) {
					total += parseFloat(i['product']['product']['discount_price'] * parseFloat(i['quantity']))
					cardShoppingList.innerHTML += `                    
					<tr class="first odd">
					<td class="image"><a class="product-image" title="" href="#"><img width="75" height="75" alt="${i['product']['product']['title']}" src="${i['product']['image'][0]['image']}" %}"></a></td>
					<td><h2 class="product-name"> <a href="#">${i['product']['product']['title']}</a> </h2></td>
					<td class="a-center hidden-table"><a class="link-wishlist1 use-ajax" href="#">Move</a></td>
					<td class="a-center hidden-table"><span class="cart-price"> <span class="price">$${i['product']['product']['discount_price']}</span> </span></td>
					<td class="a-center movewishlist"><input maxlength="12" class="input-text qty update_cart_qty_class" title="Qty" size="4" value="${i['quantity']}" data_id="${i['product']['id']}" name=""></td>
					<td class="a-center movewishlist"><span class="cart-price"> <span class="price">$${parseFloat(i['product']['product']['discount_price'] * parseFloat(i['quantity'])).toFixed(2)}</span> </span></td>
					<td class="a-center last"><a class="button remove-item" onmouseover='removeItemCart()'  data_id="${i['product']['id']}" title="Remove item"><span><span>Remove item</span></span></a></td>
				</tr>`
			}
			overall_cart_price.innerText = `$${total.toFixed(2)}`
			total_product_cart_price.innerText = `$${total.toFixed(2)}`
		}
		})
	}
	
var BasketLogic = {
	addProduct(productId, action, quantity) {
		console.log(localStorage.getItem('token'));
		fetch(`${location.origin}/api/card/`, {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product_id': productId,
				'action': action,
				'quantity': quantity,
			})
		}).then(response => response.json()).then(data => {
			cartProduct()
		});

	}
}

var addToBasket = document.querySelectorAll('.btn-cart');


function removeItemCart() {
	var removeItemFromBasket = document.getElementsByClassName('remove-item')
	for (let i = 0; i < removeItemFromBasket.length; i++) {
		removeItemFromBasket[i].onclick = function () {
			console.log(removeItemFromBasket[i]);
			const productId = this.getAttribute('data_id');
			const action = 'remove'
			BasketLogic.addProduct(productId, action, quantity=1);
		}
	}
}

var clearItems = document.getElementById('empty_cart_button')
if (clearItems != null){
	clearItems.onclick = function () {
		var removeItemFromBasket = document.getElementsByClassName('remove-item')
		for (let i = 0; i < removeItemFromBasket.length; i++) {
			console.log(removeItemFromBasket[i]);
			const productId = removeItemFromBasket[i].getAttribute('data_id');
			const action = 'remove'
			BasketLogic.addProduct(productId, action, quantity=1);
		}
	}
}


addToBasket.forEach(item => {
	item.onclick = function () {
		const productId = this.getAttribute('data');
		const action = 'add'
		BasketLogic.addProduct(productId, action, quantity=1);
	}
})

var update_cart_qty = document.getElementById('update_cart_qty')

if (update_cart_qty != null){
	update_cart_qty.onclick = function () {
		update_cart_qty_class = document.getElementsByClassName('update_cart_qty_class')
		for (let i = 0; i < update_cart_qty_class.length; i++) {
			const quantity = update_cart_qty_class[i].value
			console.log(quantity);
			const productId = update_cart_qty_class[i].getAttribute('data_id')
			const action = 'update';
			BasketLogic.addProduct(productId, action, quantity);
		}
	}
}

var pro_det_add_to_cart = document.getElementById('pro-detail-add-to-cart')

if(pro_det_add_to_cart != null){
	pro_det_add_to_cart.onclick = function () {
		const productId = this.getAttribute('data');
		const action = 'add'
		const quantity = document.getElementById('qty').value
		console.log(quantity);
		BasketLogic.addProduct(productId, action, quantity);
}
}