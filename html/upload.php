<?php

//upload file in _files to the server

$name=$_FILES['file']['name'];
$size=$_FILES['file']['size'];
$type=$_FILES['file']['type'];
$tmp_name=$_FILES['file']['tmp_name'];

header("Location: index.php");

// File upload path
$targetDir = "uploads/";
$fileName = basename($_FILES["file"]["name"]);
$targetFilePath = $targetDir . $fileName;
$fileType = pathinfo($targetFilePath,PATHINFO_EXTENSION);

//copy file from temp location to server location
move_uploaded_file($tmp_name, $targetFilePath);
//write _Request["name"],_Request["age"] and _Request["catagory"] a csv file called data.csv
$myfile = fopen("data.csv", "a") or die("Unable to open file!");
fwrite($myfile, $_REQUEST["name"].",".$_REQUEST["age"].",".$_REQUEST["gender"].",".$_REQUEST["number"].",".$_REQUEST["p_category"].",".$_REQUEST["p_type"].",".$fileName."
");

