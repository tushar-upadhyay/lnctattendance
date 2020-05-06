
<h2>LNCT Attendance and RGPV Results Fetcher  </h2>

This is a flask based application which provides apis to get different data of LNCT Bhopal and RGPV Bhopal

### Using the Apis
You can use the API's in your application to get data
<b>Base Url -- </b><i> https://newlnct.herokuapp.com/</i>
##### Basic Attendance (returns a JSON response with attnedance and percentage)
Make a get request to: 
https://newlnct.herokuapp.com/?username=youraccsoftid&password=yourpassword

<i>E.g. https://newlnct.herokuapp.com/?username=123&password=123</i>
##### Datewise attendance 
Make a get request to: 
https://newlnct.herokuapp.com/dateWise?username=id&password=pass

<i>E.g. https://newlnct.herokuapp.com/dateWise?username=123&password=123</i>
##### Subject Wise attendance 
Make a get request to: 
https://newlnct.herokuapp.com/subjectwise?username=id&password=pass

<i>E.g. https://newlnct.herokuapp.com/subjectwise?username=123&password=123</i>
##### Attendance till date
Make a get request to: 
https://newlnct.herokuapp.com/getDateWiseAttendance?username=id&password=pass

<i>E.g. https://newlnct.herokuapp.com/getDateWiseAttendance?username=123&password=123</i>
### Important 
<b>If you are student of LNCT University then include &lnctu at the end of each url</b><br>
<i>https://newlnct.herokuapp.com/?username=username&password=pass&lnctu</i>
### RGPV Result
Make a get request to: 
https://newlnct.herokuapp.com/api?rollNo=enrollment&semester=semester&stream=code
<b>Stream codes </b>
<table style="width:100%">  
<tr>  
<th>Stream</th>  
<th>Code</th>  
</tr>  
<tr>  
<td>B.Tech</td>  
<td>0</td>  
</tr>  
<tr>  
<td>M.Tech</td>  
<td>1</td>  
</tr>  
<tr>  
<td>B.Pharma</td>  
<td>2</td>  
</tr>  
</table>
More Streams will be added soon<br>
<i>E.g. https://newlnct.herokuapp.com/api?semester=3&rollno=0103cs181175&stream=0</i>
