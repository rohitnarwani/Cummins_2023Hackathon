import React, {useState} from "react";
import PortionButton from "./PortionButton.js"
import styles from "./FoodCard.module.css"

function FoodCard({m, handler, currentCount, update}) {
        let [price, setPrice] = useState(m.price);
        function _handler(name, count) {
            if ( !! update ) {
                setPrice(m.oprice * count);
            }
            handler(name, count);
        }
    return (
      <div className={styles.foodCard}>
        <img src={m.img}
        alt="foodImage" className={styles.foodImage} />
        <div className={styles.foodDescription}>
          <span className={styles.foodName}>{m.name}</span>
          <span className={styles.foodPrice}>{`${price} Rs`}</span>
        </div>
        <div className={styles.portionButton}>
            <PortionButton name={m.name} handler={_handler} currentCount={currentCount}/>
        </div>
      </div>
    );
}

export default FoodCard;
