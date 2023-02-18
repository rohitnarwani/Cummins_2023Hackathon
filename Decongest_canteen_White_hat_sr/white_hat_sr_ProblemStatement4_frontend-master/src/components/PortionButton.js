import React, {useState} from "react";
import styles from "./FoodCard.module.css"

function PortionButton({name, handler, currentCount}) {
    let [ count, setCount ] = useState(currentCount);

    function _handler(count) {
        setCount(count)
        handler(name, count);
    }

    function GetHandler(operator) {
        if (operator === "-") return () => { if (count > 0) _handler(count-1); }
        else if (operator === "+") return () => { _handler(count+1); }
    }

    if (count === null || count === undefined) {
        count = 0;
    }

    if (count === 0) {
        return (
          <button className={styles.addButton} onClick={GetHandler('+')}>Add</button>
        )
    } else {
        return (
            <>
              <button className={styles.minus} onClick={GetHandler('-')}>-</button>
              <div className={styles.quantity}>{count}</div>
              <button className={styles.plus} onClick={GetHandler('+')}>+</button>
            </>
        )
    }
}

export default PortionButton;
