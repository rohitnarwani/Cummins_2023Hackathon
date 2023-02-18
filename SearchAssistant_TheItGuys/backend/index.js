const express = require("express");
const app = express();
const port = 5000;
const cors = require("cors");
const http = require("http");
const {trialFunc}=require("./process_data/processData")
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(cors());

app.post("/", cors(), async (req, res) => {
  const {query}=req.body
  console.log(query);
  const t= await trialFunc(query)
  const result=JSON.stringify(t)
  res.send(result);
  res.status(200).end();
});

app.listen(port, () => {
  console.log("lesting at 5000");
});
