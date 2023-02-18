// import React, { Fragment, useEffect, useRef, useState } from "react";
// import styles from "./chatsection.module.css";
// import { json } from "react-router-dom";

// const ChatSection = () => {
//   const [queryResult, setResults] = useState(null);
//   const [enteredQuery, setEnteredQuery] = useState("");
//   const inputRef = useRef();
//   const FormSubmitHandler = (event) => {
//     event.preventDefault();
//     if (inputRef.current.value.trim().length == 0) return;
//     setEnteredQuery(inputRef.current.value);
//   };

//   useEffect(() => {
//     if (enteredQuery.trim().length == 0) return;
//     const sendQuery = async function () {
//       const response = await fetch(
//         "https://anna-35dee-default-rtdb.firebaseio.com/queries.json",

//         {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify({
//             enteredQuery,
//           }),
//         }
//       );
//       const data = await response.json();
//     };
//     sendQuery();
//     const getResponse = async () => {
//       const response = await fetch(
//         "https://anna-35dee-default-rtdb.firebaseio.com/results.json"
//       );
//       const data = await response.json();
//       setResults(data);
//     };
//     getResponse();
//     console.log(queryResult);
//   }, [enteredQuery]);

//   if (queryResult) {
//     return (
//       <div className={styles.chatsection}>
//         <div className={styles.replyarea}>
//           <div className={styles.question}>{enteredQuery}</div>
//           <div className={styles.answer}>
//             <div className={styles.summarytxt}>
//               {queryResult.shortSynthasis}{" "}
//             </div>
//             <div className={styles.ans}>
//               {queryResult.searchresults.map((ele) => {
//                 return (
//                   <Fragment>
//                     <div className={styles.ansele} key={Math.random()}>
//                       <p className={styles.fileName}>
//                         File Name: {ele.filename}
//                       </p>
//                       <p className={styles.fileName}>{ele.summary}</p>
//                     </div>
//                     <div className={styles.line} key={Math.random()}></div>
//                   </Fragment>
//                 );
//               })}
//             </div>
//           </div>
//         </div>
//         <div className={styles.inputarea}>
//           <form className={styles.chatform} onSubmit={FormSubmitHandler}>
//             <input
//               ref={inputRef}
//               className={styles.inputFeild}
//               placeholder="Click Here to Chat"
//             ></input>
//             <button className={styles.subbutton}>send</button>
//           </form>
//         </div>
//       </div>
//     );
//   } else {
//     return (
//       <div className={styles.chatsection}>
//         <div className={styles.replyarea}></div>
//         <div className={styles.inputarea}>
//           <form className={styles.chatform} onSubmit={FormSubmitHandler}>
//             <input
//               ref={inputRef}
//               className={styles.inputFeild}
//               placeholder="Click Here to Chat"
//             ></input>
//             <button className={styles.subbutton}>send</button>
//           </form>
//         </div>
//       </div>
//     );
//   }
// };

// export default ChatSection;

import React, { Fragment, useEffect, useRef, useState } from "react";
import styles from "./chatsection.module.css";
import { json } from "react-router-dom";

const ChatSection = () => {
  const [queryResult, setResults] = useState(null);
  const [enteredQuery, setEnteredQuery] = useState("");
  const inputRef = useRef();
  const FormSubmitHandler = (event) => {
    event.preventDefault();
    if (inputRef.current.value.trim().length == 0) return;
    setEnteredQuery(inputRef.current.value);
  };

  useEffect(() => {
    if (enteredQuery.trim().length == 0) return;
    const getResponse = async () => {
      const response = await fetch("http://localhost:5000/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: enteredQuery,
        }),
      });

        const data =await response.json()
      // const data = await response.json();
      setResults(data);
      };
    getResponse();
  }, [enteredQuery]);

  if (queryResult) {
    return (
      <div className={styles.chatsection}>
        <div className={styles.replyarea}>
          <div className={styles.question}>{enteredQuery}</div>
          <div className={styles.answer}>
            <div className={styles.summarytxt}>
              {queryResult.shortSynthasis}
            </div>
            <div className={styles.ans}>
              {queryResult.searchresults.map((ele) => {
                return (
                  <Fragment>
                    <div className={styles.ansele} key={Math.random()}>
                      <p className={styles.fileName}>
                        File Name: {ele.filename}
                      </p>
                      <p className={styles.fileName}>{ele.summary}</p>
                    </div>
                    <div className={styles.line} key={Math.random()}></div>
                  </Fragment>
                );
              })}
            </div>
          </div>
        </div>
        <div className={styles.inputarea}>
          <form className={styles.chatform} onSubmit={FormSubmitHandler}>
            <input
              ref={inputRef}
              className={styles.inputFeild}
              placeholder="Click Here to Chat"
            ></input>
            <button className={styles.subbutton}>send</button>
          </form>
        </div>
      </div>
    );
  } else {
    return (
      <div className={styles.chatsection}>
        <div className={styles.replyarea}></div>
        <div className={styles.inputarea}>
          <form className={styles.chatform} onSubmit={FormSubmitHandler}>
            <input
              ref={inputRef}
              className={styles.inputFeild}
              placeholder="Click Here to Chat"
            ></input>
            <button className={styles.subbutton}>send</button>
          </form>
        </div>
      </div>
    );
  }
};

export default ChatSection;
