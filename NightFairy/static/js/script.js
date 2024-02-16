document.getElementById("increaseNumber").onclick = function increaseNumber () {
  number = Number(document.getElementById("ong").innerHTML) + 1;
  document.getElementById("ong").innerHTML = number;
  document.getElementById("number").value = number;
}

document.getElementById("decreaseNumber").onclick = function decreaseNumber () {
  number = Number(document.getElementById("ong").innerHTML) - 1;
  if (number <= 1){
    number = 1;
  }
  document.getElementById("ong").innerHTML = number;
  document.getElementById("number").value = number;
}


// Cart


/*



function num(){

  var number = document.getElementById('rng').value;
  var output = document.getElementById('ong');
  output.innerHTML = number;
}
var rng = document.getElementById("rng")
rng.addEventListener("click", num);

document.getElementById("addToBasket").onclick = function () {
  const div = document.createElement('div');
  //div css  |||  I don't lnow why, but i can't make class for the element and if i make id it doesn't work correctly
  div.style.border = "1px gray solid";
  div.style.height = 'auto';
  div.style.width = '250px';
  div.style.color = '#FEFFBF'
  div.id = 'box_div'


  
  
  if (document.getElementById('box_div')) {
    const number = document.getElementById('box_h3').innerHTML
    console.log(number)
    number = 's'

  }else{
    
    document.body.appendChild(div); // intialization of div
    

    
  }


  
  

  const product_title = document.getElementById('product_title').innerHTML // get product's id
  
  // getting product's price
  function get_product_price(){

    try {
      const product_price = document.getElementById('strike_price').innerHTML
      return product_price
    
    }

    catch {
      const product_price = document.getElementById('price').innerHTML
      return product_price
    }

  };
  //create div2
  const div2 = document.createElement('div');
  div2.style.border = "1px gray solid";
  div2.style.height = 'auto';
  div2.style.width = '250px';
  div2.style.color = '#FEFFBF'
  div.appendChild(div2); // intialization of div
  
  //create h3 title
  const h3 = document.createElement('h3')
  h3.innerHTML = product_title
  h3.id = 'box_h3'
  div2.appendChild(h3)

  //create p simple description
  const desc = document.getElementById('product_desc').value //get description
  const p_desc = document.createElement('p')
  p_desc.innerHTML = 'Описание: ' + desc
  div2.appendChild(p_desc)

  //create p price


  const p_price = document.createElement('p')
  p_price.innerHTML = 'Цена: ' + get_product_price()
  div2.appendChild(p_price)


}*/
