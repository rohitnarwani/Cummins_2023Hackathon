const fetchFunc = require("./importData");
const {createSummary}=require("./createSummary");
// let datal = {
//   searchresults:[{
//     filename:"chaper 1.pdf",
//     tag:"hr",
//     Location:"Banglore",

//     summary:"He then ordered the remaining torpedoes inspected and his crew could find no fault with them. Daspit launched three consecutive torpedoes from this position which all hit but failed to explode. He then ordered the remaining torpedoes inspected and his crew could find no fault with them."
//   },
//   {
//     filename:"chaper 2.pdf",
//     tag:"rd",
//     location:"Mumbai",
//     summary:"He then ordered the remaining torpedoes inspected and his crew could find no fault with them. Daspit launched three consecutive torpedoes from this position which all hit but failed to explode. He then ordered the remaining torpedoes inspected and his crew could find no fault with them."
//   },
//   {
//     filename:"chaper 3.pdf",
//     tag:"rd",
//     location:"Pune",
//     summary:"He then ordered the remaining torpedoes inspected and his crew could find no fault with them. Daspit launched three consecutive torpedoes from this position which all hit but failed to explode. He then ordered the remaining torpedoes inspected and his crew could find no fault with them."
//   },{
//     filename:"chaper 4.pdf",
//     Location:"Thane",
//     summary:"He then ordered the remaining torpedoes inspected and his crew could find no fault with them. Daspit launched three consecutive torpedoes from this position which all hit but failed to explode. He then ordered the remaining torpedoes inspected and his crew could find no fault with them."
//   },
//   {
//     filename:"chaper 5.pdf",
//     tag:"hr",
//     Location:"NYC",

//     summary:"He then ordered the remaining torpedoes inspected and his crew could find no fault with them. Daspit launched three consecutive torpedoes from this position which all hit but failed to explode. He then ordered the remaining torpedoes inspected and his crew could find no fault with them."
//   },
//   ]
// };
const trialFunc = async (porp) => {

  porp=porp.toLowerCase()

  
  

  data = await fetchFunc.FetchData(porp);
  
  let datal={
    searchresults:[]
  }


  const arrtags=["Finance","Marketing","HR","Research"]
  const typearr=["pdf","docs"]
  function randomIntFromInterval(min, max) { 
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  
  for(val of data.value){
      const filename=val.metadata_title;
      const location=val.locations[0]
      const tagNum=randomIntFromInterval(1,4);
      const typeNum=randomIntFromInterval(1,2);
      const tag=arrtags[tagNum-1]
      const type=typearr[typeNum-1]
      // const tag 
      var summary="";
      summary=val.content;
    let mid =summary.indexOf(porp);
    let start=Math.max(mid-300,0);
      let end=Math.min(mid+300,summary.length)

    summary=summary.slice(start,end+1);

      // let i=0;
      // let j=0;
      // let count=0;
      // while(j<1000){
      //   if(splitarry[j]===porp){
      //     count++;
      //   }
      // }

      // let maxi=count;
      // let maxis=0;
      // let maxjs=j;
      // while(j<splitarry.length){
      //   if(splitarry[i]===porp)count--;
      //   if(splitarry[j]===porp)count++;
      //   if(count>maxi){
      //       maxis=++i;
      //       maxjs=j++;
      //   }else{
      //     i++;
      //     j++;
      //   }
      // }

      // console.log(summary.slice(maxis,maxjs));


      const setSummary=function(summaryval){
        summary=summaryval
      }
        createSummary(summary,setSummary)
        setTimeout(() => {
      
        }, 10000);

        
         mid =summary.indexOf(porp);
         start=Math.max(mid-50,0);
        end=Math.min(mid+250,summary.length)

        summary=summary.slice(start,end+1);

        datal.searchresults.push({
          filename,
          tagNum,
          tag,
          typeNum,
          type,
          location,
          summary
        })


  }

  return datal

};



trialFunc("kelvin")
module.exports={
  trialFunc
}
