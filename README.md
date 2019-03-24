Hello !
This is flask based application which I created for my college to view my attendance...
This application also provide api service which you can use for your project with our backend support..
To use Our Api services 
Base url : https://newlnct.herokuapp.com/api
You have to include a header in get request like this..
app_id : <API KEY>
And in parameters you habve to specify username and password...
  username:<username>
  password:<your password>
  
Example in Node JS :

var requests = require("requests")
requests.get("https://newlnct.herokuapp.com",{
headers:{
"app_id":<API KEY>
},
  qs:{
  "username":"<Username">,
    "password":"<password">
  }}
  ,(e,r,b)=>{
  //your code here
  //b is the response
  }
  )
