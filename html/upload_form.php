<!DOCTYPE html>
<html>
  <head>
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
  </style>


</head>
  <body>
   
  
  <div class="container" style="margin-top: 20px;">
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

              <input type="file" class="btn btn-success " name="audioFile" style="margin-bottom:5px;"/>
              
              <input type="submit"  class="btn btn-primary" />
            </form>
          </div>
        


        <div class="panel-footer">
            
        <small style="margin-left:15%;" >Partners</small>
        <small style="margin-left:20%;">Sponsored By</small>
        <small style="margin-left:15%;">Technical Partner</small>

        <small style="margin-right:5px;">Jadite Solutions Logo</small>
        <small > Radio Bulbul Logo</small> 

        <small style="margin-left:5px;">ISOC Logo</small>
        <small style="margin-left:18%;">Hackergram</small>
      

      
          
          


          </div>

         

        </div>
        
      </div>
     
    </div>
 
  </body>
</html>