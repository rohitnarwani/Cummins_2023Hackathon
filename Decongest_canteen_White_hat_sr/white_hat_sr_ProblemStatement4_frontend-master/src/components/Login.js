import React from "react";
import {useState} from "react";
import styles from "./Login.module.css"

function Login({loginHandle, signinHandle: vendorHandle}) {
    let [userName, setUserName ] = useState('');
    let [password, setPassword ] = useState('');

    function updateUserName(username) {
        setUserName(username.target.value)
    }

    function updatePassword(password) {
        setPassword(password.target.value)
    }

    function _loginHandle() {
        loginHandle(userName, password)
    }

    return (
        <div className={styles.loginBody}>
          <span className={styles.userName}>Email </span>
          <input onChange={updateUserName} type="Enter User Name" />
          <span className={styles.password}> Password </span>
          <input onChange={updatePassword} type="Enter Password" />
          <div className={styles.buttonBox}>
            <button className={styles.login} onClick={_loginHandle}> Login </button>
            <button className={styles.signing} onClick={vendorHandle}> Vendor Login</button>
          </div>
        </div>
    );
}

export default Login;
