<html>
 <head>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <style type="text/css">
    #playlist,audio{background:#666;width:400px;padding:20px;}
    .active a{color:#5DB0E6;text-decoration:none;}
    li a{color:#eeeedd;background:#333;padding:5px;display:block;}
    li a:hover{text-decoration:none;}
    
  </style>
 
  <!-- added page loader due to delay in the page loading -->

<script src='file_upload.js'></script>
<!-- loader css ends here  -->
 </head>
 <body>
  <div id="topMenu" style="display:flex; flex-direction: row;">
	<a href="/MediaUpload/gallery.php" style="padding: 10px; background-color: #000000; color: #ffffff">Visual Gallery</a>
	<a href="/MediaUpload/upload.html" style="padding: 10px; background-color: #000000; color: #ffffff">Upload Image/Video</a>
  </div>
  <center>
   <div > <img src="wallpaper.jpg" style="width:100%;height:70%"> </div>
   <br>	
   <font size="10px">  Programs </font> 

   <br><br>	
<?php

$dirArray = array("x.wav", "x_comment.wav","x_comment2.wav" ,"y.wav","y_comment.wav");
 $filename=array();
 $comments=array();
for($index=0; $index < count($dirArray); $index++){
  if (strpos($dirArray[$index], '_comment')==FALSE){
    
    array_push($filename,$dirArray[$index]);

  }
  else{
    
    array_push($comments,$dirArray[$index]);
  }

} 

$dirArray=array();
for($i=0;$i<count($filename);$i++){
  //echo(substr($filename[$i],0,-4));
 //array_push($dirArray,$filename[$i]);
 $comment_array=[];
  for($j=0;$j<count($comments);$j++){ 
   
    //echo(strpos($comments[$j],substr($filename[$i],0,-4)));
    if(strpos($comments[$j],substr($filename[$i],0,-4))!==FALSE){
     // echo("hello");  
    
    array_push($comment_array,$comments[$j]);
    // foreach ($comment_array as $value) {
    //   echo($value);
    // } 
    // }
   
  }
//  else{break;}
  // foreach ($comment_array as $value) {
  //   echo($value);
  // } 
  
  
// foreach($dirArray["x.wav"] as $key=>$value)
// {

//   echo $value;
// }

}
$dirArray[$filename[$i]]=$comment_array;
}

//echo(count($dirArray["x.wav"]));
// for($i=0;$i<count($dirArray["x.wav"]);$i++){
//   echo($dirArray["x.wav"][$i]);

//   }

// foreach($dirArray["y.wav"] as $value)
// {
//   echo $value;
// }
$flag=0;
     
     
// (Randomly) Loops through the array of files
foreach($dirArray as $key => $val) {
 
 //Loops through the array of files
 //for($index=0; $index < $indexCount; $index++) {
 
 // Gets File Names
 $name=$key;
 $name=$key;	
//  $ext = findexts($name);

 if (strlen($name)>='3'){
   $div_index=0;
   $str_index=strval($div_index);
   $fileid = "inputFile".$str_index;
//   echo($fileid);
   $inputid="inputFileUploadButton".$str_index;
   $inputlab="inputFileLabel".$str_index;
   $div_index++;
   


if ($flag==0){
// echo 'em

echo("
<audio autoplay id='audio' preload='none' tabindex= '0' controls='' type='audio/mpeg'>
      <source src='.upload/gencat/$name'>
      Sorry, your browser does not support HTML5 audio.
     </audio>
     <div class='accordion' id='playlist'>
  <div class='accordion-item>
    <h2 class='accordion-header' id='headingOne'>
    <a href='./.upload/gencat/$name'> $name</a>
      <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseOne' aria-expanded='false' aria-controls='collapseOne'>
      see comments for $name </button>
        </h2>
        <div id='collapseOne' class='accordion-collapse collapse' aria-labelledby='headingOne' data-bs-parent='#playlist'>
<div class='accordion-body'>
"
        
   
);

// Code for upload buttons



foreach($val as $comment){
  echo("<a href=./.upload/gencat/".$comment.">$comment</a><br></div>");

}
echo("
</div>
<div>
<div class='input-group'>
<div class='custom-file'>
<p class='comment'> Share a comment</p> 
 <input type='file' accept='audio/*' class='custom-file-input' id='$fileid' aria-describedby='inputGroupFileAddon04'>


</div>    
  </button>
</h2>
<label class='custom-file-label' id='$inputlab' for='$fileid'>Choose file</label>
</div>
<div class='input-group-append'>
<button class='btn btn-primary' type='button' id='$inputid' >Upload</button>
</div>
</div>
<div class='progress'>
<div id='progressbar' class='progress-bar bg-success' role='progressbar' style='width: 5%' aria-valuenow='0'
aria-valuemin='0' aria-valuemax='100'></div>
</div> 



<script>
var $fileid = document.getElementById('$fileid');
var $inputlab = document.getElementById('$inputlab');
var submitBtn = document.getElementById('$inputid');
var progressBar = document.getElementById('progressbar');

$fileid.addEventListener('change', function(){handleFileupload($fileid,$inputlab)});
submitBtn.addEventListener('click', function(){uploadFile('$name',$fileid)});
</script>

");

$flag=1;
}
else{    
    // echo 'em
    echo("
     
      
  <a href='./.upload/gencat/$name'>$name</a>
  <button class='accordion-button' type='button' data-bs-toggle='collapse' data-bs-target='#collapseOne$div_index' aria-expanded='false' aria-controls='collapseOne$div_index'>
  see comments for $name </button>

");


echo("<div>
<div class='input-group'>
<div class='custom-file'>
<p class='comment'> Share a comment</p> 
 


<div id='collapseOne$div_index' class='accordion-collapse collapse' aria-labelledby='headingOne' data-bs-parent='#playlist'>
<div class='accordion-body'>");
foreach($val as $comment){
  echo("<a href=./.upload/gencat/".$comment.">$comment</a><br></div>");

}
echo("
</div>
<div>
<div class='input-group'>
<div class='custom-file'>
<p class='comment'> Share a comment</p> 
 <input type='file' accept='audio/*' class='custom-file-input' id='$fileid' aria-describedby='inputGroupFileAddon04'>


</div>    
  </button>
</h2>
<label class='custom-file-label' id='$inputlab' for='$fileid'>Choose file</label>
</div>
<div class='input-group-append'>
<button class='btn btn-primary' type='button' id='$inputid' >Upload</button>
</div>
</div>
<div class='progress'>
<div id='progressbar' class='progress-bar bg-success' role='progressbar' style='width: 5%' aria-valuenow='0'
aria-valuemin='0' aria-valuemax='100'></div>
</div> 



<script>
var $fileid = document.getElementById('$fileid');
var $inputlab = document.getElementById('$inputlab');
var submitBtn = document.getElementById('$inputid');
var progressBar = document.getElementById('progressbar');

$fileid.addEventListener('change', function(){handleFileupload($fileid,$inputlab)});
submitBtn.addEventListener('click', function(){uploadFile('$name',$fileid)});
</script>

");

 
   }
  }
 }
 ?>
</center>

</ul> 	

</body>
<script
type="text/javascript"
src="./jquery-1.7.js"

></script>
<script src='./MediaUpload/audio_new.js'></script>


</html>



  
