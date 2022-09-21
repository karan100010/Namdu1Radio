<!DOCTYPE html>
<html>
  <head>
  <link rel="icon" href="CR Bolo Logo.jpeg">
   <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><title>Upload file </title>
  
<style>
            #leftbox1 {
              float:left;
              width:50%
                text-align:center;
            }
            #middlebox1{
              float:left;
              width:50%;
              text-align:center;
            }
            #rightbo1{
              
              width:25%
              float : right;
              text-align:center;
            }
            img {  
              max-width: 100%;  
              height: auto;  
            }
            .b_img{  
              width: auto; 
              height: 700px;
              margin-bottom:-150px;
                
              }  
            
              .footer-basic {
  padding:40px 0;
  background-color:#ffffff;
  color:#4b4c4d;
}

.footer-basic ul {
  padding:0;
  list-style:none;
  text-align:center;
  font-size:18px;
  line-height:1.6;
  margin-bottom:0;
}

.footer-basic li {
  padding:0 10px;
}

.footer-basic ul a {
  color:inherit;
  text-decoration:none;
  opacity:0.8;
}

.footer-basic ul a:hover {
  opacity:1;
}

.footer-basic .social {
  text-align:center;
  padding-bottom:25px;
}

.footer-basic .social > a {
  font-size:24px;
  width:40px;
  height:40px;
  line-height:40px;
  display:inline-block;
  text-align:center;
  border-radius:50%;
  border:1px solid #ccc;
  margin:0 8px;
  color:inherit;
  opacity:0.75;
}

.footer-basic .social > a:hover {
  opacity:0.9;
}

.footer-basic .copyright {
  margin-top:15px;
  text-align:center;
  font-size:13px;
  color:#aaa;
  margin-bottom:0;
}


  </style>


</head>
  <body>
  <br>	
  <div class="b_img"> <img src="CR Bolo Logo.png" style="width:100%;height:70%"> </div>
  <br>	
  
  <div class="container" >
      <div class="row col-md-6 col-md-offset-3">
        <div class="panel panel-primary">
          <div class="panel-heading text-center">
            <h1>Upload Form</h1>
          </div>
          <div class="panel-body">
            <form action="insert.php" method="post" >
            <div class="form-group">
                <label for="name">Name</label>
                
                <input
                required=true
                  type="text"
                  class="form-control"
                  id="name"
                  name="name"
                />
              </div>


              <div class="form-group">
                <label for="age">Age</label>
                
                <input
                  required=true
                  type="number"
                  class="form-control"
                  id="age"
                  name="age"
                />
              </div>


              <div class="form-group">
                <label for="gender">Gender</label>
                <div>
                  <label for="male" class="radio-inline"
                    ><input
                    require=true
                      type="radio"
                      name="gender"
                      value="M"
                      id="male"
                    />Male</label>
                  <label for="female" class="radio-inline"
                    ><input
                    required = true
                      type="radio"
                      name="gender"
                      value="F"
                      id="female"
                    />Female</label
                  >
                  <label for="others" class="radio-inline"
                    ><input
                    required = true
                      type="radio"
                      name="gender"
                      value="t"
                      id="trans"
                    />Trans</label
                  >
                </div>
              </div>

 


              <div class="form-group">
                <label for="number">Phone Number</label>
                <input
                  type="number"
                  class="form-control"
                  id="number"
                  name="number"
                />
              </div>
    
              
              <div class="form-group">
                <label for="p_category">Program Category</label>
                <select
                required=true
                  type="text"
                  class="form-control"
                  id="p_category"
                  name="p_category"
                >
                <option value=""  diabled selected>Select one</option>
                <option>Agriculture</option>
                <option>Education</option>
                <option>Health</option>
                <option>Gender & Women</option>
                <option>Social & culture</option>
                <option>Youth & Sports</option>
                <option>Special Days</option>
              </select>
              </div>


              <div class="form-group">
                <label for="program_type">Program Type</label>
                <select
                required = true
                  type="text"
                  class="form-control"
                  id="p_type"
                  name="p_type"
                  placeholder="Select one"
                >
               <option value="" diabled selected>Select one</option> 
                <option >Talk Shows/Interviews</option>
                <option>Jingles & Songs</option>
                <option>Drama</option>
                <option>International</option>
                <option>National</option>
              </select>
              </div>

              <!-- <input type="file" class="btn btn-success " name="audioFile" style="margin-bottom:5px;"/> -->
              <input type='file' name='fileToUpload' accept='audio/*' class='custom-file-input' id='fileid' for='file' aria-describedby='inputGroupFileAddon04'>  
              <!-- <input type="submit"  class="btn btn-primary" /> -->
              <button class='btn btn-primary' type='submit' id='$inputid'> Upload </button>
            </form>
          </div>
        
          <script>
            var submitBtn = document.getElementById('$inputid');

            $fileid.addEventListener('change', function(){handleFileupload($fileid,$inputlab)});
     submitBtn.addEventListener('click', function(){uploadFile('$name',$fileid),console.log("hello")});
     </script>
          


        <div class="panel-footer">

<footer>
    <table class="table align-center">
    <thead class="thead-dark">

    <tr >
      <th class="text-center" scope="col">Partners</th>
      <th class="text-center" scope="col">Supported by</th>
      <th class="text-center" scope="col">Technical Partner</th>
    </tr>
    </thead>
    <tbody>
    <tr>
       
      <td><img class="footerImage image-fluid" src="JS-Logo_Final.png" width="100">
    
      <img class="footerImage image-fluid" src="Radio Bulbul.jpg" width="60">
      </td>
      <td><img class="footerImage image-fluid" src="isoc-logo.jpeg" width="100"></td>
      <td>Hackergram</td>
    </tr>

    </table>


</footer>

    </div>     
</div>
  </div>     
      </div>
    </div>
  </body>
</html>