import './App.css';
import Home from './components/Home';
import Checkout from './components/Checkout';
import Login from './components/Login';
import Vendor from "./components/Vendor";
import axios from 'axios'
import {useState} from "react";
const URL="https://canteensystem.azurewebsites.net/"

function App() {
    let [cart, setCart] = useState(new Map());
    let [co, setco] = useState(false);
    let [date, setDate] = useState(null)
    let [seats, setSeats] = useState(0)
    let [email, setEmail] = useState('')
    let [loggedIn, setLoggedIn] = useState(false)
    let [vendor, setVendor] = useState(false)

    function cardHandler(name, count) {
        setCart(cart.set(name, count));
    }

    function subHandle() {
        setco(true)
    }

    function getVal(name) {
        if (cart.get(name) === undefined || cart === undefined){
            return 0;
        } else {
            return cart.get(name)
        }
    }

    function inCart(name) {
        return !(cart.get(name) === undefined || cart === undefined)
    }

    function doneFunc() {
        bookHandler()
    }

    function reqHandler(date, seats) {
        console.log(date, seats)
        setDate(date)
        setSeats(seats)
    }

    // Example POST method implementation:
    async function postlogin(url = '', data = {}) {
      // Default options are marked with *
      const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json'
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
      });
      let res = await response.json(); // parses JSON response into native JavaScript objects
        document.cookie=`token=${res.token}`
    }

    function getCookie(cname) {
      let name = cname + "=";
      let decodedCookie = decodeURIComponent(document.cookie);
      let ca = decodedCookie.split(';');
      for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    }

    function loginHandle(_email, _password) {
        setEmail(_email)
        setLoggedIn(true)
    }

    function vendorHandle() {
        console.log("Here")
        setVendor(true)
        setLoggedIn(true)
    }

    function carti() {
        let a = []
        for (let [key, value] of cart) {
            a.push({item_name: key, item_qty: value})
        }
        return a;
    }

    function convertTZ(date, tzString) {
        return new Date((typeof date === "string" ? new Date(date) : date).toLocaleString("en-US", {timeZone: tzString}));
    }

    function bookHandler() {
        let _date = new Date(date.year, date.month - 1, date.day, date.hour, date.minute)
        let __date = _date.toISOString()
        let data = { email: email, seat_count: seats, orders: carti(), start_time: __date }
        axios.post(URL + 'booking', data).
                then(function (response) {
                console.log(response);
                })
              .catch(function (error) {
                console.log(error);
              });
        // console.log(post(URL + "booking", data));
    }

   if (!loggedIn) {
       return <Login signinHandle={vendorHandle} loginHandle={loginHandle}/>
   }

   if (vendor) {
       return <Vendor/>
   }

  return (
    <div className="App">
    { co && <Checkout reqHandler={reqHandler} doneFunc={doneFunc} inCart={inCart} getVal={getVal} cardHandler={cardHandler}/> || <Home getVal={getVal} subHandle={subHandle} cardHandler={cardHandler}/> }
    </div>
  );
}

export default App;
