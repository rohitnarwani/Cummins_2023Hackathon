import React from "react";
import SearchView from "./SearchView.js"
import styles from "./Home.module.css"

function Home({cardHandler, getVal, subHandle}){
    return (
        <div>
        <div className={styles.top}>
            <h1>Home</h1>
            <button className={styles.submit} onClick={subHandle}>Checkout</button>
        </div>
        <div className={styles.sview}>
            <SearchView getVal={getVal} cardHandler={cardHandler}/>
        </div>
        </div>
    );
}

export default Home;
