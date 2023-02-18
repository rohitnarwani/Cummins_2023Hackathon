const {spawn}=require("child_process")

const createSummary= function(string,setSummary){
   
    const python=spawn("python",["nlp.py",string])
    python.stdout.on('data',function(data){
        setSummary(data.toString());
     

    })

}

module.exports={
    createSummary,
}