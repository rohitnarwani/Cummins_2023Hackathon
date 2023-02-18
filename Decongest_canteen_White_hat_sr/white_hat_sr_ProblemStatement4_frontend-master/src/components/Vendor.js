import React, {useState} from "react";
import axios from "axios"
import styles from "./Vendor.module.css"
const URL="https://canteensystem.azurewebsites.net/"
const WEB_SOCK="wss://canteensystem.azurewebsites.net/ws/notifications/neworders"

function VendorItem({m, id, handler}) {
  function getOn() {
      handler(id)
  }
  return (
    <div className={styles.Top}>
      <button onClick={getOn} className={styles.checkBox}>{m.status}</button>
      <div className={styles.orderId}> {`${m.id} . ${m.From}`} </div>
    </div>
  );
}

function Vendor(props){
    let [orders, setOrders] = useState([])
    let [loading, setLoading ] = useState(true)
    let [first, setFirst] = useState(true);
    function nextState(status) {
        switch (status) {
            case "placed" : {
                return "preparing";
            }
            case "preparing" : {
                return "finished";
            }
            default: {
                return status;
            }
        }
    }

    function changeStatus(id) {
        setLoading(true)
        let m = orders[id]
        axios.put(URL + "/orders", {
            order_id_list : [m.id],
            next_state : nextState(m.status),
        }).then(function (response) {
            if (response.data !== undefined){
            setLoading(false)
            setOrders(response.data)
            setFirst(true)
            }
        }).catch(function (error) {
            console.log(error);
        });
    }

    if (first) {
        axios.get(URL + `/orders`, {}).
            then(function (response) {
                setOrders(response.data)
                setLoading(false)
            }).catch(function (error) {
                console.log(error);
            });
        setFirst(false)
    }

    if (loading) {
        return <div className="loading">
            Loading......
            </div>
    }

    return (
      <div className="orders">
       { orders.map((id, index) => <VendorItem key={index} id={index} handler={changeStatus} m={id} />) }
      </div>
    )
}

export default Vendor;


// const socket = new WebSocket('wss://canteensystem.azurewebsites.net/ws/notifications/neworders')

// // Connection opened
// socket.addEventListener('open', (event) => {
//     socket.send(JSON.stringify({time_quantum:10}));
// });

// // Listen for messages
// socket.addEventListener('message', (event) => {
//     console.log('Message from server ', event.data);
//     socket.send(JSON.stringify({time_fquantum:10}));

// });
