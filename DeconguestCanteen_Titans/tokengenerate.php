<!-- 



<!DOCTYPE html>
<html>
  <head>
    <title>Order Form</title>
  </head>
  <body>
    <h1>Order Form</h1>
    <form id="order-form">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>

      <label for="product">Product:</label>
      <select id="product" name="product" required>
        <option value="">Select a product</option>
        <option value="Product A">Product A</option>
        <option value="Product B">Product B</option>
        <option value="Product C">Product C</option>
      </select>

      <input type="hidden" id="token-input" name="token">

      <button type="submit">Submit</button>
    </form>

    <script>
        const form = document.querySelector('#order-form');

        form.addEventListener('submit', (event) => {
          // prevent the form from submitting
          event.preventDefault();
        
          // generate a unique token ID
          const randomNumber = Math.random();
          const timestamp = new Date().getTime();
          const tokenId = `${randomNumber}-${timestamp}`;
        
          // display the token ID on the page
          const tokenDisplay = document.createElement('div');
          tokenDisplay.innerHTML = `<h2>Token ID: ${tokenId}</h2><button id="print-button">Print</button>`;
          form.appendChild(tokenDisplay);
        
          // add a click event listener to the "Print" button
          const printButton = document.querySelector('#print-button');
          printButton.addEventListener('click', () => {
            window.print();
          });
        });
        
    </script>
  </body>
</html> -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pop up</title>
    <link rel="stylesheet" href="styles.css">
</head>
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

.container {
    width: 100%;
    height: 100vh;
    background: url(bg-1.jpg);
    display: flex;
    align-items: center;
    justify-content: center;
}

.btn {
    padding: 10px 60px;
    background: aliceblue;
    border: 0;
    outline: none;
    cursor: pointer;
    font-size: 22px;
    font-weight: 500;
    border-radius: 30px;

}
.btn:hover{
  background: #2196f3;
}

.popup {
    width: 400px;
    background: #fff;
    border-radius: 6px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.1);
    text-align: center;
    padding: 0 30px 30px;
    color: #333;
    visibility: hidden;
    transition: transform 0.4s, top 0.4s;
}

.open-popup {
    visibility: visible;
    top: 50%;
    transform: translate(-50%, -50%) scale(1);
}

.popup img {
    width: 100px;
    margin-top: -50px;
    border-radius: 50%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.popup h2 {
    font-size: 38px;
    font-weight: 500;
    margin: 30px 0 10px;
}

.popup button {
    width: 100%;
    margin-top: 50px;
    padding: 10px 0;
    background: #6fd649;
    color: #fff;
    border: 0;
    outline: none;
    font-size: 18px;
    border-radius: 4px;
    cursor: pointer;
     box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
#print-button{
  width: 100px;
    color: white;
    background: black;
    margin: 10px;

}
#c2{
  margin:15px;
}
</style>
<body>
    <div class="container">
      <form id="order-form">
        <button type="submit" class="btn" onclick="openPopup()">Generate Token</button>
        </form>
        <div class="popup" id="popup">
            <img src="imges/tick.jpeg" alt="">
            <h2>Thank You!</h2>
            <p>You will find your token below </p>
            <p>You may print it </p>
            <p>By clicking below print option</p>
           
    
            <button type="button" onclick="closePopup()">OK</button>
        </div>
    </div>

<script>
let popup = document.getElementById("popup");

function openPopup() {
    popup.classList.add("open-popup");
}
function closePopup() {
    popup.classList.remove("open-popup");
}
</script>

<script>
        const form = document.querySelector('#order-form');

        form.addEventListener('submit', (event) => {
          // prevent the form from submitting
          event.preventDefault();
        
          // generate a unique token ID
          const randomNumber = Math.random();
          const timestamp = new Date().getTime();
          const tokenId = `${randomNumber}-${timestamp}`;
        
          // display the token ID on the page
          const tokenDisplay = document.createElement('div');
          tokenDisplay.innerHTML = `<h2 id="c2">Token ID: ABS ${tokenId}</h2><button id="print-button">Print</button>`;
          form.appendChild(tokenDisplay);
        
          // add a click event listener to the "Print" button
          const printButton = document.querySelector('#print-button');
          printButton.addEventListener('click', () => {
            window.print();
          });
        });
        
    </script>

</body>
</html>
