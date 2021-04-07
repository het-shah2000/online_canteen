function update_item(id, action){
    itemId = id
    console.log('Item Id:', itemId , 'Action:', action)
    console.log(user)
    if(user=== 'AnonymousUser'){
        console.log('Not Logged IN')
    }
    else{
            console.log('User Is Authenticated')
            // updateUserOrder(itemId, action)
            // var url = '/update_item/'
            fetch('/update_item/', {
                method:'POST',
                headers:{
                    'Content-Type':'application/json', // fix
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({'itemId':itemId, 'action':action})  //data to be sent to the backend as a string
            })
            .then((response) => response.json())
                    //promises to be returned, after data is processed
                    //response turned to json
            .then((data) =>{
                console.log('Data:' , data)
                location.reload()
            });
        }
}
// function updateUserOrder(itemId, action){
    
//     var url = '/update_item/'

//     fetch(url, {
//         method='POST',
//         headers:{
//             'Context-Type':'application/json', // fix
//         },
//         body:JSON.stringify{'itemId':itemId, 'action':action}  //data to be sent to the backend as a string
//     })
    
//     .then((response) => {        //promises to be returned, after data is processed
//         return response.json();  //response turned to json
//         })
//     .then((data) => {
//         console.Log('Data:' , data)
//     })
        
// }
// for(var i=0;i<updateBtns.length; i++){
//     updateBtns[i] = addEventListener('click', function(){
//         var jsonData = JSON.stringify({ 
//             itemId: updateCart.dataset.items, 
//             action: updateCart.dataset.action 
//         })    
//         console.log('Item Id:', itemId , 'Action:', action)
//     })
// }
// function add_to_cart(pid, pname, price)
// {
//     let cart = localStorage.getItem("cart");
//     if (cart == null) {
//         //no cart yet
//         let products = [];
//         let product = {productId: pid, productName: pname, productQuantity: 1, productPrice: price}
//         products.push(product);
//         localStorage.setItem("cart", JSON.stringify(products));
//         console.log("Product is added for the first time")
//     } else {
//         //cart is already present
//         let pcart = JSON.parse(cart);
//         let oldProduct = pcart.find((item) => item.productId == pid)

//         if (oldProduct)
//         {
//             //we have to increase the quantity
//             oldProduct.productQuantity = oldProduct.productQuantity + 1
//             pcart.map((item) => {
//                 if (item.productId == oldProduct.productId)
//                 {
//                     item.productQuantity = oldProduct.productQuantity;
//                 }
//                 localStorage.setItem("cart", JSON.stringify(pcart));
//                 console.log("Product is added more than one times")
//             })
//         } else {
//             //we have add the product
//             let product = {productId: pid, productName: pname, productQuantity: 1, productPrice: price}
//             pcart.push(product)
//             localStorage.setItem("cart", JSON.stringify(pcart));
//         }
//     }
//     updateCart();
// }


// function updateCart()
// {
//     let cartString = localStorage.getItem("cart");
//     let cart = JSON.parse(cartString);
    
//     if (cart == null || cart.length == 0)
//     {
//         console.log("Cart is empty !! for real")
//         $(".badge").html(`0`)
//         let table = `
//             <table class="table">
//                             <thead>
//                                 <tr>
//                                     <th><i class="fas fa-pizza-slice fa-spin"></i> Your Plate seems Empty</th>
//                                 </tr>
//                             </thead>

//             `;
//         table = table + `</table>`
//         $(".hettable").html(table);
//         let gtot=0;
//         let gtax=0;
//         $(".hettot").html(`${gtot}`);
//         $(".hettax").html(`${gtax}`);
//         $(".hetmax").html(`${gtot + gtax}`);

//     } else {
// //      there is some in cart to show
//         console.log(cart)
//         $(".badge").html(`${cart.length}`)
//         let table = `
//         <form action="cout">
//             <table class="table">
//                             <thead>
//                                 <tr>
//                                     <th>Product Name</th>
//                                     <th>Price</th>
//                                     <th>Quantity</th>
//                                     <th>Total</th>
//                                     <th>Remove</th>
//                                 </tr>
//                             </thead>

//             `;

//         table += `<tbody>`
//         let gtot = 0;
//         cart.map((item) => {
//             let itot = item.productPrice * item.productQuantity;
//             table += `
            
//             <tr>
//                 <td class="name-pr">
//                     <a>
//                         ${item.productName}
//                     </a>
//                 </td>
//                 <td class="price-pr">
//                     <p>&#8377; ${item.productPrice}</p>
//                 </td>
//                 <td class="quantity-box"><input id="pro${item.productId}" type="number" size="4" name="pap${item.productId}" value="${item.productQuantity}" min="0" step="1" class="c-input-text qty text"></td>
//                 <td class="total-pr">
//                     <p>&#8377; ${itot}</p>
//                 </td>
//                 <td class="remove-pr">
//                     <a onclick="deleteItemFromCart(${item.productId})" href="#!">
//                         <i class="fas fa-times"></i>
//                     </a>
//                 </td>
//             </tr>
            
//             `
//             gtot += item.productPrice * item.productQuantity;
//         })
//         let gtax = (5 * gtot) / 100;
//         console.log(gtot);
//         table += `</tbody>`
        
//         table = table + `</table>`
       
//         $(".hettable").html(table);
//         $(".hettot").html(`&#8377; ${gtot}`);
//         $(".hettax").html(`&#8377; ${gtax}`);
//         $(".hetmax").html(`&#8377; ${gtot + gtax}`);


//     }
// }

// //delete item
// function deleteItemFromCart(pid)
// {
//     let cart = JSON.parse(localStorage.getItem('cart'));
//     let newcart = cart.filter((item) => item.productId != pid)
//     localStorage.setItem('cart', JSON.stringify(newcart))
//     updateCart();
// }

// function imadeCart()
// {
//     let cart = JSON.parse(localStorage.getItem('cart'));
//     let newcart = cart.filter((item) => item.productQuantity = document.getElementById("pro" + item.productId).value)
//     localStorage.setItem('cart', JSON.stringify(newcart))
//     updateCart();
// }

// $(document).ready(function () {

//     updateCart();
// })