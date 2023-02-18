import React from "react";
import ChatSection from "../components/ChatSection";
import Navbar from "../components/Navbar";
import styles from "./Home.module.css";

const Home = () => {
  console.log("hello");
  return (
    <div className={styles.HomeBox}>
      {/* navbar */}
      <Navbar></Navbar>
      {/* chat section */}
      <ChatSection></ChatSection>
    </div>
  );
};
export default Home;
