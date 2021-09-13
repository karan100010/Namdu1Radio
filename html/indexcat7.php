
<html>
 <head>

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
    
     // Opens directory
     //$myDirectory=opendir("./.upload/cat7/");

     // Gets each entry
     //while($entryName=readdir($myDirectory)) {
     // $dirArray[]=$entryName;
     //}
 $dirArray=glob('.upload/cat7/*.mp3');
 usort($dirArray, function($a, $b) {
     return filemtime($a) - filemtime($b);
 });

// print_r($dirArray);
 //rsort($dirArray);
 $filename=array();
 $comments=array();
for($index=0; $index < count($dirArray); $index++){
  if (strpos($dirArray[$index], '_comment')!==FALSE){
    
    array_push($comments,$dirArray[$index]);
  }

  
  else{
    array_push($filename,$dirArray[$index]);

  }
    

} 

$dirArray=array();

for($i=0;$i<count($filename);$i++){
  //echo(substr($filename[$i],0,-4));
 array_push($dirArray,$filename[$i]);
  for($j=0;$j<count($comments);$j++){ 
    //echo(strpos($comments[$j],substr($filename[$i],0,-4)));
    if(strpos($comments[$j],substr($filename[$i],0,-4))!==FALSE){
     // echo("hello");  
      array_push($dirArray,$comments[$j]);
    }

  }

}


     // Finds extensions of files
/*      function findexts($filename) {
      for ($i=0;$filename[$i]!=NULL;$i++){}
	$exts = $filename[$i];
      return $exts;
     } */

     // Closes directory
     //closedir($myDirectory);

     // Counts elements in array
     $indexCount=count($dirArray);

     // Sorts files
     //sort($dirArray);
    //   sort($dirArray);//sorting in descendi
      
      // print($indexCount);
	
     $flag=0;
     
     
     // (Randomly) Loops through the array of files
     for($index=0; $index < $indexCount; $index++) {
      
      //Loops through the array of files
      //for($index=0; $index < $indexCount; $index++) {
      
      // Gets File Names
      $m=explode('/',$dirArray[$index]);
      // $z=end($m);
      // print($z);
      $name=end($m);
      
    //  $ext = findexts($name);
	
      if (strlen($name)>='3'){
        $str_index=strval($index);
        $fileid = "inputFile".$str_index;
     //   echo($fileid);
        $inputid="inputFileUploadButton".$str_index;
        $inputlab="inputFileLabel".$str_index;
        

	
	if ($flag==0){
	 // echo 'em
 
  	 echo("
	  <audio autoplay id='audio' preload='auto' tabindex= '0' controls='' type='audio/mpeg'>
           <source src='.upload/cat7/$name'>
           Sorry, your browser does not support HTML5 audio.
          </audio>
		
	  <ul id='playlist'>
     	 
      	  
           <li class='active'>
 	    <a href='.upload/cat7/$name'>$name</a>
       <div>
       <div class='input-group'>
         <div class='custom-file'>
         <p class='comment'> Share a comment</p> 
           <input type='file' accept='audio/*' class='custom-file-input' id='$fileid' aria-describedby='inputGroupFileAddon04'>
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
     
 "
    );
  
 
  
	 $flag=1;
	}
	else{    
         // echo 'em
         echo("
          
           <li>
	     <a href='./.upload/cat7/$name'>$name</a>
	   </li>
     <div>
  <div class='input-group'>
    <div class='custom-file'>
    <p class='comment'> Share a comment</p> 
      <input type='file' accept='audio/*' class='custom-file-input' id='$fileid' aria-describedby='inputGroupFileAddon04'>
    
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
</script>");
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
  <script src='./MediaUpload/audio.js'></script>
  
 
</html>
