<!DOCTYPE html>
<html>
 
<head>
    <title>Upload page</title>
</head>
 
<body>
    <center>
     <?php
     //upload file in _REQUEST method

 
        //  $servername = "localhost";
        //  $username = "root";
        //  $password = "root";
        //  $dbname = "upload_form";
         
        // $conn = mysqli_connect("localhost", "root", "root", "upload_form");
         
        // // Check connection
        // if($conn === false){
        //     die("ERROR: Could not connect. "
        //         . mysqli_connect_error());
        // }
        // // trial 
        
        // // Taking all 5 values from the form data(input)
        // $name =  $_REQUEST['name'];
        // $age = $_REQUEST['age'];
        // $gender =  $_REQUEST['gender'];
        // $number = $_REQUEST['number'];
        // $p_category = $_REQUEST['p_category'];
        // $p_type = $_REQUEST['p_type'];
         
 
        // // Performing insert query execution
        // // here our table name is upload_data
        // //Checking for digits od $number and running insert query.
        // if(strlen($number)==10 || strlen($number)==0)
        // {
        //     $sql = "INSERT INTO upload_data  VALUES ('$name',
        //     '$age','$gender','$number','$p_category','$p_type')";

        //     if(preg_match("/^[0-9]*$/", $number) && mysqli_query($conn, $sql))
        //     {
        //         echo "Upload Successful!";
        //     }

        // }
        // else{
        //     if(strlen($number)>10 || strlen($number)<10)
        //     {
        //         echo "Phone number you entered dosen't have 10 digits";
        //     }
            
        //     else{
        //       echo "ERROR: Hush! Sorry $sql. "
        //         . mysqli_error($conn);
        //     }
        // }


      
        // print keys of _REQUEST
//get tmp location of the selected file and print it

//get the name of the selected file and print it

//print all the key value pairs of $_FILES
echo "<pre>";
print_r($_FILES);
echo "</pre>";

$x=[1,2,3,4,5,6,7,8,9,10];
print_r($x);


// $fileName = $_POST["fileToUpload"]; // The file name
//  $fileTmpLoc = $_REQUEST["fileToUpload"]["tmp_name"]; // File in the PHP tmp folder
// // $fileType = $_FILES["fileToUpload"]["type"]; // The type of file it is
// // $fileSize = $_FILES["fileToUpload"]["size"]; // File size in bytes
// // $fileErrorMsg = $_FILES["fileToUpload"]["error"]; // 0 for false... and 1 for true



// move_uploaded_file($fileTmpLoc, '../sql/all uploads'.$fileName);
    



         
       // Close connection
        // mysqli_close($conn);
        ?> 

</body>

    </center>


 
</html>