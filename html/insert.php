<!DOCTYPE html>
<html>
 
<head>
    <title>Upload page</title>
</head>
 
<body>
    <center>
     <?php
 
         $servername = "localhost";
         $username = "root";
         $password = "";
         $dbname = "staff";
        $conn = mysqli_connect("localhost", "root", "", "staff");
         
        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. "
                . mysqli_connect_error());
        }
        // trial 
        
        // Taking all 5 values from the form data(input)
        $name =  $_REQUEST['name'];
        $age = $_REQUEST['age'];
        $gender =  $_REQUEST['gender'];
        $number = $_REQUEST['number'];
        $p_category = $_REQUEST['p_category'];
        $p_type = $_REQUEST['p_type'];
         
 
        // Performing insert query execution
        // here our table name is upload_data
        //Checking for digits od $number and running insert query.
        if(strlen($number)==10 || strlen($number)==0)
        {
            $sql = "INSERT INTO upload_data  VALUES ('$name',
            '$age','$gender','$number','$p_category','$p_type')";

            if(preg_match("/^[0-9]*$/", $number) && mysqli_query($conn, $sql))
            {
                echo "Upload Successful!";
            }

        }
        else{
            if(strlen($number)>10 || strlen($number)<10)
            {
                echo "Phone number you entered dosen't have 10 digits";
            }
            
            else{
              echo "ERROR: Hush! Sorry $sql. "
                . mysqli_error($conn);
            }
        }




         
       // Close connection
        mysqli_close($conn);
        ?> 

</body>

    </center>


 
</html>